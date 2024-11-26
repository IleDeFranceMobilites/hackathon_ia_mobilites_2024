import streamlit as st
from back import get_all_zdc, get_list_of_equipements, get_accessibilite
from edit_grievances import add_grievances
import time
from pathlib import Path
import whisper
from add_state_to_equipements import (
    AVAILABLE,
    UNAVAILABLE,
    UNCERTAIN_AVAILABLE,
    UNCERTAIN_UNAVAILABLE,
    UNCERTAIN,
)

st.set_page_config(page_title="Hackathon accessibilité")


@st.cache_resource
def get_whisper():
    return whisper.load_model("base")


@st.dialog("Signalement")
def grieve(key, supposed_state):
    left, right = st.columns([0.8, 0.2])
    text = left.text_area("décrivez la situation (optionnel)")
    audio = right.audio_input("", key="audio_input_" + key)
    if audio:
        with open("audio.wav", "wb") as f:
            f.write(audio.getbuffer())
        text = get_whisper().transcribe("audio.wav", language="fr", fp16=False)["text"]
        st.write(text)
        time.sleep(4)
    skip = st.button("Ignorer")
    if len(text) > 0 or skip:
        add_grievances(key, supposed_state, text)
        st.rerun()


# @st.dialog("Quel est le problème avec l'équipement ?")
# def grieve(key, supposed_state):
#     text = st.text_area("décrivez la situation (optionnel)")
#     left, right = st.columns(2)
#     if left.button("Problème"):
#         add_grievances(key, UNAVAILABLE, text)
#     if right.button("En fonctionnement"):
#         add_grievances(key, AVAILABLE, text)

# audio = audiorecorder("Dites vos doléances", key=key+"_audio_input")
# if audio:
#     audio.export("audio.wav", format="wav")
#     transcription = get_whisper().transcribe("audio.wav")
#     st.write(transcription["text"])
# audio = st.audio_input("Dites vos doléances", key="audio_input_" + key)
# result = st.text_area("Ecrivez vos doléances", key="text_area_" + key)
# # , value=st.session_state.get("text", ""))
# if audio:
#     with open("audio.wav", "wb") as f:
#         f.write(audio.getbuffer())
#     result = get_whisper().transcribe("audio.wav", language="fr")["text"]
#     st.write(result)
# if len(result) > 0:
#     add_grievances(key, state, result)
#     # st.write("done")


zdc = st.selectbox("Sélectionner gare", get_all_zdc(), index=None)

if zdc is None:
    st.stop()

if not (accessibility := get_accessibilite(zdc)).empty:
    st.info(accessibility["accessibility_level_name"].iloc[0].capitalize())


# st.image(
#     f"http://estacions.albertguillaumes.cat/img/paris/{zdc.lower()}.png", width=100
# )
zdc_formatted = (
    zdc.replace(" - ", "_")
    .replace(" ", "_")
    .replace("é", "e")
    .replace("è", "e")
    .replace("-", "_")
    .lower()
)
path = Path(f"static/img/{zdc_formatted}.png")
if path.exists():
    st.image(str(path))
# st.html(
#     f"<img src='http://estacions.albertguillaumes.cat/img/paris/{zdc_formatted}.png'>"
# )

for type_of_equipment, d in get_list_of_equipements(zdc).items():
    for key, values in d.items():
        left, middle_left, middle_right, right = st.columns(
            [0.3, 0.1, 0.3, 0.3], vertical_alignment="center"
        )

        state = values.get("state")

        if type_of_equipment == "elevators":
            left.write(str(values["liftsituation"] or "ascenseur inconnu"))
        elif type_of_equipment == "escalators":
            left.write(str(values["etage"] or "escalator inconnu"))

        middle_left.image(f"static/img/{type_of_equipment}.png", width=50)

        if state == AVAILABLE or state == UNCERTAIN_AVAILABLE:
            message = "signaler un problème"
            middle_right.image(
                "static/img/thumb-up.png",
                width=20,
            )
        elif state == UNAVAILABLE or state == UNCERTAIN_UNAVAILABLE:
            message = "l'équipement fonctionne"
            middle_right.image(
                "static/img/thumb-down.png",
                width=20,
            )
            middle_right.markdown(" / ".join(values["reasons_grievances"]))
        else:
            message = "décrire le fonctionnement de l'équipement"
            middle_right.image(
                "static/img/question.png",
                width=20,
            )

        if right.button(message, key=key):
            grieve(
                key,
                (
                    AVAILABLE
                    if state in [UNAVAILABLE, UNCERTAIN_UNAVAILABLE]
                    else (
                        UNAVAILABLE
                        if state in [AVAILABLE, UNCERTAIN_AVAILABLE]
                        else UNCERTAIN  # stays uncertain whatever the message
                    )
                ),
            )

import streamlit as st
from streamlit_geolocation import streamlit_geolocation

from sources.agent.agent import invoke_agent
from sources.converter.text_to_speech import generate_audio
from sources.converter.speech_to_text import recognize_speech

st.markdown(
    """
    <style>
    .center-logo {
        display: flex;
        justify-content: center;
        align-items: center
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="center-logo">', unsafe_allow_html=True)
st.image("images/logo_idfm.png", width=2000)
st.markdown('</div>', unsafe_allow_html=True)

st.title("Recherchez votre itinéraire avec Mob'IA")
st.markdown("""<span style='color: black;'>Bienvenue, appuyez sur "Enregistrer" pour enregistrer votre demande</span>""", unsafe_allow_html=True)
if location := streamlit_geolocation():
    if location.get('longitude') is not None:
        user_location = ';'.join([str(location.get('longitude')), str(location.get('latitude'))])
        st.markdown("""<span style='color: green;'>Geolocalisation active</span>""", unsafe_allow_html=True)

    else:
        user_location = "Inconnue"
        st.markdown("""<span style='color: red;'>Geolocation inactive</span>""", unsafe_allow_html=True)


if 'button' not in st.session_state:
    st.session_state.button = False


def click_button():
    st.session_state.button = True


st.button("Enregistrer", on_click=click_button)

if st.session_state.button:
    user_input = recognize_speech()
    st.text_area("Retranscription :", user_input)
    agent_response = invoke_agent(user_input, user_location)
    audio = generate_audio(agent_response)
    st.audio(audio, autoplay=True)

    st.session_state.button = False

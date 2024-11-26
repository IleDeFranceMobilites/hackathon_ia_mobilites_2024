import streamlit as st
import disruption_generation
import time
from itinerary_calculator import ItineraryCalculator
from itinerary_data import Itinerary
from dataclasses import asdict
from langchain_openai import generate_messages
from dotenv import load_dotenv
import front_map

load_dotenv(override=True)

st.markdown("###")

st.title("IVoice")

###

def message_generation(itineraries: dict[str, list[Itinerary]], infos_incident: str):
    it_dict = {k: [asdict(it) for it in v] for k, v in itineraries.items()}
    messages = generate_messages(it_dict, infos_incident, "Métro 9")
    return messages


def itineraire_generation():
    it_calc = ItineraryCalculator()
    itineraries = it_calc.compute_alternate_itineraries(line_id="IDFM:C01379")
    return itineraries

def generation_incident():
    result = disruption_generation.create_disruption()
    st.markdown(result.message, unsafe_allow_html=True)
    return result.message

def loading_itineraire() -> dict[str, list[Itinerary]]:
    with st.spinner("Génération de l'itinéraire:"):
        itinerary = itineraire_generation()
    st.success("Itinéraire généré !")
    return itinerary

def loading_message(itinerary: dict[str, list[Itinerary]], infos_incident: str) -> dict[str, str]:
    with st.spinner("Génération du message"):
        messages = message_generation(itinerary, infos_incident)
    st.success("Message généré !")
    return messages

def print_messages(messages: dict[str, str]):
    for key in messages.keys():
        result = f"{key}: {messages.get(key)}"
        st.write(result)

def print_map(messages):
    # map_dictionnary doit être l'output de message_generation
    map_dictionnary = messages
    st.components.v1.html(front_map.create_map(map_dictionnary), scrolling=True, height=500)


def print_results():
    infos_incident = generation_incident()
    st.write("\n")
    itinerary = loading_itineraire()
    st.write("\n")
    messages = loading_message(itinerary, infos_incident)
    print_map(messages)
    st.write("\n")
    print_messages(messages)


with st.container():
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button('Générer un incident'):
        print_results()
    st.markdown('</div>', unsafe_allow_html=True)

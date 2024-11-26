from langchain_core.tools import tool

from langchain_community.tools import TavilySearchResults
from langchain_core.tools import tool
from server.directions import DirectionsAPI
import os
directions_api = DirectionsAPI(api_key=os.getenv(
    'DIRECTIONS_API_KEY', 'REMOVED'))


@tool
def add(a: int, b: int):
    """Add two numbers. Please let the user know that you're adding the numbers BEFORE you call the tool"""
    return a + b


@tool
async def check_address(address: str):
    """
    Disambiguate or check an address using the geocoding API.
    Let the user know you're checking the address before calling this tool.

    :param address: The address to disambiguate (e.g., "Eiffel Tower, Paris")
    :return: A dictionary containing the latitude, longitude, and full address label
    """
    try:
        from server.geocode import GeocodingAPI
        geocoding_api = GeocodingAPI()
        result = await geocoding_api.geocode(address)
        results_list = []
        for item in result:
            results_list.append({
                "latitude": item["lat"],
                "longitude": item["lon"],
                "full_address": item["label"]
            })
        return results_list
        # return {
        #     "latitude": result["lat"],
        #     "longitude": result["lon"],
        #     "full_address": result["label"]
        # }
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

import base64
import requests
from typing import Optional

@tool
async def analyze_image(image_url: str, prompt: Optional[str] = None):
    """
    Analyze an image using GPT-4 Vision and return a description.
    PS : If there is any text, you must read it to the user.
    Let the user know you're analyzing the image before calling this tool.

    :param image_url: The URL of the image to analyze
    :param prompt: Optional. A specific prompt to guide the image analysis
    :return: A description of the image
    """
    try:
        # Fetch the image
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content

        # Encode the image to base64
        base64_image = base64.b64encode(image_data).decode('utf-8')

        # Prepare the payload for the OpenAI API
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt if prompt else "Peux tu me dire ce qui est écrit sur cette image ?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        # Make the API call
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
        }
        api_response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
        api_response.raise_for_status()

        # Extract and return the description
        result = api_response.json()
        return result['choices'][0]['message']['content']

    except requests.RequestException as e:
        return f"Error fetching or analyzing the image: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


@tool
async def get_journey_info(start: str, destination: str, datetime_str: str = None, wheelchair: bool = False):
    """
    Get journey information between two points.
    Let the user know you're fetching journey information before calling this tool.

    :param start: Starting point (e.g., "Eiffel Tower, Paris") You must be as precise as possible
    :param destination: Destination point (e.g., "Louvre Museum, Paris") Similarly, you must precise the region or city if available.
    :param datetime_str: Optional. Departure or arrival time in ISO 8601 format (e.g., "20230615T143000")
    :param wheelchair: Optional. Set to True for wheelchair-accessible routes
    :return: Parsed journey information
    """
    journey_data = await directions_api.get_journey_from_verbal_points(start, destination, datetime_str, wheelchair)
    if journey_data:
        return directions_api.parse_journey_data(journey_data)
    else:
        return "Unable to fetch journey information. Please check the provided locations and try again."


# tavily_tool = TavilySearchResults(
#     max_results=5,
#     include_answer=True,
#     description=(
#         "This is a search tool for accessing the internet.\n\n"
#         "Let the user know you're asking your friend Tavily for help before you call the tool."
#     ),
# )

TOOLS = [add, get_journey_info, check_address, analyze_image]

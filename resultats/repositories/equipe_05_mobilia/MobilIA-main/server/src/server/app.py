from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import os
from directions import DirectionsAPI
import uvicorn
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse  # Add JSONResponse here
from starlette.routing import Route, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocket
from starlette.requests import Request

from langchain_openai_voice import OpenAIVoiceReactAgent


from server.utils import websocket_stream
from server.prompt import INSTRUCTIONS
from server.tools import TOOLS
from dotenv import load_dotenv

load_dotenv()

# Configure CORS middleware
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all methods
        allow_headers=["*"],  # Allows all headers
    )
]

# Update the Starlette app initialization to include the middleware

# Mount static files


async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    browser_receive_stream = websocket_stream(websocket)

    agent = OpenAIVoiceReactAgent(
        model="gpt-4o-realtime-preview",
        tools=TOOLS,
        instructions=INSTRUCTIONS,
    )

    await agent.aconnect(browser_receive_stream, websocket.send_text)


async def homepage(request):
    with open("src/server/static/index.html") as f:
        html = f.read()
        return HTMLResponse(html)


# catchall route to load files from src/server/static


async def get_directions(request: Request):
    try:
        # Extract parameters from the request
        params = request.query_params
        origin_long = params.get('origin_long')
        origin_lat = params.get('origin_lat')
        dest_long = params.get('dest_long')
        dest_lat = params.get('dest_lat')
        datetime_str = params.get('datetime')
        wheelchair = params.get('wheelchair', 'false').lower() == 'true'

        # Validate required parameters
        if not all([origin_long, origin_lat, dest_long, dest_lat, datetime_str]):
            return JSONResponse({"error": "Missing required parameters"}, status_code=400)

        # Get journey information
        journey_data = await directions.get_journey_info(
            origin_long, origin_lat, dest_long, dest_lat, datetime_str, wheelchair
        )

        if journey_data is None:
            return JSONResponse({"error": "Failed to fetch journey information"}, status_code=500)

        # Parse journey data
        parsed_journeys = directions.parse_journey_data(
            journey_data)  # Remove await here

        return JSONResponse(parsed_journeys)

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


routes = [
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
    Route("/api/directions", get_directions, methods=["GET"])
]

app = Starlette(debug=True, routes=routes, middleware=middleware)

app.mount("/", StaticFiles(directory="src/server/static"), name="static")

# app = Flask(__name__)

# # Configuration
# app.config['DEBUG'] = True  # Enable debug mode for development
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

# Initialize DirectionsAPI with API key from environment variable
directions = DirectionsAPI(api_key=os.getenv('DIRECTIONS_API_KEY', ''))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

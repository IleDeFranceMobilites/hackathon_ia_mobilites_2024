from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Need to specify the list of ports, else it wont work with only "*"
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://10.244.1.53:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON Data
with open('../../frontend-angular/db.json', 'r') as file:
    data = json.load(file)

# Extract user data
users = data['users']

@app.get("/summarize_user_data", response_class=HTMLResponse)
async def summarize_user_data():
    summary = {
        "total_users": len(users),
        "total_preferences": len(users),  # Assuming each user has one preference
        "user_names": [user["name"] for user in users]
    }
    html_content = f"""
    <html>
        <body>
            <h1>Summary:</h1>
            <pre>{json.dumps(summary, indent=4)}</pre>
        </body>
    </html>
    """
    return html_content


from collections import defaultdict
from fastapi import Request


# Function to summarize conversation messages
def summarize_conversations(conversations):
    summary = defaultdict(list)
    for conversation in conversations:
        user_id = conversation["userId"]
        summary[user_id].append(conversation["message"])
    return summary


conversations = data.get("conversations", [])

@app.get("/summarize_conversations", response_class=HTMLResponse)
async def summarize_conversations_endpoint(request: Request):
    # Extract conversation data from the request (replace this with actual data extraction logic)

    # Summarize the conversation messages
    conversation_summary = summarize_conversations(conversations)

    # Format the summary as HTML
    summary_html = "<html><body><h1>Conversation Summary:</h1><pre>"
    for user_id, messages in conversation_summary.items():
        summary_html += f"User {user_id}:\n"
        for message in messages:
            summary_html += f"  - {message}\n"
    summary_html += "</pre></body></html>"

    return HTMLResponse(content=summary_html)






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)

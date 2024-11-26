import uvicorn
from idfmhk24.app import app


def main():
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

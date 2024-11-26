# load env variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('secrets.env'), override=True)
load_dotenv(find_dotenv('.env'), override=True)

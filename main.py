from client import ApiClient
from os import environ
from time import sleep
from dotenv import load_dotenv

# Load the secrets from the .env file
load_dotenv()

# Create an APIClient Object and print the result of a call to /organization
client = ApiClient(environ.get('ORG_NAME'), environ.get('API_KEY'), environ.get('API_SECRET'))

if result:= client.GetSkipDates(10):
    print(result[0])





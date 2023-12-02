import requests
import uuid
import json

with open("config.json", "r") as file:
    config = json.load(file)

ENDPOINT = config["endpoint"]
PATH = config["path"]
LOCATION = config["location"]
KEY = config["key"]

def get_translation(text):
    # Add your key and endpoint

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['zu']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': LOCATION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    try:
        # Make the translation request
        request = requests.post(ENDPOINT + PATH, params=params, headers=headers, json=body)
        request.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Process the response
        response = request.json()
        translation_text = response[0]['translations'][0]['text']

        return translation_text

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (4xx and 5xx)
        raise TranslationError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        raise TranslationError(f"Request error occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        # Handle JSON decoding errors
        raise TranslationError(f"JSON decoding error occurred: {json_err}")
    except KeyError as key_err:
        # Handle key errors in the response structure
        raise TranslationError(f"Key error occurred: {key_err}")
    except Exception as e:
        # Handle other unexpected errors
        raise TranslationError(f"An unexpected error occurred: {e}")

# Custom exception for translation errors
class TranslationError(Exception):
    pass
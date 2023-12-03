"""

- 'requests' module is used for making HTTP requests.
- 'uuid' module provides functions for generating and working with UUIDs.
- 'json' module is used for encoding and decoding JSON data

Example usage:

import requests
# Make an HTTP GET request
response = requests.get('https://api.example.com/data')
print(response.json())

import uuid
# Generate a random UUID
random_uuid = uuid.uuid4()
print(random_uuid)

import json
# Encode a Python object to JSON
data = {'key': 'value'}
json_data = json.dumps(data)
print(json_data)

"""

import uuid
import json
import requests

from constants import PREFIX_TRACE_ID, TIMEOUT_SECONDS


with open("config.json", "r", encoding='utf-8') as file:
    config = json.load(file)

ENDPOINT = config["endpoint"]
PATH = config["path"]
LOCATION = config["location"]
KEY = config["key"]

def get_translation(text, language):

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': LOCATION,
        'Content-type': 'application/json',
        'X-ClientTraceId': f'{PREFIX_TRACE_ID}-{str(uuid.uuid4())}'
    }

    body = [{
        'text': text
    }]

    url = ENDPOINT + PATH
    timeout = TIMEOUT_SECONDS

    try:

        request = requests.post(url, params=params, headers=headers, json=body, timeout=timeout)
        request.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Process the response
        response = request.json()
        translation_text = response[0]['translations'][0]['text']

        return translation_text

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (4xx and 5xx)
        raise TranslationError(f"HTTP error occurred: {http_err}") from http_err
    except requests.exceptions.Timeout as req_err:
        raise TranslationError(f"Request timed out.: {req_err}") from req_err
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        raise TranslationError(f"Request error occurred: {req_err}") from req_err
    except json.JSONDecodeError as json_err:
        # Handle JSON decoding errors
        raise TranslationError(f"JSON decoding error occurred: {json_err}") from json_err
    except KeyError as key_err:
        # Handle key errors in the response structure
        raise TranslationError(f"Key error occurred: {key_err}") from key_err
    except Exception as e:
        # Handle other unexpected errors
        raise TranslationError(f"An unexpected error occurred: {e}") from e

# Custom exception for translation errors
class TranslationError(Exception):
    """Custom exception for translation errors."""
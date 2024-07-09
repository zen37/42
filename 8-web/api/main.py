import requests
from requests.auth import HTTPBasicAuth  # For basic authentication

owner= "<...>"
repo = "<...>"
#token should not be in the copde!!!
token = "<...>"

# GitHub API endpoint for repositories
repo_url = 'https://api.github.com/repos/{owner}/{repo}'

url = repo_url.format(owner=owner, repo=repo)

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Print repository information
    repo_info = response.json()
    print(f"Repository Name: {repo_info['full_name']}")
    print(f"Description: {repo_info['description']}")
    print(f"URL: {repo_info['html_url']}")
else:
    print(f"Failed to retrieve repository information. Status code: {response.status_code}")
    print(f"Response: {response.text}")

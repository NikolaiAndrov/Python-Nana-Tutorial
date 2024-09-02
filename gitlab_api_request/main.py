import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
projects = response.json()

for project in projects:
    print(f"Project Name: {project['name']}. Project Url {project['web_url']}")
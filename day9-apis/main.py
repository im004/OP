import requests

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"User '{username}' not found.")
            return None
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("No Internet connection. Please check your network settings.")
        return None
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
        return None
    
user = input("Enter a GitHub username: ")
user = fetch_github_user(user)

if user:
    print(f"Username: {user['login']}")
    print(f"Name: {user.get('name', 'N/A')}")
    print(f"Public Repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
    print(f"Following: {user['following']}")


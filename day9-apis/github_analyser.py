import requests
import json

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("No Internet connection. Please check your network settings.")
        return None
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
        return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None
    
def analyse_repos(repos):
    if repos is None:
        return None
    
    languages = {}
    total_stars = 0
    repos_names = []

    for repo in repos:
        repos_names.append(repo['name'])
        total_stars += repo['stargazers_count']
        lang = repo.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
        
    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "languages": languages,
        "repos_names": repos_names,
        "most_used_language": max(languages, key=languages.get) if languages else None
    }

def print_report(username, analysis):
    if not analysis:
        print("No data to report")
        return

    print(f"\n======= GitHub Report: {username} =======")
    print(f"Public Repos:       {analysis['total_repos']}")
    print(f"Total Stars:        {analysis['total_stars']}")
    print(f"Most Used Language: {analysis['most_used_language']}")
    print(f"\nLanguage Breakdown:")
    for lang, count in sorted(analysis["languages"].items(), key=lambda x: x[1], reverse=True):
        print(f"  {lang}: {count} repo(s)")
    print(f"\nRepositories:")
    for name in analysis["repos_names"]:
        print(f"  - {name}")

def save_report(username, analysis):
    filename = f"{username}_github_report.json"
    with open(filename, 'w') as f:
        json.dump(analysis, f, indent=4)
    print(f"Report saved to {filename}")


def main():
    username = input("Enter a GitHub username: ")
    repos = get_user_repos(username)
    analysis = analyse_repos(repos)
    print_report(username, analysis)
    save_report(username, analysis)

if __name__ == "__main__":
    main()


import os
import time
import git
import requests


ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

repo = git.Repo('.')
commit = repo.commit('HEAD')
repository_url = repo.remotes.origin.url.split('.git')[0]
# For remote repositories
repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
user_name = repo.remotes.origin.url.split('.git')[0].split('/')[-2]

commit_url = f"{repository_url}/commit/{commit.hexsha}"


print(repo);
print(commit);
print(repository_url)
print(repo_name)
print(user_name)

print(commit_url)


headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    'X-GitHub-Api-Version': '2022-11-28',
}

response = requests.get(f"https://api.github.com/repos/{user_name}/{repo_name}/dependency-graph/compare/HEAD", headers=headers)

print(response)
#https://github.com/PyGithub/PyGithub

from github import Github

ACCESS_TOKEN = 'access token'
g = Github(ACCESS_TOKEN)

def repo_commit_count():
    for repo in g.get_user().get_repos():
     print(repo.name, repo.get_commits().totalCount)

if __name__ == '__main__':
    repo_commit_count()
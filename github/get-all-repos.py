from github import Github

ACCESS_TOKEN = 'access token'
g = Github(ACCESS_TOKEN)

def get_user():
    print('Username is: ' + str(g.get_user().name))

def get_repo_names():
    for repo in g.get_user().get_repos():
        print(repo.name)


if __name__ == '__main__':
    get_user()
    get_repo_names()
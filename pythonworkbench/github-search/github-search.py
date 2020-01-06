#https://python.gotrained.com/search-github-api/

from github import Github

ACCESS_TOKEN = 'ec93ccff88e95d635fecce9752da5d03bce842f5'
g = Github(ACCESS_TOKEN)
print(g.get_user().get_repos())

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repos(s)')

    for repo in result:
        print(repo.clone_url)

if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)
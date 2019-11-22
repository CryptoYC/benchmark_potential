import json
import time
import requests
from .models import Repository
from . import db


def get_repositories_topic():
    """
    Get the topic of repositories
    :return:
    """
    repositories = []
    for num in range(1, 11):
        # Sleep
        time.sleep(1)
        # Get the repositories
        url = "https://api.github.com/search/repositories"
        headers = {'Accept': "application/vnd.github.mercy-preview+json", 'Host': "api.github.com"}
        querystring = {"q": "topic:Blockchain", "page": num, "per_page": 100}
        response = requests.request("GET", url, headers=headers, params=querystring)
        topic_json = json.loads(response.text)
        # Get the name , stars and so on
        print(num)
        items = topic_json["items"]
        if len(items) > 0:
            for item in items:
                repository = Repository(name=item["name"], full_name=item["full_name"], html_url=item["html_url"],
                                        stargazers_count=item["stargazers_count"],
                                        watchers_count=item["watchers_count"],
                                        forks_count=item["forks_count"], open_issues_count=item["open_issues_count"])
                repositories.append(repository)
        if topic_json["incomplete_results"] is True:
            break
    return repositories


def insert_repositories_topic(repositories):
    """
    Insert the topic of repositories
    :param repositories:
    :return:
    """
    db.session.add_all(repositories)
    db.session.commit()

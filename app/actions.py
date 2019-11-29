import json
import requests
from dataclasses import dataclass
from . import scheduler
from . import db
from threading import Lock

lock = Lock()


@dataclass
class Repository(db.Model):
    id: int
    name: str
    full_name: str
    html_url: str
    stargazers_count: int
    watchers_count: int
    forks_count: int
    open_issues_count: int

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    full_name = db.Column(db.Text)
    html_url = db.Column(db.Text)
    stargazers_count = db.Column(db.Integer)
    watchers_count = db.Column(db.Integer)
    forks_count = db.Column(db.Integer)
    open_issues_count = db.Column(db.Integer)


def get_repositories_topic():
    """
    Get the topic of repositories
    :return:
    """
    repositories = []
    for num in range(1, 11):
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
    with scheduler.app.app_context():
        db.session.add_all(repositories)
        db.session.commit()


@scheduler.task('interval', id='get_repositories_topic_task', seconds=60)
def get_repositories_topic_task():
    had_lock = lock.acquire(blocking=False)
    # Is get lock?
    if had_lock:
        try:
            print("benchmark : Start getting Github data")
            repositories = get_repositories_topic()
            print("benchmark : Start inserting database")
            insert_repositories_topic(repositories)
            lock.release()
        except Exception as e:
            lock.release()
            raise e

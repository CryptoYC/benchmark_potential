from app.actions import get_repositories_topic,insert_repositories_topic


def get_repositories_topic_task():
    repositories=get_repositories_topic()
    insert_repositories_topic(repositories)

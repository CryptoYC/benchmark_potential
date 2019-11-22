from app.actions import get_repositories_topic, insert_repositories_topic
from . import scheduler


@scheduler.task('interval', id='get_repositories_topic_task', days=5)
def get_repositories_topic_task():
    repositories = get_repositories_topic()
    insert_repositories_topic(repositories)

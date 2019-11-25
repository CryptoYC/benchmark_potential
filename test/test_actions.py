from unittest import TestCase
from app.actions import get_repositories_topic, insert_repositories_topic
from app.actions import Repository


class TestActions(TestCase):
    def test_get_repositories_topic(self):
        get_repositories_topic()

    def test_insert_repositories_topic(self):
        repository = Repository(name="1", full_name="1", html_url="1", stargazers_count=1, watchers_count=1,
                                forks_count=1, open_issues_count=1)
        insert_repositories_topic([repository])

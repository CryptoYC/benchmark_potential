from unittest import TestCase
from app.actions import get_repositories_topic


class TestActions(TestCase):
    def test_get_repositories_topic(self):
        get_repositories_topic()

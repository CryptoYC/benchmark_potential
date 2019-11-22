from dataclasses import dataclass
from . import db


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
    name = db.Column(db.String(50))
    full_name = db.Column(db.String(150))
    html_url = db.Column(db.Text)
    stargazers_count = db.Column(db.Integer)
    watchers_count = db.Column(db.Integer)
    forks_count = db.Column(db.Integer)
    open_issues_count = db.Column(db.Integer)

from .db import db


issues_users = db.Table(
    "JoinIU",
    db.Column("issue_id", db.Integer, db.ForeignKey("Issues.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("Users.id"), primary_key=True)
)

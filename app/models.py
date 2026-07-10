from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Deployment(db.Model):
    __tablename__ = "deployments"

    id = db.Column(db.Integer, primary_key=True)

    build_number = db.Column(db.String(50), nullable=False)

    version = db.Column(db.String(20), nullable=False)

    environment = db.Column(db.String(30), nullable=False)

    status = db.Column(db.String(30), nullable=False)

    deployed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Deployment {self.build_number}>".

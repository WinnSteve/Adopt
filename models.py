"""models Pet"""

from flask_sqlalchemy import SQLAlchemy

# found this image source from Springboard solution
DEFAULT_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


class Pet(db.Model):
    """db for pets"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """returns image of pet of the default profile image"""

        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """connection for db"""

    db.app = app
    db.init_app(app)

from movieapp import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Post('{self.name}','{self.location}','{self.datetime}')"
from app import db

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f'<Appointment {self.title}>'
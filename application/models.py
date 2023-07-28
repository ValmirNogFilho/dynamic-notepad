from application import db

class Notepad(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    link = db.Column(db.String(), unique=True)
    content = db.Column(db.String(), nullable=False, default='')

    def __repr__(self) -> str:
        return f'Link do notepad: {self.link}'
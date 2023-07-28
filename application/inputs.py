from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class LinkForm(FlaskForm):
    input_link = StringField(label='Link do seu notepad: ')
    submit_button = SubmitField(label='Entrar')

class NotepadForm(FlaskForm):
    input_text = TextAreaField(label='Texto:')
    submit = SubmitField(label='Salvar')

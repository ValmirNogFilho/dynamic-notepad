from application import app, render_template
from application.inputs import LinkForm, NotepadForm
from application.models import Notepad
from application import db
from flask import redirect, url_for, request, flash
# from flask_login import login_user
from wtforms.validators import ValidationError

@app.route('/', methods=['GET', 'POST'])
def home():
    alert_text = ''
    form = LinkForm()
    if request.method == 'POST':
            form.validate()
            attempted_link = request.form.get('input_link')
            exists = Notepad.query.filter_by(link=attempted_link).first()

            if attempted_link != None:
                if exists:
                    alert_text = 'Esse link já foi utilizado anteriormente! Por favor, tente outro.'
                else:
                    row = Notepad(link=attempted_link)
                    db.session.add(row)
                    db.session.commit()
                    return redirect(f'/{attempted_link}')


    return render_template('home.html', alert_text=alert_text, form=form)


@app.route('/<link>', methods=['GET', 'POST'])
def notepad(link):

    link_exists = Notepad.query.filter_by(link=link).first()
    if not link_exists:
        return redirect(url_for('error'))
        
    form = NotepadForm()
    current_user = Notepad.query.filter_by(link=link).first()
    form.input_text.data = current_user.content
    if request.method == 'POST':
        if form.is_submitted():
            new_text = request.form.get('input_text')
            current_user.content = new_text
            db.session.commit()
            flash("Bloco de notas salvo com sucesso!", category='success')
            return redirect(url_for('home'))
    return render_template('notepad.html', form=form, current_user=current_user)

@app.route('/error')
def error():
    return render_template('error.html')
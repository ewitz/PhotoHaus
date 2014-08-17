import os
from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.wtf import Form
from flask.ext.moment import Moment


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config.from_pyfile('app.cfg')


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

@app.route('/', methods=['POST'])
def index_page_post():
	#Redirect user to the Date_Of_Events page.
	return "Enter in the date of the event!"

@app.route('/Date_Of_Events', methods=['GET'])
def date_of_events():
	#Cache selected photos somewhere and somehow... into a container/object
	return "Here are the list of events for this date!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
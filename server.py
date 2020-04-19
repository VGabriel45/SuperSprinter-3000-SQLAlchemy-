from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import data_handler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_story = db.Column(db.Text(), nullable=False)
    acceptance_criteria = db.Column(db.Text(), nullable=False)
    business_value = db.Column(db.Integer(), nullable=False)
    estimation = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default='Not yet')


@app.route('/')
@app.route('/list', methods=['GET', 'POST'])
def route_list():
    headers = data_handler.DATA_HEADER
    if request.method == "POST":
        title = request.form['title']
        if title == '':
            title = 'Unknown'
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = 'Not yet'
        new_story = Story(title=title, user_story=user_story, acceptance_criteria=acceptance_criteria,
                          business_value=business_value, estimation=estimation, status=status)
        db.session.add(new_story)
        db.session.commit()
        return redirect('/list')
    else:
        stories = Story.query.all()
        return render_template('list.html', headers=headers, stories=stories)


@app.route('/add_story', methods=['GET', 'POST'])
def add_story():
    statuses = data_handler.STATUSES
    return render_template('form.html', statuses=statuses)


@app.route('/update_story/<int:id>', methods=['GET', 'POST'])
def update_story(id):
    statuses = data_handler.STATUSES
    story = Story.query.get_or_404(id)
    if request.method == "POST":
        story.title = request.form['title']
        story.user_story = request.form['user_story']
        story.acceptance_criteria = request.form['acceptance_criteria']
        story.business_value = request.form['business_value']
        story.estimation = request.form['estimation']
        story.status = request.form['status']
        db.session.commit()
        return redirect('/list')
    else:
        return render_template('update.html', story=story, statuses=statuses)


@app.route('/delete_story/<int:id>', methods=['GET', 'POST'])
def delete_story(id):
    story = Story.query.get_or_404(id)
    db.session.delete(story)
    db.session.commit()
    return redirect('/list')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )

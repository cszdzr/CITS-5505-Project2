Requirements:
flask-wtf
flask
python-dotenv
flask-sqlalchemy
flask-migrate
flask-login
email-validator
flask-mail
pyjwt
flask-bootstrap

pip install -r requirements.txt

flask db migrate -m "setup"
flask db upgrade

flask shell
>>>from app.models import Course
>>>from app import db
>>>u = Course(name="Reverse Parallel Park", content_url='https://www.youtube.com/embed/l4LcfZeS4qw', assessment_file="rpp_test.html", thumbnail='https://i.ytimg.com/vi/l4LcfZeS4qw/hqdefault.jpg')
>>>db.session.add(u)
>>>db.session.commit()

flask run

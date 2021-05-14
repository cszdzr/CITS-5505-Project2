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

flask db migrate -m "setup"
flask db upgrade

*may need to delete migration 356d5ec 

u = Course(name="Reverse Parallel Park", content_url='https://www.youtube.com/embed/l4LcfZeS4qw', assessment_file="rpp_test.html", thumbnail='https://i.ytimg.com/vi/l4LcfZeS4qw/hqdefault.jpg')


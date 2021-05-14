from app.models import Course
from app import db

u = Course(name="Reverse Parallel Park", content_url='https://www.youtube.com/embed/l4LcfZeS4qw', assessment_file="rpp_test.html", thumbnail='https://i.ytimg.com/vi/l4LcfZeS4qw/hqdefault.jpg')
db.session.add(u)
db.session.commit()

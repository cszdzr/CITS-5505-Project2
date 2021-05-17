git clone -b master https://github.com/cszdzr/CITS-5505-Project2.git <br>

pip install -r requirements.txt <br>

flask db migrate -m "setup" <br>
flask db upgrade <br>

flask shell <br>
>from app.models import Course <br>
>from app import db <br>
>u = Course(name="Reverse Parallel Park", content_url='https://www.youtube.com/embed/l4LcfZeS4qw', assessment_file="rpp_test.html", thumbnail='https://i.ytimg.com/vi/l4LcfZeS4qw/hqdefault.jpg') <br>
>db.session.add(u) <br>
>db.session.commit() <br>

flask run <br>

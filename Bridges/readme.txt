(venv) $ pip install flask-sqlalchemy

(venv) $ pip install flask-migrate
$ENV:FLASK_APP = "main.py"
pip install FLASK_APP
(venv) $ flask db init
flask db migrate
(venv) $ flask db upgrade


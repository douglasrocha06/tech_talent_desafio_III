from app import app
from flaskext.mysql import MySQL
import os

user = os.environ['MYSQL_DATABASE_USER']
password = os.environ['MYSQL_DATABASE_PASSWORD']
db = os.environ['MYSQL_DATABASE_DB']
host = os.environ['MYSQL_DATABASE_HOST']

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = db
app.config['MYSQL_DATABASE_HOST'] = host
mysql.init_app(app)
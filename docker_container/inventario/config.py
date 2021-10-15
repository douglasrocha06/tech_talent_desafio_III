from app import app3
from flaskext.mysql import MySQL
import os

user = os.environ['MYSQL_DATABASE_USER']
password = os.environ['MYSQL_DATABASE_PASSWORD']
db = os.environ['MYSQL_DATABASE_DB']
host = os.environ['MYSQL_DATABASE_HOST']

mysql3 = MySQL()
app3.config['MYSQL_DATABASE_USER'] = user
app3.config['MYSQL_DATABASE_PASSWORD'] = password
app3.config['MYSQL_DATABASE_DB'] = db
app3.config['MYSQL_DATABASE_HOST'] = host
mysql3.init_app(app3)
from app import app2
from flaskext.mysql import MySQL
import os

user = os.environ['MYSQL_DATABASE_USER']
password = os.environ['MYSQL_DATABASE_PASSWORD']
db = os.environ['MYSQL_DATABASE_DB']
host = os.environ['MYSQL_DATABASE_HOST']

mysql2 = MySQL()
app2.config['MYSQL_DATABASE_USER'] = user
app2.config['MYSQL_DATABASE_PASSWORD'] = password
app2.config['MYSQL_DATABASE_DB'] = db
app2.config['MYSQL_DATABASE_HOST'] = host
mysql2.init_app(app2)

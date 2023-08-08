
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT
import cx_Oracle


cx_Oracle.init_oracle_client(lib_dir=r"C:\\Oracle\\instantclient_19_19")


app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = f'oracle+cx_oracle://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/xe'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1500), nullable=False)
    prediction = db.Column(db.Boolean)

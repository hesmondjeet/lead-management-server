import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.lead import Lead, Leads
from resources.agent import Agent

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:root@localhost:3306/nec')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True

api = Api(app)

api.add_resource(Lead, '/leads/<string:lead_id>')
api.add_resource(Leads, '/leads')
api.add_resource(Agent, '/agents')

if __name__ == "__main__":
    print("Started from __main__")

    @app.before_first_request
    def create_tables():
        print("creating db")
        db.create_all()

    from extensions import db
    db.init_app(app)
    app.run(port=5000, debug=True, use_reloader=False)

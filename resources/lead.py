from flask_restful import Resource, reqparse, request
from models.lead import LeadModel

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=False)
parser.add_argument('email', type=str, required=False)
parser.add_argument('phone', type=str, required=False)
parser.add_argument('status', type=int, required=False)
parser.add_argument('agent_id', type=int, required=False)


class Lead(Resource):

    @staticmethod
    def get(lead_id):
        lead = LeadModel.find_by_id(lead_id)
        if lead:
            return lead.json()
        return {'message': 'Lead not found'}, 404

    @staticmethod
    def put(lead_id):
        data = parser.parse_args()
        lead = LeadModel.find_by_id(lead_id)

        if lead is None:
            lead = LeadModel(**data)
        else:
            lead.name = data['name']
            lead.email = data['email']
            lead.phone = data['phone']
            lead.status = data['status']

        lead.save_to_db()
        return lead.json()

    @staticmethod
    def delete(lead_id):
        lead = LeadModel.find_by_id(lead_id)
        if lead:
            lead.delete_from_db()
            return {'status': 'OK', 'message': 'Delete success'}
        else:
            return {'message': 'Lead not found'}, 404


class Leads(Resource):
    @staticmethod
    def post():
        data = parser.parse_args()
        lead = LeadModel(**data)

        lead.save_to_db()

        return lead.json(), 201

    @staticmethod
    def get():
        args = request.args
        query = LeadModel.query
        if args.get('agent_id', None):
            query = query.filter(LeadModel.agent_id == args.get('agent_id', None))
        return {'leads': [lead.json() for lead in query.all()]}

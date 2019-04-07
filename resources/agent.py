from flask_restful import Resource, reqparse
from models.agent import AgentModel

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=False)


class Agent(Resource):

    @staticmethod
    def get(agent_id):
        agent = AgentModel.find_by_id(agent_id)
        if agent:
            return agent.json()
        return {'message': 'Agent not found'}, 404

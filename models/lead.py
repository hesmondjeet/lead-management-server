from extensions import db


class LeadModel(db.Model):
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    status = db.Column(db.Integer)

    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'))
    agent = db.relationship('AgentModel')

    def __init__(self, name, email, phone, status, agent_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status
        self.agent_id = agent_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'status': self.status,
            'agent_id': self.agent_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

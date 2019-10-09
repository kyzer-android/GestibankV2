import unittest
from webapp import create_app
from webapp.gestibank.models.agents import Agent
from webapp.extension import db
import logging

from webapp.gestibank.models.demandecreacompte import DemandeCreacompte


class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()





    def tearDown(self):
        db.session.remove()

    # def test_cree_client(self):
    #     demande_crea = DemandeCreacompte.query.get(1)
    #     agent = Agent.query.get(2)
    #     client = agent.cree_client(demande_crea)
    #     logging.debug(client)
    #     db.session.add(client)
    #     db.session.commit()

    # def test_lister_demandecrea(self):
    #     agent = Agent.query.get(2)
    #     list= agent.lister_demandecrea()
    #     logging.debug(list)

    def test_validation(self):
        agent = Agent.query.get(2)
        demande_crea = DemandeCreacompte.query.get(1)
        agent.validation_Crea(demande_crea, True)




if __name__ == "__main__":
    unittest.main()
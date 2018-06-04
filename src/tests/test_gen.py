import json
import unittest

from src.teams import TeamManager
from src.main import handler

class TestGenerator(unittest.TestCase):

    def setUp(self):
        with open('tests/testdata.json', 'r') as fp:
            self.body = json.load(fp)

        self.men = self.body.get('men',[])
        self.women = self.body.get('women', [])

    def test_parse(self):

        mgr = TeamManager()
        men, women = mgr.parseBody(self.body)
        self.assertEqual(len(men), len(women),
                         "Expected equal count of men and women")
        self.assertEqual(men[0].name, self.men[0]['name'],
                         "Name should match raw data")

    def test_gen(self):
        mgr = TeamManager()
        men, women = mgr.parseBody(self.body)

        sequences = mgr.pickTeams(men=men, women=women)

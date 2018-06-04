from collections import namedtuple

from .teamgen.TeamGen2 import TeamGen

Person = namedtuple('Person', ['name', 'ntrp', 'untrp'])

class TeamManager(object):
    def __init__(self, players=None):
        """ Parse players as json object """

        pass

    def makePerson(self, data):

        return Person(name=data.get('name'),
                      ntrp=data.get('ntrp'),
                      untrp=data.get('untrp', data.get('ntrp')))

    def parseBody(self, body=None):
        """ Parse json body into men and women objects """
        mData = body.get('men')
        wData = body.get('women')

        men = [self.makePerson(x) for x in mData]
        women = [self.makePerson(x) for x in wData]

        return men, women


    def pickTeams(self, men=None, women=None,
                  noDupes=False, nCourts=None, nSequences=3):

        # Calculate number fo courts based on # of men.
        # Assume # of women is the same.
        if nCourts is None:
            nCourts = len(men)/2

        if len(men) < nCourts * 2 or len(women) < nCourts * 2:
            errmsg = "Cannot pick teams, there are not enough men or women."
            errmsg += "Need %d of both. Have %d men and %d women." % (nCourts * 2, len(men), len(women))
            return {"status": {"error": errmsg}}

        tg = TeamGen(nCourts, nSequences, men, women)
        sequences = tg.generate_set_sequences(noDupes)

        if sequences is None or len(sequences) < nSequences:
            return {"status": {"error": "Could not generate the required sequences"}}

        else:
            # Put the worst sequences last.
            sequences.reverse()
            tg.display_sequences(sequences)
            tg.show_all_diffs(sequences)

            return sequences


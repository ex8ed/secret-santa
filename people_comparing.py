import random
import config
from pprint import pprint
from collections import deque


def pairUp(people_):
    """ Given a list of people, assign each one a secret santa partner
    from the list and return the pairings as a dict. Implemented to always
    create a perfect cycle"""
    random.shuffle(people_)
    partners = deque(people_)
    partners.rotate()
    return dict(zip(people_, partners))


# This list contains all members of the secret santa
p = config.people
pprint(pairUp(p))

from abc import ABCMeta, abstractmethod
class Scene(object):


    def __init__(self, trope, identity, suspense, trope):
        self.events = events
        self.id = identity
        self.suspense = suspense
        self.trope = trope



class Event(object):
    """An Abrstract event class

    """

    __metaclass__ = ABCMeta
    def __init__(self, identity, name):
        self.identity = identity
        self.name = name


class Element(object):
    __metaclass__ = ABCMeta
    def __init__(self, identity, name):
        self.identity = identity
        self.name = name



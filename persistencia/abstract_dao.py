import pickle
from abc import ABC, abstractmethod

class AbstractDAO(ABC):

    def __init__(self, datasource=''):
        self.datasource = datasource
        self.__objectCache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    @property
    def objectCache(self):
        return self.__objectCache

    def dump(self):
        pickle.dump(self.objectCache, open(self.datasource, 'wb'))

    def load(self):
        self.__objectCache = pickle.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.objectCache[key] = obj
        self.dump()

    def get(self, key):
        try:
            return self.objectCache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.objectCache.pop(key)
            self.dump()
        except KeyError:
            pass

    def get_all(self):
        return self.objectCache.values()
from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def find_all(self):
        pass

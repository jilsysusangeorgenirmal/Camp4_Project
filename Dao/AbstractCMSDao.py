from abc import ABC, abstractmethod

class CMSDaoService(ABC):

    @abstractmethod
    def verification_login(self,username, password):
        pass
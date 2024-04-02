from domain.entity import Entity

class Person(Entity):
    def __init__(self, personId, personName, personAdress):
        super().__init__(personId)
        self.__personName = personName
        self.__personAdress = personAdress

    def getPersonName(self):
        return self.__personName

    def getPersonAdress(self):
        return self.__personAdress

    def setPersonName(self, personName):
        self.__personName = personName

    def setPersonAdress(self, personAdress):
        self.__personAdress = personAdress

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Numele este: {self.__personName}, Adresa este: {self.__personAdress}"
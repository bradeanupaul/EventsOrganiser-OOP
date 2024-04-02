from domain.entity import Entity


class Eveniment(Entity):
    def __int__(self, evenimentId, evenimentDate, evenimentTime, evenimentDescription):
        super().__init__(evenimentId)
        self.__evenimentDate = evenimentDate
        self.__evenimentTime = evenimentTime
        self.__evenimentDescription = evenimentDescription

    def getEvenimentDate(self):
        return self.__evenimentDate

    def getEvenimentTime(self):
        return self.__evenimentTime

    def getEvenimentDescription(self):
        return self.__evenimentDescription

    def setEvenimentDate(self, evenimentDate):
        self.__evenimentDate = evenimentDate

    def setEvenimentTime(self, evenimentTime):
        self.__evenimentTime = evenimentTime

    def setEvenimentDescription(self, evenimentDescription):
        self.__evenimentDescription = evenimentDescription

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Data este: {self.__evenimentDate}, Timpul este: {self.__evenimentTime}, Descrierea este: {self.__evenimentDescription}"

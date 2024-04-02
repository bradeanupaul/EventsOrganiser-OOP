from domain.entity import Entity


class Assignment(Entity):
    def __init__(self, assignmentId, assignmentPerson, assignmentEveniment):
        super().__init__(assignmentId)
        self.__assignmentPerson = assignmentPerson
        self.__assignmentEveniment = assignmentEveniment

    def getAssignmentPerson(self):
        return self.__assignmentPerson

    def getAssignmentEveniment(self):
        return self.__assignmentEveniment

    def setAssignmentPerson(self, personId):
        self.__assignmentPerson = personId

    def setAssignmentEveniment(self, evenimentId):
        self.__assignmentEveniment = evenimentId

    def __str__(self):
        return f"Id-ul este {self.getEntityId()}, Persoana este: {self.__assignmentPerson}, Evenimentul este: {self.__assignmentEveniment}"
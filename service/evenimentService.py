from repository.genericRepository import Repository
from domain.eveniment import Eveniment


class EvenimentService:
    def __init__(self, evenimentRepository: Repository, assignmentRepository: Repository):
        self.__evenimentRepository = evenimentRepository
        self.__assignmentRepository = assignmentRepository

    def SearchEveniment(self, evenimentId):
        return self.__evenimentRepository.getEntityById(evenimentId)

    def getAllEveniment(self):
        return self.__evenimentRepository.getAllEntities()

    def addEveniment(self, evenimentId, evenimentDate, evenimentTime, evenimentDescription):
        eveniment = Eveniment(evenimentId, evenimentDate, evenimentTime, evenimentDescription)
        self.__evenimentRepository.addEntity(eveniment)

    def modifyEveniment(self, evenimentId, newEvenimentDate, newEvenimentTime, newEvenimentDescription):
        newEveniment = Eveniment(evenimentId, newEvenimentDate, newEvenimentTime, newEvenimentDescription)
        self.__evenimentRepository.modifyEntity(newEveniment)

    def deleteEveniment(self, evenimentId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getAssignmentEveniment() == evenimentId:
                self.__assignmentRepository.deleteEntity(assignment.getAssignmentEveniment())
        self.__evenimentRepository.deleteEntity(evenimentId)
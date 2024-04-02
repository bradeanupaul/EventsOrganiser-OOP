from repository.genericRepository import Repository
from domain.assignment import Assignment
from domain.exceptions.duplicateError import DuplicateError


class AssignmentService:
    def __init__(self, assignmentRepository: Repository, personRepository: Repository, evenimentRepository: Repository):
        self.__assignmentRepository = assignmentRepository
        self.__personRepository = personRepository
        self.__evenimentRepository = evenimentRepository

    def searchAssignment(self, assignmentId):
        return self.__assignmentRepository.getEntityById(assignmentId)

    def getAllAssignments(self):
        return self.__assignmentRepository.getAllEntities()

    def addAssignment(self, assignmentId, assignmentPerson, assignmentEveniment):
        if self.__personRepository.getEntityById(assignmentPerson) is None:
            raise KeyError("Nu exista o persoana cu acest id.")
        if self.__evenimentRepository.getEntityById(assignmentEveniment) is None:
            raise KeyError("Nu exista un eveniment cu acest id.")

        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getAssignmentPerson() == assignmentPerson and assignment.getAssignmentEveniment() == assignmentEveniment:
                raise DuplicateError("Persoana participa deja la acest eveniment.")

        assignment = Assignment(assignmentId, assignmentPerson, assignmentEveniment)
        self.__assignmentRepository.addEntity(assignment)

    def deleteAssignment(self, personId, evenimentId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getAssignmentPerson() == personId and assignment.getAssignmentEveniment() == evenimentId:
                self.__assignmentRepository.deleteEntity(assignment.getEntityId())

from repository.genericRepository import Repository
from domain.person import Person


class PersonService:
    def __init__(self, personRepository: Repository, assignmentRepository: Repository):
        self.__personRepository = personRepository
        self.__assignmentRepository = assignmentRepository

    def searchPerson(self, personId):
        return self.__personRepository.getEntityById(personId)

    def getAllPerson(self):
        return self.__personRepository.getAllEntities()

    def addPerson(self, personId, personName, personAdress):
        person = Person(personId, personName, personAdress)
        self.__personRepository.addEntity(person)

    def modifyPerson(self, personId, newPersonName, newPersonAdress):
        person = Person(personId, newPersonName, newPersonAdress)
        self.__personRepository.modifyEntity(person)

    def deletePerson(self, personId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getAssignmentPerson() == personId:
                self.__assignmentRepository.deleteEntity(assignment.getAssignmentPerson())
        self.__personRepository.deleteEntity(personId)
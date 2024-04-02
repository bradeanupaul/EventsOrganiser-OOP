from repository.genericRepository import Repository
from service.personService import PersonService
from service.evenimentService import EvenimentService
from service.assignmentService import AssignmentService
from ui.console import Console

def main():
    personRepository = Repository()
    evenimentRepository = Repository()
    assignmentRepository = Repository()

    personService = PersonService(personRepository, assignmentRepository)
    evenimentService = EvenimentService(evenimentRepository, assignmentRepository)
    assignmentService = AssignmentService(assignmentRepository, personRepository, evenimentRepository)

    console = Console(personService, evenimentService, assignmentService)
    console.menu()

main()
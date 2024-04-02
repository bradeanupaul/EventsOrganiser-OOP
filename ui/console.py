from domain.exceptions.duplicateError import DuplicateError
from service.personService import PersonService
from service.evenimentService import EvenimentService
from service.assignmentService import AssignmentService


class Console:
    def __init__(self, personService: PersonService, evenimentService: EvenimentService, assignmentService: AssignmentService):
        self.__personService = personService
        self.__evenimentService = evenimentService
        self.__assignmentService = assignmentService

    def addPerson(self):
        try:
            personId = input("Introdu id-ul persoanei: ")
            personName = input("Introdu numele persoanei: ")
            personAdress = input("Introdu adresa persoanei: ")
            self.__personService.addPerson(personId, personName, personAdress)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyPerson(self):
        try:
            personId = input("Introdu id-ul persoanei: ")
            newPersonName = input("Introdu noul nume al persoanei: ")
            newPersonAdress = input("Introdu noua adresa a persoanei: ")
            self.__personService.modifyPerson(personId, newPersonName, newPersonAdress)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deletePerson(self):
        try:
            personId = input("Introdu id-ul persoanei: ")
            self.__personService.deletePerson(personId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showPerson(self):
        try:
            personId = input("Introdu id-ul persoanei: ")
            self.__personService.searchPerson(personId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def getAllPerson(self):
        for person in self.__personService.getAllPerson():
            print(person)

    def addEveniment(self):
        try:
            evenimentId = input("Introdu id-ul evenimentului: ")
            evenimentDate = input("Introdu data evenimentului: ")
            evenimentTime = input("Introdu ora evenimentului: ")
            evenimentDescription = input("Introdu descrierea evenimentului: ")
            self.__evenimentService.addEveniment(evenimentId, evenimentDate, evenimentTime, evenimentDescription)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyEveniment(self):
        try:
            evenimentId = input("Introdu id-ul evenimentului: ")
            newEvenimentDate = input("Introdu noua data a evenimentului: ")
            newEvenimentTime = input("Introdu noua ora e evenimentului: ")
            newEvenimentDescription = input("Introdu noua descriere a evenimentului: ")
            self.__evenimentService.modifyEveniment(evenimentId, newEvenimentDate, newEvenimentTime, newEvenimentDescription)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteEveniment(self):
        try:
            evenimentId = input("Introdu id-ul evenimentului: ")
            self.__evenimentService.deleteEveniment(evenimentId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showEveniment(self):
        try:
            evenimentId = input("Introdu id-ul evenimentului: ")
            self.__evenimentService.SearchEveniment(evenimentId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def getAllEveniment(self):
        print(self.__evenimentService.getAllEveniment())

    def addAssignment(self):
        try:
            assignmentId = input("Introdu id-ul inscrierii: ")
            personId = input("Introdu id-ul persoanei: ")
            evenimentId = input("Introdu id-ul evenimentului: ")
            self.__assignmentService.addAssignment(assignmentId, personId, evenimentId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteAssignment(self):
        try:
            personId = input("Introdu id-ul persoanei: ")
            evenimentId = input("Introdu id-ul evenimentului: ")
            self.__assignmentService.deleteAssignment(personId, evenimentId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAssignment(self):
        try:
            assignmentId = input("Introdu id-ul inscrierii: ")
            self.__assignmentService.searchAssignment(assignmentId)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def getAllAssignment(self):
        print(self.__assignmentService.getAllAssignments())

    def printMenu(self):
        print("1. Adauga persoana.")
        print("2. Modifica persoana.")
        print("3. Sterge persoana.")
        print("4. Cauta persoana.")
        print("p. Afiseaza toate persoanele.")
        print("5. Adauga eveniment.")
        print("6. Modifica eveniment.")
        print("7. Sterge eveniment.")
        print("8. Cauta eveniment.")
        print("e. Afiseaza toate evenimentele.")
        print("9. Inscrie persoana la eveniment.")
        print("10. Sterge inscriere.")
        print("11. Cauta inscriere.")
        print("i. Afiseaza toate inscrierile.")
        print("d. Statistica DTO.")
        print("x. Iesire.")

    def menu(self):
        while True:
            self.printMenu()
            option = input("Scrie optiunea: ")
            if option == "1":
                self.addPerson()
            elif option == "2":
                self.modifyPerson()
            elif option == "3":
                self.deletePerson()
            elif option == "4":
                self.showPerson()
            elif option == "p":
                self.getAllPerson()
            elif option == "5":
                self.addEveniment()
            elif option == "6":
                self.modifyEveniment()
            elif option == "7":
                self.deleteEveniment()
            elif option == "8":
                self.showEveniment()
            elif option == "e":
                self.getAllEveniment()
            elif option == "9":
                self.addAssignment()
            elif option == "10":
                self.deleteAssignment()
            elif option == "11":
                self.showAssignment()
            elif option == "i":
                self.getAllAssignment()
            elif option == "d":
                print("In lucru.")
            elif option == "x":
                break
            else:
                print("Optiune gresita.")
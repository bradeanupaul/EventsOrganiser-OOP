from domain.exceptions.duplicateError import DuplicateError


class Repository:
    def __init__(self):
        self._entities = {}

    def getAllEntities(self):
        return list(self._entities.values())

    def getEntityById(self, entityId):
        if entityId in self._entities:
            return self._entities[entityId]

    def addEntity(self, entity):
        if self.getEntityById(entity.getEntityId()):
            raise DuplicateError("Exista deja o entitate cu acest id.")
        self._entities[entity.getEntityId] = entity

    def modifyEntity(self, newEntity):
        if self.getEntityById(newEntity.getEntityId()) is None:
            raise DuplicateError("Nu exista o entitate cu acest id.")
        self._entities[newEntity.getEntityId()] = newEntity

    def deleteEntity(self, entityId):
        if self.getEntityById(entityId) is None:
            raise DuplicateError("Nu exista o entitate cu acest id.")
        self._entities.pop(entityId)
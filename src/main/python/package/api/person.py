import logging

from package.api.database import Database
from settings import MYSQL_ERRORS


class Person:
    def __init__(self, lastname: str, firstname: str, company_id: int, status: bool = True, id: int = None):
        self.id: int = None or id
        self.lastname: str = lastname.upper()
        self.firstname: str = firstname.capitalize()
        self.company_id: int = company_id
        self.status: bool = True or status
        self.job: str = None
        self.db: Database = Database()

    def __str__(self):
        return f"{self.__class__}\n{self.lastname} {self.firstname} (id: {self.id})\nID Entreprise: {self.company_id}\nActif :{'Oui' if self.status else 'Non'}\n{'-' * 50}"

    def save(self) -> bool:
        try:
            if self.job:
                request = "INSERT INTO people (lastname, firstname, company_id, job) VALUE (%s, %s, %s, %s)"
                params = (self.lastname, self.firstname, 1, self.job)
            else:
                request = "INSERT INTO people (lastname, firstname, company_id) VALUE (%s, %s, %s)"
                params = (self.lastname, self.firstname, self.company_id)
            self.db.insert(operation=request, params=params)
            return True
        except MYSQL_ERRORS as e:
            logging.error(f"{type(e)}: {e}")
            return False


class Staff(Person):
    def __init__(self, lastname: str, firstname: str, job: str, company_id: int = 1, status: bool = True,
                 id: int = None):
        super().__init__(lastname, firstname, company_id, status, id)
        self.job: str = job.title()
        self.db: Database = Database()


def getAllTechnicians() -> list[Staff]:
    technicians = []
    try:
        for elt in Database().select("technicians_vw"):
            technician = Staff(id=elt[0],
                               lastname=elt[1],
                               firstname=elt[2],
                               job=elt[4],
                               status=elt[5]
                               )
            technicians.append(technician)
        return technicians
    except MYSQL_ERRORS as e:
        logging.error(f"{type(e)}: {e}")
        return None

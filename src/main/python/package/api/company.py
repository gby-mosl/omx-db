import logging

from package.api.database import Database
from package.api.person import Person, Staff
from settings import MYSQL_ERRORS


class Company:
    def __init__(self, name: str, address: str, post_code: str, city: str, id: int = None):
        self.id: int = None or id
        self.name: str = name.upper()
        self.address: str = address.title()
        self.post_code: str = post_code
        self.city: str = city.upper()
        self.db: Database = Database()

    def __str__(self):
        return f"{self.name} (id: {self.id})\n{self.address}\n{self.post_code} {self.city}\n{'-' * 50}"

    def save(self) -> bool:
        try:
            request = "INSERT INTO companies (name, address, post_code, city) VALUE (%s, %s, %s, %s)"
            params = (self.name, self.address, self.post_code, self.city)
            self.db.insert(operation=request, params=params)
            return True
        except MYSQL_ERRORS as e:
            logging.error(f"{type(e)}: {e}")
            return False

    @property
    def members(self) -> list[Person | Staff]:
        members = []
        try:
            for elt in self.db.select("people", "company_id", self.id):
                if elt[4]:
                    member = Staff(id=elt[0], lastname=elt[1], firstname=elt[2], job=elt[4], status=elt[5])
                else:
                    member = Person(id=elt[0], lastname=elt[1], firstname=elt[2], company_id=elt[3], status=elt[5])
                members.append(member)
            return members
        except MYSQL_ERRORS as e:
            logging.error(f"{type(e)}: {e}")
            return None

def getAllCompanies() -> list[Company]:
    companies = []
    try:
        for elt in Database().select("companies"):
            company = Company(id=elt[0], name=elt[1], address=elt[2], post_code=elt[3], city=elt[4])
            companies.append(company)
        return companies
    except MYSQL_ERRORS as e:
        logging.error(f"{type(e)}: {e}")
        return None

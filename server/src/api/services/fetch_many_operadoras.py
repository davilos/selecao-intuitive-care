

class FetchManyOperadorasService:
  def __init__(self):
    self.mysql_repository = MySQLOperadorasRepository()

  def execute(self, query: str):
    operadoras = self.mysql_repository.find_many(query)

    return operadoras

from repositories.operadoras_repository import MySQLOperadorasRepository

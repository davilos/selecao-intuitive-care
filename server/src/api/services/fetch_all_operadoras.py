

class FetchAllOperadorasService:
  def __init__(self):
    self.mysql_repository = MySQLOperadorasRepository()

  def execute(self):
    operadoras = self.mysql_repository.find_all()

    return operadoras

from repositories.operadoras_repository import MySQLOperadorasRepository

from .base_repository import BaseRepository

import pymysql


class MySQLOperadorasRepository(BaseRepository):
  def __init__(self):
    self.db_config = pymysql.connect(
      host='localhost',
      user='root',
      password='dev',
      db='intuitive_care_db',
      port=9000
    )
  
  def find_many(self, query: dict["Razao_social": str, "Registro_ANS": str ]):
    connection = self.db_config

    try:
      cursor = connection.cursor()
      query = f"SELECT * FROM operadoras WHERE Registro_ANS = %s OR Razao_Social = %s  LIMIT 50"

      cursor.execute(query, ())

      return cursor.fetchmany()
    except Exception as e:
      print("Erro ao buscar operadoras: ", e)
      return None
    finally:
      cursor.close()
      connection.close()

  def find_all(self):
    connection = self.db_config

    try:
      cursor = connection.cursor()
      query = f"SELECT * FROM operadoras"

      cursor.execute(query)

      return cursor.fetchall()
    except Exception as e:
      print("Erro ao buscar operadoras: ", e)
      return None
    finally:
      cursor.close()
      connection.close()

  
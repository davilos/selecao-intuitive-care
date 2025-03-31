from .base_repository import BaseRepository

import pymysql


class MySQLOperadorasRepository(BaseRepository):
    def __init__(self):
        self.db_config = pymysql.connect(
            host="localhost",
            user="root",
            password="dev",
            db="intuitive_care_db",
            port=9000,
            autocommit=True,
        )

    def find_all(self):
        try:
            with self.db_config.cursor() as cursor:
                query = """
                    SELECT 
                        o.Registro_ANS,
                        o.CNPJ,
                        o.Razao_Social,
                        o.Nome_Fantasia,
                        o.Modalidade,
                        o.Logradouro,
                        o.Numero,
                        o.Complemento,
                        o.Bairro,
                        o.Cidade,
                        o.UF,
                        o.CEP,
                        CONCAT_WS('', '(', o.DDD, ') ', o.Telefone),
                        o.Fax,
                        o.Endereco_eletronico,
                        o.Representante,
                        o.Cargo_Representante,
                        o.Regiao_de_Comercializacao,
                        DATE_FORMAT(o.Data_Registro_ANS, '%d/%m/%Y'),
                        SUM(dc.VL_SALDO_FINAL) as total_vendas
                    FROM operadoras o
                    INNER JOIN demonstracao_contabeis dc 
                        ON o.Registro_ANS = dc.REG_ANS
                    WHERE dc.CD_CONTA_CONTABIL = '41'
                    GROUP BY 
                        o.Registro_ANS, o.CNPJ, o.Razao_Social, o.Nome_Fantasia, o.Modalidade,
                        o.Logradouro, o.Numero, o.Complemento, o.Bairro, o.Cidade, o.UF, o.CEP,
                        o.DDD, o.Telefone, o.Fax, o.Endereco_eletronico, o.Representante,
                        o.Cargo_Representante, o.Regiao_de_Comercializacao, o.Data_Registro_ANS
                    ORDER BY total_vendas DESC
                    LIMIT 10;
                """

                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print("Erro ao buscar operadoras: ", e)
            return None
        finally:
            if self.db_config:
                self.db_config.close()

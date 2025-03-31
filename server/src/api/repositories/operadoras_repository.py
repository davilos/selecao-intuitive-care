from .base_repository import BaseRepository

import pymysql


class MySQLOperadorasRepository(BaseRepository):
    def __init__(self):
        self.db_config = pymysql.connect(
            host="localhost",
            user="root",
            password="dev",
            db="intuitive_care_db",
            port=9000
        )

    def find_all(self):
        try:
            with self.db_config.cursor() as cursor:
                query = """
                    WITH aggregated_sales AS (
                        SELECT 
                            REG_ANS,
                            SUM(VL_SALDO_FINAL) AS total_vendas
                        FROM demonstracao_contabeis
                        WHERE
                        DESCRICAO LIKE '%EVENTOS/%SINISTROS CONHECIDOS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
                        GROUP BY REG_ANS
                    )
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
                        DATE_FORMAT(o.Data_Registro_ANS, '%d/%m/%Y')
                    FROM operadoras o
                    INNER JOIN aggregated_sales agg 
                        ON o.Registro_ANS = agg.REG_ANS
                    ORDER BY agg.total_vendas DESC
                    LIMIT 50;
                """
                                        
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print("Erro ao buscar operadoras: ", e)
            return None
        finally:
            if self.db_config:
                self.db_config.close()

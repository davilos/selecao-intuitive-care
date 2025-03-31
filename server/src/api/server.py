from services.fetch_all_operadoras import FetchAllOperadorasService

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "dev"
app.config["MYSQL_DB"] = "intuitive_care_db"


@app.route("/get-all-operadoras", methods=["GET"])
@cross_origin()
def get_all_operadoras():
    try:
        service = FetchAllOperadorasService()

        raw_operadoras = service.execute()
        operadoras = []

        for op in raw_operadoras:
            operadora = {
                "registro_ans": op[0],
                "cnpj": op[1],
                "razao_social": op[2],
                "nome_fantasia": op[3],
                "modalidade": op[4],
                "endereco": {
                    "logradouro": op[5],
                    "numero": op[6],
                    "complemento": op[7],
                    "bairro": op[8],
                    "cidade": op[9],
                    "uf": op[10],
                    "cep": op[11],
                },
                "contato": {
                   "telefone": op[12],
                    "fax": op[13],
                    "email": op[14],
                },
                "responsavel": {"nome": op[15], "cargo": op[16]},
                "regiao_comercializacao": op[17],
                "data_registro": op[18]
            }
            operadoras.append(operadora)

        response = {
            "error": False,
            "message": "Operadoras carregadas com sucesso",
            "data": operadoras,
        }

        return jsonify(response), 200

    except Exception as e:
        response = {"error": True, "message": str(e), "data": None}
        return jsonify(response), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)

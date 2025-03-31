from services.fetch_many_operadoras import FetchManyOperadorasService
from services.fetch_all_operadoras import FetchAllOperadorasService

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dev'
app.config['MYSQL_DB'] = 'intuitive_care_db'

@app.route("/get-all-operadoras", methods=["GET"])
@cross_origin()
def get_all_operadoras():
  try:
    service = FetchAllOperadorasService()

    operadoras = service.execute()

    response = {
      'error': False,
      'message': 'Operadoras carregadas com sucesso',
      'data': operadoras
    }

    return jsonify(response), 200

  except Exception as e:
    response = {
      'error': True,
      'message': str(e),
      'data': None
    }
    return jsonify(response), 500

@app.route("/get-operadoras", methods=["GET"])
@cross_origin()
def get_operadoras():
  try:
    service = FetchManyOperadorasService()

    operadoras = service.execute("teste")

    response = {
      'error': False,
      'message': 'Operadoras carregadas com sucesso',
      'data': operadoras
    }

    return jsonify(response), 200

  except Exception as e:
    response = {
      'error': True,
      'message': str(e),
      'data': None
    }
    return jsonify(response), 500
  
if __name__ == "__main__":
  app.run(debug=True)
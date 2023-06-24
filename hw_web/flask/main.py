from flask import Flask, request, jsonify
from flask.views import MethodView
from db import Adv, Session
from schema import validate_create_ad
from errors import HttpError

app = Flask('server')


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    http_response = jsonify({'status': 'error', 'description': error.message})
    http_response.status_code = error.status_code
    return http_response


class AdvView(MethodView):

    def post(self):
        request_data = validate_create_ad(request.json)
        with Session() as session:
            new_adv = Adv(**request_data)
            session.add(new_adv)
            session.commit()
            return jsonify(
                {
                    'id': new_adv.id,
                    'creation_time': str(new_adv.creation_time.isoformat()),
                }
            )

    def get(self, adv_id: int):
        if adv_id is None:
            with Session() as session:
                data = session.query(Adv).all()
                adv_list = []
                for item in data:
                    adv = {'id': item.id, 'title': item.title, 'creation_time': str(item.creation_time.isoformat())}
                    adv_list.append(adv)
                return adv_list
        else:
            with Session() as session:
                adv = session.query(Adv).get(adv_id)
                return {'id': adv.id, 'title': adv.title, 'creation_time': str(adv.creation_time.isoformat())}

    def delete(self, adv_id: int):
        with Session() as session:
            session.query(Adv).filter(Adv.id == adv_id).delete()
            session.commit()
            return f'Adv № {adv_id} has beed deleted'


adv_view = AdvView.as_view('adv_id')
app.add_url_rule('/adv', defaults={'adv_id': None}, view_func=adv_view, methods=['GET', ])
app.add_url_rule('/adv', view_func=adv_view, methods=['POST', ])
app.add_url_rule('/adv/<int:adv_id>', view_func=adv_view, methods=['GET', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)

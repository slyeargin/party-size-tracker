from flask import request, jsonify
from models import Party, db

def init_routes(app):
    @app.post('/party')
    def post_party():
        input = request.json
        party_size = input.get("size")

        if party_size is None:
            return jsonify({
                "error": "Bad request."
            }), 400
        else:
            try:
                ## create Party
                party = Party()
                party.size = party_size
                db.session.begin()
                db.session.add(party)
                db.session.commit()
            except:
                db.session.rollback()
                return jsonify({
                    "error": "Server error."
                }), 500
            
            # get Party count
            count = db.session.query(Party).where(Party.size == party_size).count()
            return jsonify({
                "count": count
            }), 201
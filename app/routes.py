from flask import Flask, flash, render_template, request
from models import Party, db

def init_routes(app):
    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            party_size = request.form.get("size")

            if not party_size:
                flash('Party size is required!', 'error')
            else:
                ## create Party
                try:
                    party = Party()
                    party.size = party_size
                    db.session.begin()
                    db.session.add(party)
                    db.session.commit()
                except:
                    db.session.rollback()
                    flash('Server error.', 'error')
                    return render_template('index.html')

                ## get Party count
                count = db.session.query(Party).where(Party.size == party_size).count()
                times = 'time' if count == 1 else 'times'

                flash(f'Parties of a size of {party_size} have been seated {count} {times} today.', 'success')
                return render_template('index.html')

        return render_template('index.html')
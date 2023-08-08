from flask import flash, render_template, request

import requests
import json

def init_routes(app):
    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            party_size = request.form.get("size")

            if not party_size:
                flash('Party size is required!', 'error')
            else:
                ## send request
                url = 'http://api:81/party'
                data = {'size': party_size}
                headers = {'Content-Type': 'application/json'}

                r = requests.post(url, data=json.dumps(data), headers=headers)

                if r.status_code == 201:
                    ## parse response
                    res = r.json()
                    count = res.get("count")
                    if not count:
                        flash(f'Server error.')
                        return render_template('index.html')

                    times = 'time' if count == 1 else 'times'

                    flash(f'Parties of a size of {party_size} have been seated {count} {times} today.', 'success')
                    return render_template('index.html')
                else:
                    flash(f'Server error.  Status code: {r.status_code}')
                    return render_template('index.html')

        return render_template('index.html')
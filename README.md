# Party Size Tracker

Party Size Tracker is a simple Flask app.  It uses Flask-SQLAlchemy and psycopg2-binary to connect to a PostgreSQL database. Both the application and the database are running in Docker containers.

I used [this Flask/Docker/Postgres starter](https://github.com/slyeargin/flask-docker-postgres-starter) as a starting point.

## Local development instructions

Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is running locally.

Clone this repository, and from its root directory run `make run`.

If you see `Party Size Tracker` and a simple form when you visit [localhost](http://localhost), everything is running as expected.
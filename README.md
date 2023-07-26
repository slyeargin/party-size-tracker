# Flask Docker Postgres Starter

This is a simple Flask REST API starter using Flask-SQLAlchemy and psycopg2-binary to connect to a PostgreSQL database.  Both the application and the database are running in Docker containers.

## Local development instructions

Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is running locally.

Clone this repository, and from its root directory run `make run`.

If you see `Hello World` when you visit [localhost](http://localhost), everything is running as expected.
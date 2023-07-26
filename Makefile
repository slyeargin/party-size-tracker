.PHONY: build run

run: build

build:
	docker compose build
	docker compose up -d

# migrate:
#	sleep 5 && cat backup/*.sql | docker exec -i db psql -U postgres -d postgres

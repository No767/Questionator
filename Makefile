all: run

run:
	poetry run python Bot/main.py

start-compose-dev:
	sudo docker compose -f docker-compose-dev.yml up -d

stop-compose-dev:
	sudo docker compose -f docker-compose-dev.yml stop
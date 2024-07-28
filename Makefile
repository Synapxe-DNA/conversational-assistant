.PHONY: lint

lint:
	pre-commit run --all-files

all: lint

backend-start:
	@docker-compose -f ./backend/docker-compose.yml up -d

backend-run:
	@docker-compose -f ./backend/docker-compose.yml up

backend-stop:
	@docker-compose -f ./backend/docker-compose.yml down

.PHONY: lint

lint:
	pre-commit run --all-files

all: lint

backend-build:
	@docker-compose -f ./backend/docker-compose.yml build

backend-run:
	@docker-compose -f ./backend/docker-compose.yml up

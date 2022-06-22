
check:
	docker-compose ps
clear:
	docker system prune -a --volumes
dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
down:
	docker-compose down
prod:
	docker-compose up -d --scale worker=5 --no-recreate

add:
	curl -v http://localhost:11521/add/$(P1)/$(P2)
result:
	curl -v http://localhost:11521/check/$(CHECK)
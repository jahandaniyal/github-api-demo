.PHONY: build test run stop clean

build: stop
	docker-compose build --no-cache

clean:
	rm -rf .env

run:
	docker-compose up

test:
	docker-compose up test

stop:
	docker-compose kill flask-app grafana-service prometheus-service
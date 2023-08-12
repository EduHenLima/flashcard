## Docker
* docker run -d -p 3306:3306 --name mysql-docker-container -e MYSQL_ROOT_PASSWORD=flashcards -e MYSQL_DATABASE=flashcards -e MYSQL_USER=edu -e MYSQL_PASSWORD=flashcards mysql/mysql-server:latest
* Start Specif docker container by id: Docker start [id]
* List all dockers: docker ps -a
* Stop all containers: docker stop $(docker ps -a -q)

Commands:
* pip install mysql-connector-python
* pip install sqlalchemy
* pip install pandas

Invoke:
* Run local: serverless offline start --stage local
* Ping: serverless invoke local --function ping
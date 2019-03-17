# Flask REST API Boilerplate

Boilerplate to speed up building HTTP Rest API using Flask

## Getting Started

### Prerequisites

```
docker & docker-compose
```

### Installing

To run the flask on your local machine, you need to install docker
```
create .env in root directory and set this
# ROOT MONGO SETTING
DB_ROOT_USERNAME=< MongoDB Root Username >
DB_ROOT_PASSWORD=< MongoDB Root Password>
# database user setting
DB_USERNAME=< MongoDB User username>
DB_PASSWORD=<MongoDB User password>
DB_HOSTNAME=mongo
DB_NAME=<MongoDB Database that going to be created>
DB_PORT=27017
# flask
ENVIRONMENT=<environment to run >
HOST=0.0.0.0
```

```
./start.sh
```
it will rebuild docker images and automatically run it

```
try access 127.0.0.1:5000 :)
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Simple Deployment using Docker!

## Built With

* [Flask](http://flask.pocoo.org) - The Python Web framework
* [Mongo](https://www.mongodb.com) - NoSQL Database
* [Docker](https://www.docker.com) - Containerization Technology

## Contributing

Please read [CONTRIBUTING.md]for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Kelvin Desman** - *Initial work* - [vousmeevoyez](https://github.com/vousmeevoyez)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

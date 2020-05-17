# Flask REST API Clean Architecture Practice
A Clean Architecture Practice with Flask REST API.

This is a practice project I used to learn Clean Architecture by implementing the REST API with a full Authentication/Authorization Protocols, Dependency Injection and furthermore the Swagger documentation.

## Basic Folder Structure

> application.py

The major application declaration file.

> apps

The Application Layer that defines API controller endpoint, global exceptions and also Request/Response/Presenter/Validator adapters.

> config

Application Configuration files are here.

> core

The core concept of the Clean Architecture practice. The `kernel` part is about the interface and abstract class definitions. The `core` part contains the business logic and the domains objects such as **entity**, **value object**, **use case** and also the **repository**.

> extensions

Some configuration and plugins I used, to make the application itself cleaner.

> infra

The Infrastructure Layer that provides the actual implementation of network, persistent, cache layer... etc.

> tests

Test folder, not implemented yet.

## Dependencies
* `flask`: Base Web Framework
* `werkzeug`: Utility Library under Flask
* `authlib`: OpenID Connect Provider Library
* `flask-restplus` = REST API, Swagger Library
* `flask-injector` = Dependency Injection
* `attrs` = Data Classes Utility LIbrary
* `cattrs` = Serialization / Deserialization

## Run the project
```
> pipenv sync
```

Enter Shell
```
> pipenv shell
```

Start App
```
> flask run
```

Sample API request

- http://localhost:5000/profile/v1/member/111/


API Documentation

- http://localhost:5000/account/v1/doc/

- http://localhost:5000/profile/v1/doc/


## TODO Items for POC
- [x] Apply Clean Architecture
- [x] Layer Abstraction
- [x] Dependency Injection
- [x] UseCase Implementation
- [x] Serialization / Deserialization
- [x] Mock Repo Implementation
- [x] Handle Exceptions
- [x] Response Marshalling
- [x] Review usecase.execute() with Req/Resp
- [x] Review API Documentation
- [ ] Implement Full Story with Entity, ValueObject
- [ ] Request Validation with Marshmallow
- [ ] Deal with Date/DateTime
- [ ] Database with SQLAlchemy
- [ ] Logging
- [ ] OAuth2 with Authlib Implementation
- [ ] Authentication to Resource API
- [ ] Dev/Prod Configuration
- [ ] Apply Tests
- [ ] WSGI Settings

## Reference

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)
- [Injector](https://github.com/alecthomas/injector)
- [Flask Injector](https://github.com/alecthomas/flask_injector)
- [attrs](https://www.attrs.org/en/stable/)
- [cattrs](https://github.com/Tinche/cattrs)
- [Authlib](https://docs.authlib.org/en/latest/)
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

# https://testdriven.io/blog/fastapi-mongo/

## Install

### MongoDB

You can get the community edition via brew, [instructions here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)

Xcode cmd line tools are a pre-requisite.

```
brew tap mongodb/brew

brew update

brew install mongodb-community@7.0
```

### Dependencies

```
poetry init

poetry install

poetry shell
```

## Start/stop mongo via terminal

Set to auto-start in your bash/zsh profile if you want, or just do manually when running the project;

```
brew services start mongodb-community@7.0

brew services stop mongodb-community@7.0
```

## In a different terminal

```
mongosh

Current Mongosh Log ID:	664260a1b9a9fde7b53f3d38
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.5
Using MongoDB:		7.0.8
Using Mongosh:		2.2.5

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------
   The server generated these startup warnings when booting
   2024-05-13T19:39:46.570+01:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
------

test> exit()

~ 14s
```

## Start up the API

```
python app/main.py
```

## Local site on port 8000

Swagger docs for testing out the API: [http://localhost:8000/docs](http://localhost:8000/docs)

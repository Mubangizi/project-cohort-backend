# Matatu Project Cohort Api
With simple CRUD implementations

### Project Setup

Follow these steps to have a local running copy of the app.

##### Clone The Repo

`git clone https://github.com/Mubangizi/project-cohort-backend.git`

If `master` is not up to date, `git checkout develop`. However, note that code on develop could be having some minor issues to sort.

##### Install PostgreSQL

Here's a great resource to check out:

[How To Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Create a development database and call it `cohort_db`.

##### Create a Virtual Environment

create virtual enviroment called venv

Run `virtualenv venv`

Activate the virtual environment.

Run `. venv/bin/activate`

App was developed with `Python 3.6`.

Make sure you have `pip` installed on your machine.

Install the dependencies.

`pip install -r requirements.txt`

Create a `.env` file (which defines the environment variables used) at the root of the app.

Add the following details, customizing as needed.

```
export FLASK_APP=server.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
```

Run the application.

`flask run`

##### To checkout Api Documentation

Through your browser go to link `localhost:<flask_port>/apidocs`.


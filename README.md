<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i1.wp.com/lendigo.ng/wp-content/uploads/2019/12/Lendigo-Logo-2.png?w=1200" alt="Bot logo"></a>
</p>

<h3 align="center">Lendigo Task</h3>

---

<p align="center"> Hacker News DIY Consuming API
    <br> 
</p>

## Table of Contents

- [About](#about)
- [How it works](#working)
- [Getting Started](#getting_started)
- [Deploying API](#deployment)
- [Built Using](#built_using)
- [API URL](#api-side)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>

An API built to get news from HackerNews API. It also lets you post to the API too.

## How it works <a name = "working"></a>

This project sweeps the Hacker News API every 5 minutes and gets 100 for the latest news and stores them in a database. However, on a blank database, it pulls all of it.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

It would help if you had Python and Redis installed on your machine to get this program running. We'll start by creating a virtual environment.

```
python3 -m venv venv
```

Activate the virtual environment

```
. venv/bin/activate
```

Clone the repo on your machine

```
git clone https://github.com/iMiebaka/lendigo_task.git
cd lendigo_task
```
#### Initilize/ Migrate Database

To Initate Database, run the command below:
```
python3 create_db.py
```
You might experience some errors if the database (SQLite) already exit.

</br>
To migrate database run the command below

```
python3 migration.py
```

### Installing

Now the code is pulled, let's install the packages in the requirements.txt

```
pip install -r requirements.txt
```

#### Executing The project

To run this project to live, You need three command windows to execute this project

- One for the flask app
- Another to start Celery
- The last window runs the API call every 5 minutes

#### Run flask app

```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w run:app
```

NB: The above uses uwsgi to run the flask app, but if it does try the development command

```
python3 run.py
```

#### Start Celery Worker

```
celery -A core.task.celery worker --loglevel=INFO

```

#### Start Celery Beat

```
celery -A core.task.celery worker --loglevel=INFO
```

## API Urls <a name = "api-side"></a>

<p> API_ENDPOINT:   The API_ENDPOINT is as followed:
<br>
['/api/v1/get-comments', '/api/v1/add-comment', '/api/v1/delete-post', '/api/v1/get-posts', '/api/v1/delete-post', '/api/v1/add-post', '/api/v1/', '/']
</p>

```
http://localhost:5000/api/v1
```

### Get Post - GET
```
http://localhost:5000/api/v1/get-post

```

Using Search Query
```
http://localhost:5000/api/v1/get-post?page=1?search=helloworld

```

Using Pagination Query

```
http://localhost:5000/api/v1/get-post?page=1?search=helloworld&page=1
```


### To Add Post - POST

```
http://localhost:5000/api/v1/add-post
```

Body Example

```
{
  "by": "test_data",
  "descendants": 0,
  "title": "test_data",
  "url": "test_data",
  "text": "test_data"
  }
```

### Delete Post - DELETE
```
http://localhost:5000/api/v1/get-post?page=1?delete=11111

```
NB: You can only delete a custom-made post.


## Deploying API <a name = "deployment"></a>

This project is currently using SQLite, changing the dev_flag (in core/**init**.py) to deployment will require some configuration.

If you want to switch to production, do not forget to create the MySQL data

- username: root
- password: MYSQL_ROOT_PASSWORD # Change as configured by MySQL Database
- database_name: hackernewstask
  <br>

Also, if you're using Redis as a service, it has to reflect in the config.


## Built Using <a name = "built_using"></a>

- [Flask Web Server](https://flask-login.readthedocs.io/en/latest/) - Python

## Authors <a name = "authors"></a>

- [@imiebaka](https://github.com/imiebaka) - Idea & Initial work

## Acknowledgements <a name = "acknowledgement"></a>

- God, the giver of all good gift
- Lendigo for the learning Experience
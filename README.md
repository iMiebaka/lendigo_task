<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i1.wp.com/lendigo.ng/wp-content/uploads/2019/12/Lendigo-Logo-2.png?w=1200" alt="Bot logo"></a>
</p>

<h3 align="center">Lendigo Task</h3>


---

<p align="center"> Hacker News DIY Consuming API
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Deploying your own bot](#deployment)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
An API built to get news from HackerNews api

## 💭 How it works <a name = "working"></a>

This project sweeps the Hacker News API every 5 minutes for the latest news and store them in a database
<p> API_ENDPOINT:   
<br>
'/api/v1/get-comments', '/api/v1/add-comment', '/api/v1/delete-post', '/api/v1/get-posts', '/api/v1/add-post', '/api/v1/', '/']
</p>

The API_ENDPOINT is as followed:

```
http://localhost:5000/api/v1
```


## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites
You need Python and Redis installed on your machine to get this program running. Let's create create a virtual enviroment.

```
python3 -m venv venv
```

Activate the virtual enviroment
```
. venv/bin/activate
```

Clone the repo on your machine
```
git clone xxx
cd xxx
```

### Installing

Now the code is pulled, lets install the packages in the requirements.txt

```
pip install -r requirements.txt
```


### Executing The project

Now lets bring this project to live, You need three command window to execute this project
- One for the flask app
- Another to start Celery
- Last window for Run the API call every 5 minutes

#### Run flask app
```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w run:app
```
NB: The above uses uwsgi to run the flast app, but if it does try the development command
```
python3 run.py
```

#### Start Radis
```
celery -A core.task.celery worker --loglevel=INFO

```
#### Start Radis
```
celery -A core.task.celery worker --loglevel=INFO
```


## 🚀 Deploying your own bot <a name = "deployment"></a>

This project is currently using sqlite, however changing the dev_flag (in core/__init__.py) to deployment, some configutation should be consider.


If you want to switch to production, do not forget to create the mysql data
  - username: root
  - password: MYSQL_ROOT_PASSWORD  # Change as configured by MySQL Database
  - database_name: hackernewstask

## ⛏️ Built Using <a name = "built_using"></a>

- [PRAW](https://praw.readthedocs.io/en/latest/) - Python - Flask
- [Heroku](https://www.heroku.com/) - SaaS hosting platform

## ✍️ Authors <a name = "authors"></a>

- [@imiebaka](https://github.com/imiebaka) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- God, the giver of all good gift
- Lendigo for the leaning Experience

. venv/bin/activate && python create_db.py  &&  export FLASK_APP=run.py && flask db init &&  flask db migrate && flask db upgrade
setup:
	python3 -m venv ~/.DSBA-6190_Proj2

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	hadolint Dockerfile 
	pylint --disable=R,C main.py
	pylint --disable=R,C python_scripts/model.py

run:
	python3 main.py
all: 
	install lint test
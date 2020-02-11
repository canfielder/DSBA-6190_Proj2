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
	pylint --disable=R,C,W1202 main.py
	pylint --disable=R,C python_scripts/**.py
	pylint --disable=R,C,W0104,E0602 wine_predict/**.ipynb


run:
	python3 main.py
all: 
	install lint test
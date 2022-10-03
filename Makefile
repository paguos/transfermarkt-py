dev-env:
	pipenv install --dev

lint:
	pipenv run flake8

unit:
	pipenv run pytest --cov

tests: lint unit

install: # poetry install
	poetry install

build: # project building
	poetry build

publish: # project publication
	poetry publish --dry-run

package-install: # project install
	python3 -m pip install --user dist/*whl

package-reinstall: #reinstall project
	python3 -m pip install --user --force-reinstall dist/*whl

linter:
	poetry run flake8 gendiff

tests:
	poetry run pytest -vv

make test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

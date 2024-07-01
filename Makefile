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

lint:
	poetry run flake8 gendiff

init:
	poetry install

update:
	poetry update

test:
	poetry run pytest

watch_test:
	poetry run ptw

build:
	poetry build

publish_test:
	poetry config repositories.testpypi https://test.pypi.org/legacy/ && poetry publish -r testpypi

publish:
	poetry publish
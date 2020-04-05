init:
	poetry install

test:
	poetry run pytest

watch_test:
	poetry run ptw
install: # построить дерево зависимостей проекта, и установить все пакеты.
	poetry install

brain-games: # запуск программы.
	poetry run brain-games

build: # собирает пакет
	poetry build

publish: # отладка публикации, без добавления пакета в PyPI
	poetry publish --dry-run

package-install: # установка пакета из операционной системы
	python3 -m pip install --user dist/*.whl

lint: # запускает линтер
	poetry run flake8 brain_games
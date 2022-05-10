install: # построить дерево зависимостей проекта, и установить все пакеты.
	poetry install

brain-games: # запуск программы.
	poetry run brain-games

brain-even: # запуск игры "Проверка на четность".
	poetry run brain-even

brain-calc: # запуск игры "Калькулятор".
	poetry run brain-calc

brain-gcd: # запуск игры "НОД".
	poetry run brain-gcd

brain-progression: # запуск игры "Арифметическая прогрессия".
	poetry run brain-progression

brain-prime: # запуск игры "Простое ли число?".
	poetry run brain-prime

build: # собирает пакет
	poetry build

publish: # отладка публикации, без добавления пакета в PyPI
	poetry publish --dry-run

package-install: # установка пакета из операционной системы
	python3 -m pip install --user dist/*.whl

lint: # запускает линтер
	poetry run flake8 brain_games
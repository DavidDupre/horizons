init:
	pip install -r requirements.txt

run:
	python -m horizons

publish:
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*

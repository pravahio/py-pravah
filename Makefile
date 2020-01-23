package:
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*

clean:
	rm -rf build/
	rm -rf dist/
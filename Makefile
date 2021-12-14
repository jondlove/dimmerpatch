build:
	python3 -m build

clean:
	rm dist/*

upload:
	python3 -m twine upload --repository testpypi dist/*

release:
	python3 -m twine upload dist/*
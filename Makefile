
build:
	python3 -m build

clean:
	rm dist/*

upload:
	python3 -m twine upload --repository testpypi dist/*

local-install:
	LOCALBUILD="$(shell ls dist/dimmerpatch-*.tar.gz)"; python3 -m pip install $$LOCALBUILD

test-install:
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps dimmerpatch

test-upgrade:
	python3 -m pip install --upgrade --index-url https://test.pypi.org/simple/ --no-deps dimmerpatch

release:
	python3 -m twine upload dist/*
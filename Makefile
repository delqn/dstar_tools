.DEFAULT_GOAL := all

.PHONY: all
all: install-prepush lint

.PHONY: lint
lint: clean test
	pep8 dstartools/ ./*.py --exclude=mocks.py
	pylint --rcfile=.pylintrc dstartools/ ./*.py

.PHONY: install-prepush
install-prepush:
	@-if [ -d .git ] && [ ! -h .git/hooks/pre-push ] ; then \
		ln -s ../../prepush .git/hooks/pre-push; \
	fi

.PHONY: clean
clean:
	find . -name \*.pyc -delete

.PHONY: test
test:
	nosetests $(find . -name "_test.py")

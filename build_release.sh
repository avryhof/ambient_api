#!/bin/bash
python3 setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel
# Test PyPi
#twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# Prod PyPi
twine upload dist/*
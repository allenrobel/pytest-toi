#!/bin/bash
#
# To install the coverage tool:
#  pip install coverage
#
# Modify below to point to the location of your ansible_collection and testcases.
# ANSIBLE_CODE: Path to the ansible collection you want to test
# PYTEST_TESTCASES: Path to the testcases you want to run within the ansible collection
# COVERAGE_DIR: Path to the directory where you want to store the coverage report
#
# Run this script to generate the coverage report for the ansible collection.
# The coverage report will be stored in the COVERAGE_DIR directory.
# Open the index.html file in the COVERAGE_DIR directory with a web browser to view the coverage report.
# For example, with the COVERAGE_DIR defined below, we'd open:
# On Linux:
#  file:///tmp/coverage/index.html
# On MacOS:
#  file:///private/tmp/coverage/index.html

export ANSIBLE_CODE=$HOME/repos/toi/pytest-toi
export CODE=$ANSIBLE_CODE/modules
export TESTS=$ANSIBLE_CODE/tests
export COVERAGE_DIR=/tmp/pytest-toi

rm -rf $COVERAGE_DIR
coverage run \
  --source=$CODE \
  -m pytest $TESTS
coverage html -d $COVERAGE_DIR

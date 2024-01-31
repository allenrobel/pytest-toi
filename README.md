## Example pytest testcases and some code to test.

To use:

1. Install pytest if not already installed.

```bash
pip install pytest
```

2. Clone the repo.

```bash
git clone https://github.com/allenrobel/pytest-toi.git
```

2. cd into the local clone.

```bash
cd pytest-toi
```

3. Run the testcases

```bash
pytest
```

4. To run a specific test case:

```bash
pytest -k test_monkeypatch_baz
```

## Coverage report

1. Have a look in the coverage.bash script for details on how to use it to generate a coverage report for the example code in this repo.

2. Run coverage.bash (modify as needed depending on your local repo path)

From the report, you should see that:

1. The following have complete coverage:

modules/baz.py
modules/square.py

2. The following are missing coverage for the mocked function send_request(), as expected:

modules/foo.py
modules/bar.py

## coverage report tip

Sometimes it's useful to see what the coverage is for a single test case, or set of test cases.

This can answer the question "Is this testcase really doing anything?"

Below we run the test case in tests/test_parametrize_1.py

```bash
rm -rf /tmp/pytest-toi
coverage run --source=./modules -m pytest tests/test_parametrize_1.py
coverage report --show-missing | grep '^Name\|square'
# output removed....
Name                  Stmts   Miss  Cover   Missing
modules/square.py         5      2    60%   3
```

The coverage report shows that ``raise`` in modules/square.py (line 3) is not covered, as expected.

If we rerun coverage for tests/test_parametrize_2.py, we see the ``raise`` is covered.

The text report below is actually not correct (Miss should be 0 and Cover 100%).

Looking at the html report shows that all lines ARE covered.  Looks like a bug with coverage tool ``:-(``

```bash
rm -rf /tmp/pytest-toi
coverage run --source=./modules -m pytest tests/test_parametrize_2.py
coverage report --show-missing | grep '^Name\|square'
# output removed....
Name                  Stmts   Miss  Cover   Missing
modules/square.py         5      1    80%
```

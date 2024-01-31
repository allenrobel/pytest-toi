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

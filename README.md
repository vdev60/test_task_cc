# test_task_cc

1. Setting virtual environment

```console
$ virtualenv .venv
$ source .venv/bin/activate
```
2. Install requirements 

```console
$ pip install -r requirements.txt
```

3. To run flake8 linter use next command

```console
$ flake8 --config .flake8
```
You can run black package for code formatter

```console
$ black {source_file_or_directory}
```
Heroku app - https://test-task-cc.herokuapp.com/
Graphql - https://test-task-cc.herokuapp.com/graphql

4. To run unit testing use next command

```console
$ pytest tests
```

For unit testing used:

pytest -  https://docs.pytest.org/en/6.2.x/
snapshottest - https://github.com/syrusakbary/snapshottest
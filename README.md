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
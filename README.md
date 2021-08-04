# Running the application

```bash
$ pipenv shell
$ make build
$ spark-submit --master local spark-python/main.py
$ cd dist && spark-submit --master local --py-files src.zip main.py && cd
```

## See all run options

```bash
$ spark-submit
````

## Setting up the virtual environment in the same directory as the Pipfile

By default the virtual env is created in a folder in '/Users/YourName/.local/share/virtualenvs/'

If you want it to be set in the same directory as the Pipfile, set the `PIPENV_VENV_IN_PROJECT` environment variable to any value (ex: 1):
`PIPENV_VENV_IN_PROJECT=1 pipenv shell`

If you want to reset this:
`unset PIPENV_VENV_IN_PROJECT`

Check if environment variable is set:
`printenv PIPENV_VENV_IN_PROJECT`

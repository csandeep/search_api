### Setup

```shell
pip install pipenv --user
pipenv install
```

### Initialize

```shell
cp .env_sample .env
```

Edit the `.env` file and add your api key.

### Run

```shell
pipenv run pytest
pipenv run fastpai dev
```

### Documentation

Once you `pipenv run fastapi dev` you can browse the api documentation at `http://127.0.0.1:8000/docs#/`

# FlexUSD AvgAPY Bot

This bot will, in response to an /apy command, post the average annual percentage yield of CoinFlex's FlexUSD token.

## Commands

/apy or /apy@botusername - returns the average annual percentage yield of CoinFlex's FlexUSD token

## Setup

This project uses Poetry to manage dependencies.

```
poetry shell
poetry install
cp .env.example .env
```

Then, replace the values in the .env file with your own & run

```
poetry run python src/flexbot.py
```

## Contributing

This project uses pre-commit hooks and commitizen to manage commits.
After staging your changes, run

```
poetry run pre-commit run
```

stage changes made by pre-commit hooks &

```
poetry run git cz c
```

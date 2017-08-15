# Python Cookiecutter CLI with Pipfile and pipenv

[![Build Status](https://travis-ci.org/menzenski/cookiecutter-python-cli.svg?branch=develop)](https://travis-ci.org/menzenski/cookiecutter-python-cli) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/menzenski/cookiecutter-python-cli/issues) [![license](https://img.shields.io/github/license/menzenski/cookiecutter-python-cli.svg?style=flat)](https://github.com/menzenski/cookiecutter-python-cli/blob/develop/LICENSE.md)

## What is this?

A default template for a new CLI project, written in Python, to be used
with the [cookiecutter](https://cookiecutter.readthedocs.io) utility.
Deals with all the boilerplate involved in the setuptools setup, etc.

## How to answer these questions?

When running Cookiecutter, you'll need to provide some values.
Here's what they're for:

* `project_name` -- "My Tool"   (Used for marketing.  Keep it short and capitalize accordingly.)
* `repo_name` -- "python-mytool"  (Name of the GitHub repo.)
* `pypi_name` -- "mytool"   (Name on PyPI, i.e. what people type to `pipsi install`.)
* `script_name` -- "my-tool"  (Binary of the script, i.e. what people will run on the command line.)
* `package_name` -- "my_tool"  (Name of the Python module/package used internally.)

## License

Liberally licensed under BSD terms.

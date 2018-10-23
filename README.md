# pytest-dotenv

This little plugin uses `python-dotenv` to load any environment variables
defined in any `pytest` config files, such as `pytest.ini`, `tox.ini` and so on.

## Installation

Install the plugin with `pip`:

```
$ pip install pytest-dotenv
```

## Usage

Add a new section to a config file named `env_vars`.
You can list as many files as necessary:

```
[pytest]
env_files =
    .env
    .test.env
    .deploy.env
```

The files will be loaded and added to the `os.environ` dict object before
any tests are run. If the files are not found on the working directory, it will search for the files in the ancestor directory and upwards. 

By default the plugin will not overwrite any variables already defined in the
process' environment. If you want that behavior, you have to use the
`env_override_existing_values` setting:

```
[pytest]
env_override_existing_values = 1
env_files =
    .env
    .test.env
    .deploy.env
```

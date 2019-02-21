# pytest-dotenv

This little plugin uses `python-dotenv` to load any environment variables from a `.env` file. Extra configuration can be defined in any `pytest` config files, such as `pytest.ini`, `tox.ini` and so on.

## Installation

Install the plugin with `pip`:

```
$ pip install pytest-dotenv
```

## Basic Usage

If all you want is to load environment variables from a `.env` file then installing the plugin is all that is needed. `python-dotenv` will automatically detect your `.env` file and load it. By default, the plugin won't override any existing system variables.


## Non-default configuration

### Custom Environment Variable Files

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

### Overriding Existing Values

By default the plugin will not override any variables already defined in the
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

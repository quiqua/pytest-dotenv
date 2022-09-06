# -*- coding: utf-8 -*-
import os
import sys

from dotenv import load_dotenv, find_dotenv

import pytest


def pytest_addoption(parser):
    parser.addini("env_files",
                  type="linelist",
                  help="a line separated list of env files to parse",
                  default=['.env'])
    parser.addini("env_override_existing_values",
                  type="bool",
                  help="override the existing environment variables",
                  default=False)
    parser.addoption("--envfile",
                    dest="envfile",
                    default="foo",
                    type=str,
                    help="Overwrite any environment variable specified in this file. This argument ignores the .ini settings.")


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    _override = early_config.getini("env_override_existing_values")
    for filename in early_config.getini("env_files"):
        _check_exists(filename)
        load_dotenv(find_dotenv(filename, usecwd=True), override=_override)


def pytest_sessionstart(session):
    config = session.config
    env_file = config.getoption("envfile", default=None)
    if env_file is not None:
        _check_exists(env_file)
        load_dotenv(dotenv_path=env_file, override=True)


def _check_exists(filename):
    if not os.path.exists(filename):
        sys.stderr.write("Env file not found: %s\n" % filename)

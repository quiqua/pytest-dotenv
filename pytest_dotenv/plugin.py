# -*- coding: utf-8 -*-

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
        load_dotenv(find_dotenv(filename, usecwd=True), override=_override)


def pytest_sessionstart(session):
    config = session.config
    if config.getoption("envfile", default=None) is not None:
        load_dotenv(dotenv_path=config.getoption("envfile"), override=True)

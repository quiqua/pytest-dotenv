# -*- coding: utf-8 -*-

from dotenv import load_dotenv

import pytest


def pytest_addoption(parser):
    parser.addini("env_files",
                  type="linelist",
                  help="a line separated list of env files to parse",
                  default=[])
    parser.addini("env_override_existing_values",
                  type="bool",
                  help="override the existing environment variables",
                  default=False)


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    for file in early_config.getini("env_files"):
        load_dotenv(
            file, override=early_config.getini("env_override_existing_values")
        )

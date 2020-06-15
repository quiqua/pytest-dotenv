# -*- coding: utf-8 -*-
from unittest import mock

import pytest


@pytest.fixture
def mock_os_environ():
    with mock.patch.dict("os.environ", clear=True) as m:
        yield m


@pytest.mark.usefixtures("mock_os_environ")
def test_ini_file(testdir):
    testdir.makeini("""
        [pytest]
        env_files =
            myenv.txt
    """)

    testdir.maketxtfile(myenv="FOO=BAR\nSPAM=EGGS")

    # create a temporary pytest test module
    testdir.makepyfile("""
        import os

        def test_env_foo():
            assert os.environ.get('FOO') == 'BAR'

        def test_env_spam():
            assert os.environ.get('SPAM') == 'EGGS'
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_env_foo PASSED*',
        '*::test_env_spam PASSED*'
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


@pytest.mark.usefixtures("mock_os_environ")
def test_ini_file_refuse_overwrite(testdir):
    testdir.makeini("""
        [pytest]
        env_override_existing_values = 0
        env_files =
            myenv.txt
            overwrite.txt
    """)

    testdir.maketxtfile(myenv="FOO=BAR\nSPAM=EGGS")
    testdir.maketxtfile(overwrite="FOO=EGGS\nSPAM=BAR")
    # create a temporary pytest test module
    testdir.makepyfile("""
        import os

        def test_env_foo():
            assert os.environ.get('FOO') == 'BAR'

        def test_env_spam():
            assert os.environ.get('SPAM') == 'EGGS'
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_env_foo PASSED*',
        '*::test_env_spam PASSED*'
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


@pytest.mark.usefixtures("mock_os_environ")
def test_ini_file_allow_overwrite(testdir):
    testdir.makeini("""
        [pytest]
        env_override_existing_values = 1
        env_files =
            myenv.txt
            overwrite.txt
    """)

    testdir.maketxtfile(myenv="FOO=BAR\nSPAM=EGGS")
    testdir.maketxtfile(overwrite="FOO=EGGS\nSPAM=BAR")
    # create a temporary pytest test module
    testdir.makepyfile("""
        import os

        def test_env_foo():
            assert os.environ.get('FOO') == 'EGGS'

        def test_env_spam():
            assert os.environ.get('SPAM') == 'BAR'
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_env_foo PASSED*',
        '*::test_env_spam PASSED*'
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


@pytest.mark.usefixtures("mock_os_environ")
def test_file_argument_force_overwrite(testdir):
    testdir.makeini("""
        [pytest]
        env_files =
            myenv.txt
    """)

    testdir.maketxtfile(myenv="FOO=BAR\nSPAM=EGGS")
    tmp_env_file = testdir.maketxtfile(tmpenv="FOO=BAZ\nBAR=SPAM")
    # create a temporary pytest test module
    testdir.makepyfile("""
        import os

        def test_env_foo():
            assert os.environ.get('FOO') == 'BAZ'

        def test_env_spam():
            assert os.environ.get('SPAM') == 'EGGS'

        def test_env_bar():
            assert os.environ.get('BAR') == 'SPAM'
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest("-v", "--envfile", str(tmp_env_file))

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_env_foo PASSED*',
        '*::test_env_spam PASSED*',
        '*::test_env_bar PASSED*'
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0

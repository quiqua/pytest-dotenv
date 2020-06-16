from setuptools import setup
from os import path

description = 'A py.test plugin that parses environment files before running tests'

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytest-dotenv',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.5.2',
    author='Marcel Radischat',
    author_email='marcel@quiqua.eu',
    url='https://github.com/quiqua/pytest-dotenv',
    download_url='https://github.com/quiqua/pytest-dotenv/tarball/0.5.2',
    packages=['pytest_dotenv'],
    entry_points={'pytest11': ['dotenv = pytest_dotenv.plugin']},
    install_requires=['pytest>=5.0.0', 'python-dotenv>=0.9.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
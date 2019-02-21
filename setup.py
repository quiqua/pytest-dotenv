from setuptools import setup

description = 'A py.test plugin that parses environment files before running tests'

setup(
    name='pytest-dotenv',
    description=description,
    long_description=description,
    version='0.4.0',
    author='Marcel Radischat',
    author_email='marcel@quiqua.eu',
    url='https://github.com/quiqua/pytest-dotenv',
    download_url='https://github.com/quiqua/pytest-dotenv/tarball/0.2.0',
    packages=['pytest_dotenv'],
    entry_points={'pytest11': ['env = pytest_dotenv.plugin']},
    install_requires=['pytest>=2.6.0', 'python-dotenv>=0.9.1'],
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
        'Programming Language :: Python :: 3.6'
    ]
)
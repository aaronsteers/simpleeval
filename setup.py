import subprocess
from setuptools import setup


def get_version():
    """Load version"""
    with open("VERSION") as buffer:
            return buffer.readline().strip()

version = get_version()

setup(
    name='simpleeval',
    py_modules=['simpleeval'],
    version=version,
    description='A simple, safe single expression evaluator library.',
    long_description=open('README.rst', 'r').read(),
    long_description_content_type='text/x-rst',
    author='Daniel Fairhead',
    author_email='danthedeckie@gmail.com',
    url='https://github.com/danthedeckie/simpleeval',
    download_url='https://github.com/danthedeckie/simpleeval/tarball/' + version,
    keywords=['eval', 'simple', 'expression', 'parse', 'ast'],
    test_suite='test_simpleeval',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python',
                 ],
)

# testver

[![PyPI version](https://badge.fury.io/py/testver.svg)](https://badge.fury.io/py/testver)

*Programmatically edit python package versions for testing.*

When publishing a python package from a continuous integration system, it can
be useful to publish it to a test package repository such as test.pypi.org.

However, package repositories only accept a certain version of a package once.
To get around this, this package edits the python version in your python code
(defined as the `<package>.__version__` variable).

This works well with systems such as flit, that require versions to be
specified in the code.

## Usage:

```bash
testver src/ --dryrun
```

This will print out all the changes the script would make. It goes through the
directory you pass, and searchers for python files called `__init__.py` or
`__version__.py` (common ways of naming the files in which version numbers
are specified).

Once found, if `--dryrun` is not specified, it will modify the python source
code. **Make sure you can easily revert this locally if you are testing**
(i.e. commit changes before you run this).

```bash
testver src/
```

For an example on how to use this in a continuous integration system, see
the 
[workflow file](https://github.com/janfreyberg/testver/blob/master/.github/workflows/test.yml#L39#L52)
of this repository.

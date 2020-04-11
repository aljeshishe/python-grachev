========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-grachev/badge/?style=flat
    :target: https://readthedocs.org/projects/python-grachev
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/aljeshishe/python-grachev.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/aljeshishe/python-grachev

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/aljeshishe/python-grachev?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/aljeshishe/python-grachev

.. |requires| image:: https://requires.io/github/aljeshishe/python-grachev/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/aljeshishe/python-grachev/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/aljeshishe/python-grachev/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/aljeshishe/python-grachev

.. |version| image:: https://img.shields.io/pypi/v/grachev.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/grachev

.. |wheel| image:: https://img.shields.io/pypi/wheel/grachev.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/grachev

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/grachev.svg
    :alt: Supported versions
    :target: https://pypi.org/project/grachev

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/grachev.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/grachev

.. |commits-since| image:: https://img.shields.io/github/commits-since/aljeshishe/python-grachev/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/aljeshishe/python-grachev/compare/v0.0.0...master



.. end-badges

Grachev package

* Free software: BSD 2-Clause License

Installation
============

::

    pip install grachev

You can also install the in-development version with::

    pip install https://github.com/aljeshishe/python-grachev/archive/master.zip


Documentation
=============


https://python-grachev.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

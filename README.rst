========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis|
        |
        | |codeclimate|
    * - package
      - | |commits-since|

.. |travis| image:: https://travis-ci.com/csci-e-29/2020sp-csci-utils-VinceGa.svg?token=xU6seRT6npfm3ro3kyke&branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/csci-e-29/2020sp-csci-utils-VinceGa

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/d4630282b8b7734ef0fd/maintainability
   :target: https://codeclimate.com/repos/5e588006824d400165010d8d/maintainability
   :alt: CodeClimate Quality Status

.. |commits-since| image:: https://img.shields.io/github/commits-since/csci-e-29/2020sp-csci-utils-VinceGa/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/csci-e-29/2020sp-csci-utils-VinceGa/compare/v0.0.0...master

.. end-badges

An example package. Generated with cookiecutter-pylibrary.

Installation
============

::

    pip install csci-utils

You can also install the in-development version with::

    pip install https://github.com/csci-e-29/2020sp-csci-utils-VinceGa/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import csci_utils
    csci_utils.longest()


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

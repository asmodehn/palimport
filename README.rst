palimport
=========

Palimpsest importer for python

Palimport allows you to import modules that can be defined in any custom language, as long as you provide a grammar and way to interpret it ( in python !)

This way you can embed multiple DSLs in your python programs.

Supported parsers :

- lark
- more to come

Currently tested with python 3.5::

    pytest tests/


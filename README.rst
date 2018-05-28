palimport
=========

.. image:: https://travis-ci.org/asmodehn/palimport.svg?branch=master
    :target: https://travis-ci.org/asmodehn/palimport

Palimpsest importer for python

Palimport allows you to import modules that can be defined in any custom language, as long as you provide a grammar and way to interpret it ( in python !)
This way you can embed multiple DSLs in your python programs.

Why ?
-----

Because managing importer properly, and following python package logic, is not trivial.
So if you want to embed your programming language into python, and leverage all python tools and libraries, better implement your importer in palimport.

Benefits
--------

Here are a few benefits of using palimport to teach new languages to your favorite python interpreter::

- Already implemented Python 2/3 importer compatibility (using filefinder2)
- Importer is enabled/disabled as a context manager, so you stay in control over what can be imported or not.
- Compare your importers with other importers right here, and be notified when an importer is changed.


Roadmap
-------


Currently Supported parsers include ::

- hy [TODO]
- coconut [TODO]
- lark
- add yours here !

Currently tested with python 3.5::

    pytest tests/


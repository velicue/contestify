#  Game Master

## Dependency

  + Python2 with virtualenv
  + MongoDB 2.6.1 or latter

## Installation

Make sure you have python2 and virtualenv in ``PATH``, then run the following command:

	cd manage
	./quickinstall

*Notice* If you are using Mac, you may need to install libevent with you package manger.
And if you are using macports, run following command instead:

	cd manage
	CLAGS="-I /opt/local/include -L /opt/local/lib" ./quickinstall

## Configuration
Website configuration lies in ``common/gmconfig.py``. You can specify your own
configuration (such as database host and post other than given) in ``common/config.py``,
which will be ignored by git.

## Run
Hooray! To start the website:

	./start.py


# Modules
The website is decoupled into several modules:

  + api: RESTful apis
  + common: configurations
  + manage: scripts that helps better manage the development
  + model: mongoengine Document definitions
  + tests: unit test
  + routes: routes of the website 
  + gm: application entrance


# Test
If you are not familiar with python unittest, please read through [http://docs.python.org/2/library/unittest.html](http://docs.python.org/2/library/unittest.html)
to understand basic concepts and practices.

To test:

    ./tests/run_tests.py

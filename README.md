Fork Feed
=========

This is a small but very useful utility for each GitHub user.
It allows to track all changes in all forks of your projects.

Installation
------------

    easy_install forkfeed

Usage
-----

    forkfeed svetlyak40wt

This will create `svetlyak40wt-projectname.xml` for each project. Or

    forkfeed svetlyak40wt/cony

This will create `svetlyak40wt-cony.xml` only.

You can setup a cron to update feeds on a hourly basis and serve feeds
using a webserver.

Development
-----------

To install forkfeed in development environment, run `./bootstrap.sh`.
It will create a virtual environment and install forkfeed and all
dependencies there.

Feel free to send me your pull requests.

Credits
-------

Alexander Artemenko (author)

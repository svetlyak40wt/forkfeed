Fork Feed
=========

This is a small but very useful utility for each GitHub user.
It allows to track all changes in all forks of your projects.

Installation
------------

    easy_install forkfeed

Usage
-----

    forkfeed.py svetlyak40wt

This will create `svetlyak40wt-projectname.xml` for each project. Or

    forkfeed.py svetlyak40wt/cony

This will create `svetlyak40wt-cony.xml` only.

You can setup a cron to update feeds on a hourly basis and serve feeds
using a webserver.

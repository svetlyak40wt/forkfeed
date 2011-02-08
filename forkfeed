#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement

import logging
import feedgenerator

from opster import command
from github2.client import Github

@command(usage='%name (username or username/repository) [-o output.xml]')
def main(
        repository_or_username,
        output_filename=('o', '%(username)s-%(repository)s.xml', 'output filename'),
    ):
    """Utility to build Atom feed for new commits from your projects' forks on the GitHub."""

    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.DEBUG,
    )
    log = logging.getLogger()

    gh = Github()

    if '/' in repository_or_username:
        username, repository = repository_or_username.split('/', 1)
        repositories = [repository]
    else:
        username = repository_or_username
        repositories = [rep.name for rep in gh.repos.list(username)]

    for repository in repositories:
        full_repname = username + '/' + repository
        log.info('Processing %s' % full_repname)

        # first, we need to get the date of the last commit
        commits = gh.commits.list(full_repname, 'master')
        last_commit_date = commits[0].committed_date

        feed = feedgenerator.Atom1Feed(
            title=u'%s forks' % full_repname,
            link=u'http://github.com/%s' % full_repname,
            description=u'Commits from forks of %s repository at GitHub.' % full_repname,
            language=u'en',
        )

        for fork in gh.repos.network(full_repname):
            fork_repname = '%(owner)s/%(name)s' % fork

            log.info('Fetching commits from %s' % fork_repname)
            fork_commits = gh.commits.list(fork_repname, 'master')

            for commit in reversed(fork_commits):
                if commit.committed_date > last_commit_date:
                    short_commit_message = commit.message.split('\n', 1)[0]
                    log.debug(
                        u'%s %s %s %s',
                        fork_repname,
                        commit.committed_date,
                        commit.author['login'],
                        short_commit_message
                    )

                    feed.add_item(
                        title=fork_repname + ' ' + short_commit_message,
                        link=u'http://github.com/%s/commit/%s' % (fork_repname, commit.id),
                        description=commit.message,
                        author_name=commit.author['name'],
                        author_email=commit.author['email'],
                        author_link=u'http://github.com/' + commit.author['login'],
                    )

        with open(output_filename % locals(), 'w') as f:
            feed.write(f, 'utf-8')


if __name__ == '__main__':
    main()

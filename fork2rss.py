#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from github2.client import Github

def main(repository):
    """Data processor.

    Argument repos should be given in form username/repname.
    """
    gh = Github()

    # first, we need to get the date of the last commit
    commits = gh.commits.list(repository, 'master')
    last_commit_date = commits[0].committed_date

    for fork in gh.repos.network(repository):
        fork_repname = '%(owner)s/%(name)s' % fork
        fork_commits = gh.commits.list(fork_repname, 'master')

        for commit in reversed(fork_commits):
            if commit.committed_date > last_commit_date:
                short_commit_message = commit.message.split('\n', 1)[0]
                print fork_repname, commit.committed_date, short_commit_message

if __name__ == '__main__':
    #main(sys.argv[1])
    main('svetlyak40wt/cony')

# culture-shock
Automatically exported from code.google.com/p/culture-shock

# STATUS: INCOMPLETE AND UNUSABLE.

Just trying to get some ideas down

# Overview

A little rivalry and competition never hurt anyone!  Now you can see which developers are helping improve the development culture, and what's hurting.

Points can be scored by:
 * committing new code
 * keeping the build green
 * cleaning up old code
 * reducing code complexity
 * improving code test coverage
 * adding new tests

Points are lost when:
 * build is broken
 * tests fail
 * code complexity increases substantially

The vision is to build a framework that uses score-generator plugins.  A score-generator uses whatever voodoo is necessary to analyze a single code commit to the repository.

These plugins may pull data from external sources including continuous build automation tools (buildbot, cruisecontrol, hudson), the code repository itself (svn, hg, etc). 

We feed the configuration's list of plugins the commits from a repository we're watching, then compile statistics, calculate points, and see who's doing what.  The feed into the engine might be controlled by a post-commit hook, such as the ones used by [http://code.google.com/p/support/wiki/PostCommitWebHooks google code] or [http://help.github.com/post-receive-hooks/ github].

A web app and flex/air app will display the leaderboard (daily, weekly, monthly, all-time).

The concept is similar to [https://help.launchpad.net/YourAccount/Karma Launchpad's Karma scoring], but offers an advantage because it analyzes not only that you did something, but _how well_ you did something.  *The goal isn't to highlight the studs and discourage newbies, but rather to encourage everyone to try to improve the craft.*

""" Plugins module provides the plugin interface, as well as some sample plugins
"""

__id__ = "$Id: $"


class IPlugin(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def parse(self, commit_info):
        pass

    def generate_score(self):
        pass


class LinesOfCodePlugin(IPlugin):
    """ Scores based on number of lines of code committed """


class DoesItCompilePlugin(IPlugin):
    """ Ensures no syntax errors and gives score. """


class CleaningUpOldCodePlugin(IPlugin):
    """ Points are scored for removing old code.  (although if brand new code is
        added on top of this, scores will cancel)
    """


class PythonComplexityPlugin(IPlugin):
    """ Analyses complexity of code committed """


class PyLintPlugin(IPlugin):
    """ Analyses and scores based on how well PyLint scores the code """


class BuildBotPlugin(IPlugin):
    """ Looks-up results of commit on BuildBot slaves to determine affect of
        change.
    """

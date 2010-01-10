""" Test the plugins """

__id__ = "$Id: $"

from nose import tools as NT
from cultureshock import plugins


class TestPluginInterface(object):

    def test_should_attach_constructor_arguments_to_class(object):
        p = plugins.IPlugin(a=1, b='2', c='three')

        NT.assert_equals(p.a, 1)
        NT.assert_equals(p.b, '2')
        NT.assert_equals(p.c, 'three')

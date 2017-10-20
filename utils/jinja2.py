from __future__ import absolute_import
from jinja2 import Environment
from django.core.urlresolvers import reverse


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'reverse': reverse,
    })
    return env


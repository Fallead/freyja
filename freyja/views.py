# -*- coding: utf-8 -*-
import logging

from django.views.generic import TemplateView
from django.http import HttpResponse

from utils.permissionmixin import PermissionMixin

logger = logging.getLogger(__name__)


def login(request):
    pass


def logout(request):
    pass


def signup(request):
    pass


def forget(request):
    pass


def reset_password(request):
    pass


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(PermissionMixin, TemplateView):
    template_name = 'about.html'

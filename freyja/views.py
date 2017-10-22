# -*- coding: utf-8 -*-
import logging

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from utils.permissionmixin import PermissionMixin

logger = logging.getLogger(__name__)


def login(request):
    # if user already login, redirect to index
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    # process POST request
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user and user.is_active:
            # core
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, template_name, {'errors': True})
    # process GET request
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        print request.POST.get('username')
        print request.POST.get('email')
        print request.POST.get('password')
        return HttpResponse('ok')
    else:
        return render(request, 'signup.html')


def forget(request):
    pass


def reset_password(request):
    pass


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(PermissionMixin, TemplateView):
    template_name = 'about.html'

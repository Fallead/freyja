# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from utils.exceptions import UserNotLoginException


class PermissionMixin(object):
    def check_login(self):
        if not self.request.user.is_authenticated():
            raise UserNotLoginException

    def dispatch(self, request, *args, **kwargs):
        try:
            self.check_login()
        except UserNotLoginException:
            return HttpResponseRedirect(redirect_to=reverse('index'))
        return super(PermissionMixin, self).dispatch(request, *args, **kwargs)

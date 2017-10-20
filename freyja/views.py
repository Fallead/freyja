# -*- coding: utf-8 -*-
import logging

from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        logger.warning('test')
        return context

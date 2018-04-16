# -*- coding: utf-8 -*-
from django.http.response import Http404
from django.views.generic import TemplateView
from .models import Instance


class InstancesView(TemplateView):
    template_name = "microb/index.html"

    def get_context_data(self, **kwargs):
        context = super(InstancesView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser is False:
            raise Http404
        context["instances"] = Instance.objects.all()
        return context

from django.views.generic import TemplateView
from authtools.views import LoginRequiredMixin
from accounts import const

from . import mixins
from . import models


class DashboardView(mixins.UserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'cowork/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.user.user_type == const.USER_TYPE_COMPANY:
            context['last_locations'] = models.Location.objects.filter(company__user=self.user)[:5]
        return context


class SearchView(TemplateView):
    template_name = 'cowork/search.html'


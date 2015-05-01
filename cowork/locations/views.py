from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from accounts import const
from braces import views

from .. import forms
from .. import models
from .. import mixins


class LocationListView(mixins.UserMixin, views.LoginRequiredMixin, generic.ListView):
    context_object_name = 'location_list'
    company_template_name = "cowork/locations/company/location_list.html"
    coworker_template_name = "cowork/locations/coworker/location_list.html"

    def get_template_names(self):
        if self.user.user_type == const.USER_TYPE_COMPANY:
            return self.company_template_name
        else:
            return self.coworker_template_name

    def get_queryset(self):
        # TODO: get office of given users
        return models.Location.objects.filter(company__user=self.user)


class LocationAddView(mixins.UserMixin, views.LoginRequiredMixin, generic.FormView):
    form_class = forms.LocationCreationForm
    template_name = "cowork/locations/company/location_add.html"
    success_url = reverse_lazy('cowork:locations:list')

    def form_valid(self, form):
        if self.user.companies.count() > 0:
            self.object = form.save(commit=False)
            self.object.company = self.user.companies.first()
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())

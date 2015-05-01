from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from accounts import const
from braces import views

from .. import forms
from .. import models


class UserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(UserMixin, self).dispatch(request, *args, **kwargs)


class OfficeListView(UserMixin, views.LoginRequiredMixin, generic.ListView):
    context_object_name = 'office_list'
    company_template_name = "cowork/offices/company/office_list.html"
    coworker_template_name = "cowork/offices/coworker/office_list.html"

    def get_template_names(self):
        if self.user.user_type == const.USER_TYPE_COMPANY:
            return self.company_template_name
        else:
            return self.coworker_template_name

    def get_queryset(self):
        # TODO: get office of given users
        return models.Office.objects.filter(company__user=self.user)


class OfficeAddView(UserMixin, views.LoginRequiredMixin, generic.FormView):
    form_class = forms.OfficeCreationForm
    template_name = "cowork/offices/company/office_add.html"
    success_url = reverse_lazy('cowork:offices:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.company = self.user.companies.first()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

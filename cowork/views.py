from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from authtools.views import LoginRequiredMixin
from accounts import const
from . import forms
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

    def get(self, request, *args, **kwargs):
        return render_to_response('cowork/search.html', {'location': 0, 'city': "...",
                                                         }, context_instance=RequestContext(request))

    def post(self, request):
        if request.POST:
            city_name =request.POST.get('city_name', False)
            location = models.Location.objects.filter(city=city_name)

            return render_to_response('cowork/search.html', {'location': location, 'city': location[0].city, },
                                      context_instance=RequestContext(request))


def rent_desk(request, pk):
    form = forms.DeskCreateForm(request.POST or None)
    location = models.Location.objects.get(id=pk)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.owner = request.user
        save_it.location = location
        save_it.save()
        print "Save form"
        return HttpResponseRedirect('/')
    return render_to_response('cowork/rent_desk.html', context_instance=RequestContext(request))




from __future__ import absolute_import, unicode_literals

from dash.orgs.views import OrgPermsMixin
from django.utils.translation import ugettext_lazy as _
from smartmin.users.views import SmartTemplateView
from tracpro.groups.models import Group
from tracpro.polls.models import Issue


class HomeView(OrgPermsMixin, SmartTemplateView):
    """
    TracPro homepage
    """
    title = _("Home")
    template_name = 'home/home.haml'

    def has_permission(self, request, *args, **kwargs):
        return request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        if self.request.region:
            issues = self.request.region.issues
        else:
            issues = Issue.get_all(self.request.org)

        context['latest_issues'] = issues.order_by('-conducted_on')[0:3]
        context['all_groups'] = Group.get_all(self.request.org).order_by('name')
        return context

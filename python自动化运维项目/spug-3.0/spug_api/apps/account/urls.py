# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.urls import path

from spug_api.apps.account.views import *
from spug_api.apps.account.history import *

urlpatterns = [
    path(r'^login/$', login),
    path(r'^logout/$', logout),
    path(r'^user/$', UserView.as_view()),
    path(r'^role/$', RoleView.as_view()),
    path(r'^self/$', SelfView.as_view()),
    path(r'^login/history/$', HistoryView.as_view())
]

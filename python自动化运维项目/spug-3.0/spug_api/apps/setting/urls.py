# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
# from django.urls import path
from django.urls import path
from spug_api.apps.setting.views import *
from spug_api.apps.setting.user import UserSettingView

urlpatterns = [
    path(r'^$', SettingView.as_view()),
    path(r'^user/$', UserSettingView.as_view()),
    path(r'^ldap_test/$', ldap_test),
    path(r'^email_test/$', email_test),
    path(r'^mfa/$', MFAView.as_view()),
    path(r'^about/$', get_about),
    path(r'^push/bind/$', handle_push_bind),
    path(r'^push/balance/$', handle_push_balance),
]

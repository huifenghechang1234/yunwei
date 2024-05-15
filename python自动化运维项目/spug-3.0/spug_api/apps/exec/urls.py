# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.urls import re_path

from spug_api.apps.exec.views import *
from spug_api.apps.exec.transfer import TransferView

urlpatterns = [
    re_path(r'template/$', TemplateView.as_view()),
    re_path(r'do/$', TaskView.as_view()),
    re_path(r'transfer/$', TransferView.as_view()),
]

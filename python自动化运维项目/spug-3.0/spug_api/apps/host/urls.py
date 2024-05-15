# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.urls import path

from spug_api.apps.host.views import *
from spug_api.apps.host.group import GroupView
from spug_api.apps.host.extend import ExtendView
from spug_api.apps.host.add import get_regions, cloud_import

urlpatterns = [
    path('', HostView.as_view()),
    path('extend/', ExtendView.as_view()),
    path('group/', GroupView.as_view()),
    path('import/', post_import),
    path('import/cloud/', cloud_import),
    path('import/region/', get_regions),
    path('parse/', post_parse),
    path('valid/', batch_valid),
]

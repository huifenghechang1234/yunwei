# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from spug_api.channels.routing import ProtocolTypeRouter
from spug_api.consumer import routing

application = ProtocolTypeRouter({
    'websocket': routing.ws_router
})

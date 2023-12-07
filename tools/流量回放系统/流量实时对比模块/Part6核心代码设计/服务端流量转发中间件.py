# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:27
# @Author : waxberry
# @File : 服务端流量转发中间件.py
# @Software : PyCharm


# copyFlow2Proxy.py
from mitmproxy import http
from mitmproxy import ctx
import typing


class copyFlow2ForwardProxy:
    def __init__(self):
        self.address = ('{sourceHost}', {sourcePort})
        pass

    def proxy_address(self, flow: http.HTTPFlow) -> typing.Tuple[str, int]:
        return self.address

    def request(self, flow: http.HTTPFlow):
        if flow.request.method == "CONNECT":
            return

        if flow.is_replay == 'request':
            return

        if "view" in ctx.master.addons:
            ctx.master.commands.call("view.flows.add", [flow])

        if flow.live:
            address = self.proxy_address(flow)
            flow.live.change_upstream_proxy_server(address)
            f = flow.copy()
            f.request.headers["RequestId"] = flow.id
            ctx.master.commands.call("replay.client", [f])


addons = [
    copyFlow2ForwardProxy()
]
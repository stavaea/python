# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:23
# @Author : waxberry
# @File : 获取流量response的中间件.py
# @Software : PyCharm


# getReplayResponse.py
import mitmproxy.http
from bs4 import BeautifulSoup
from mitmproxy import ctx
import logging, json, typing, requests, hashlib

PARSE_ERROR = object()

def parse_json(s: bytes) -> typing.Any:
    try:
        return json.loads(s.decode('utf-8'))
    except ValueError:
        return PARSE_ERROR

class MappingAddonConfig:
    HTML_PARSER = "html.parser"

class GetReplayResponse:
    def __init__(self):
        self.serverDomain = "{appHost}"
        self.taskId = "{taskId}"
        self.logger = logging.getLogger(self.__class__.__name__)

    def uploadToServer(self, requestId, responseData, replayRespHash):
        url = self.serverDomain + '/api/replayManage/getResponseFromProxy'
        data = {{
            'taskId': self.taskId,
            'requestId': requestId,
            'responseData': responseData,
            'replayRespHash': replayRespHash,
        }}
        headers = {{'Content-Type': 'application/json'}}
        res = requests.post(url, data=json.dumps(data), headers=headers)
        resp = res.json()
        if resp['code'] != 0:
            ctx.log.info("upload [ %s ] flow failed " % requestId)

    def response(self, flow: mitmproxy.http.HTTPFlow) -> None:
        """If a response is received, check if we should replace some content. """
        try:
            requestId = flow.id
            res = flow.response
            if res is not None:
                encoding = res.headers.get("content-encoding", "utf-8")
                content_type = res.headers.get("content-type", "text/html")
                replayRespHash = hashlib.sha256(res.raw_content).hexdigest()
                responseData = ''
                if "text/html" in content_type and encoding == "utf-8":
                    content = BeautifulSoup(res.content, MappingAddonConfig.HTML_PARSER)
                    responseData = content.encode(encoding)
                elif "json" in content_type:
                    data = parse_json(res.content)
                    if data is not PARSE_ERROR:
                        responseData = data
                    else:
                        self.logger.warning(
                            f"PARSE_ERROR content type '{{content_type}}'")
                else:
                    self.logger.warning(f"Unsupported content type '{{content_type}}' or content encoding '{{encoding}}'")
                self.uploadToServer(requestId, responseData, replayRespHash)
        except KeyError:
            pass


addons = [
    GetReplayResponse()
]
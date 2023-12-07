# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:23
# @Author : waxberry
# @File : mitmproxy中的自定义dump接口.py
# @Software : PyCharm


# mitmproxy/tools/web/app.py
class FlowDumpByIdHandler(RequestHandler):
    def get(self):
        self.set_header("Content-Disposition", "attachment; filename=flows")
        self.set_header("Content-Type", "application/octet-stream")

        save_ids = self.json

        bio = BytesIO()
        fw = io.FlowWriter(bio)
        for f in self.view:
            if save_ids['saveIds']:
                if f.id in save_ids['saveIds']:
                    fw.add(f)

        self.write(bio.getvalue())
        bio.close()
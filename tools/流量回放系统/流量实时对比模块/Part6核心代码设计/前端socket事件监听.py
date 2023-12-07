# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:27
# @Author : waxberry
# @File : 前端socket事件监听.py
# @Software : PyCharm


this.wsClient.onmessage = e = > {
    try {
        const data = JSON.parse(e.data);
        if (data.resource == = "flows"){
            switch (data.cmd) {
            case 'add': {
                const
                record = data.data;
                this.updateFlowStatus([record])
                break;
            }
            case
                'update': {
                const
                record = data.data;
                this.updateFlowStatus([record])
                break;
            }
            case
                'remove': {
                const
                recordId = data.data;
                this.removeFlow(recordId)
                break;
            }
            default: {
                break;
            }
        }
    }
    } catch(error)
    {
        console.error(error);
        console.error('Failed to parse the websocket data with message: ', e.data);
    }
}
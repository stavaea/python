# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:21
# @Author : waxberry
# @File : 前端对比模块.py
# @Software : PyCharm


// DiffView.js
import React, { Component } from 'react';
import ReactDiffViewer, { DiffMethod } from 'react-diff-viewer';

import styles from './index.less';

export default class Page extends Component {
    render() {
        const { leftTitle, rightTitle, srcResponse, dstResponse } = this.props;
        return (
        <div className={styles.diffContainer}>
            <ReactDiffViewer
            leftTitle={leftTitle}
            rightTitle={rightTitle}
            oldValue={JSON.stringify(srcResponse, null, 2)}
            newValue={JSON.stringify(dstResponse, null, 2)}
            splitView
            // showDiffOnly={false}
            compareMethod={DiffMethod.JSON}
            // renderContent={this.highlightSyntax}
            />
        </div>
        )
    }
}
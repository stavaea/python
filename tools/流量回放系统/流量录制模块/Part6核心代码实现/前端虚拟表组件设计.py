# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:14
# @Author : waxberry
# @File : 前端虚拟表组件设计.py
# @Software : PyCharm

import React, { useRef, useEffect, useMemo } from 'react';
import { Table } from 'antd';
import { useVT } from 'virtualizedtableforantd4';

const MyRow = React.forwardRef((props, ref) => {
  const { children, ...rest } = props;
  return <tr {...rest} ref={ref}>{children}</tr>;
});
function CustomRowsHooks(props) {
  const columns = useRef(props.columns);
  const [VT, setVT] = useVT(() => ({ scroll: { y: 600 }, debug: true }));
  useMemo(() => setVT({ body: { row: MyRow } }), [setVT]);
  return (
    <Table
      {...props}
      components={VT}
      scroll={{ y: 600 }}
      dataSource={props.dataSource}
      columns={columns.current}
    />
  );
}

export default CustomRowsHooks;
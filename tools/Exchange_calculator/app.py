# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2022/8/30 11:52
# @Author : waxberry
# @File : app.py
# @Software : PyCharm

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrp_components as dbc

try:
    app = Dash(__name__, external_stylesheets=['http://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css'])
    print ('此网页渲染基于在线的css')
except:
    app = Dash(__name__, external_stylesheets=[r"E:\Desktop\My_Python\Dash\css\bootstrap.min.css"])
    print ('此网页渲染基于本地的css')
app.title = '在线汇率计算器'


def item(name, img_path):
    return dbc.ListGroupItem([html.H5(name), html.Img(src=img_path), html.H5('---', id=name, className='float-right')])


app.layout = dbc.Container(
    children=[
        dbc.ListGroup([
            dbc.ListGroupItem(children=[
                html.H1("汇率计算器-简单版",style={'textAlign': 'center','color':'#272528'}),
                html.P('输入：用于兑换外币的人民币数；输出：能兑换到的外币数；单位：单位币值。',style={'textAlign': 'center','color':'#BB002D'}),
                dbc.Input(value = 0, id = 'input', type='number')
            ],active=True),
            item('JPY','./assets/Japan.jpg'),
            item('USD','./assets/USA.jpg'),
            item('GBP','./assets/UK.jpg'),
            item('HKD','./assets/Hongkong.jpg'),
            item('EUR','./assets/EU.png'),
            item('CHF','./assets/France.png'),
            item('INR','./assets/India.jpg')
        ],className='shadow')
    ],style={'padding':'2rem'}
)

@app.callback(
    output = [
    Output('JPY', 'children'),
    Output('USD', 'children'),
    Output('GBP', 'children'),
    Output('HKD', 'children'),
    Output('EUR', 'children'),
    Output('CHF', 'children'),
    Output('INR', 'children')
    ],
    inputs = [Input('input', 'value')]
    )
def rule(rmb):
    rmb = rmb if rmb is not None else 0
    return (
        f'{round(rmb/0.0501,2)} ￥',
        f'{round(rmb/6.7646,2)} ＄',
        f'{round(rmb/8.1682,2)} ￡',
        f'{round(rmb/0.8615,2)} ￥',
        f'{round(rmb/6.8881,2)} €',
        f'{round(rmb/7.0309,2)} €',
        f'{round(rmb/0.0852,2)} $'
        )
# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/5/26 16:52
# @Author : waxberry
# @File : Greeting_cards.py
# @Software : PyCharm

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.platypus import Paragraph

def table_pargraph(name):
    doc = SimpleDocTemplate('table_pargraph.pdf', pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    pheader = f'<font color=black size=14>To {name}: </font>'
    p0 = Paragraph(pheader, styles['Normal'])

    # 挑选一张精美的图片
    im = Image('best_wished.jpeg')
    im.drawHeight = 5 * inch * im.drawHeight / im.drawWidth
    im.drawWidth = 3 * inch
    colwidth = (3.5 * inch, 2.5 * inch, 0.2 * inch)
    colheight = inch

    data = [[im, p0, ''],
            ['', '', ''],
            ['', '', ''],
            ['', 'Best', ''],
            ['', 'Wishes!', ''],
            ]
    tblstyle = TableStyle([
        ('ALIGN', (-2, 4), (-2, 4), ('LEFT')),
        ('ALIGN', (-2, -1), (-2, -1), 'RIGHT'),
        ('TEXTCOLOR', (-1, -2), (-1, -1), colors.black),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEABOVE', (-2, -4), (-2, -2), 2, colors.black),
        ('SPAN', (0, 0), (0, -1)),
        ('VALIGN', (-2, -1), (-2, -1), 'TOP'),

    ])

    tbl = Table(data, colWidths=colwidth)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    name = 'xxx'
    table_pargraph(name)
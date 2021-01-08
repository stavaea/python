from xml.etree import ElementTree

tree=ElementTree.parse('a.xml')

root=tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root.text)

#三种查找方式
#从子节点中找
# print(root.find('country'))
# print(root.findall('country'))
# print(root.find('rank')) #None


#从正树形结构中查找
# print(list(root.iter('rank')))

# for country in root.findall('country'):
#     rank=country.find('rank')
#     print(rank.tag,rank.attrib,rank.text)


#遍历文档树
# for country in root:
#     print('=============>',country.attrib['name'])
#     for item in country:
#         print(item.tag,item.attrib,item.text)


# for year in root.iter('year'):
#     print(year.tag,year.attrib,year.text)


# for year in root.iter('year'):
#     year.set('updated',"yes")
#     year.text=str(int(year.text)+1)
#
# tree.write('a.xml')

# for country in root:
#     obj=ElementTree.Element('egon') #<egon name="egon" age="18">egon is good</egon>
#     obj.attrib={'name':'egon','age':'18'}
#     obj.text='egon is good'
#     country.append(obj)
#
# tree.write('a.xml')

# for rank in root.iter('rank'):
#     if int(rank.text) == 5:
#         obj=ElementTree.Element('egon') #<egon name="egon" age="18">egon is good</egon>
#         obj.attrib={'name':'egon','age':'18'}
#         obj.text='egon is good'
#         rank.append(obj)
#
# tree.write('a.xml')









import os

# print(os.stat(r'F:\Python周末20期\day6\1 本节内容').st_size)

# res=os.system('tasklist')
# print('====>',res)

# print(os.path.split(r'F:\Python周末20期\day6\1 本节内容'))
# print(os.path.dirname(r'F:\Python周末20期\day6\1 本节内容'))
# print(os.path.basename(r'F:\Python周末20期\day6\1 本节内容'))

# print(os.path.isabs(r'C:\\a123sz'))
# print(os.path.isabs(r'/root/a123sz'))

# print(os.path.join('C:','D:\\','dir1','dir2','a.txt'))
# print(os.path.join('D:\\','dir1','dir2','a.txt'))

# print(os.path.normcase('c:/windows\\SYstem32\\..'))
# print(os.path.normpath('c://windows\\System32\\../Temp/')) #C:\windows\temp


#F:\Python周末20期\day6\3 os模块.py\..\..
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR=os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    '..',
    '..'
))
print(BASE_DIR)

# print(os.path.getsize(r'F:\Python周末20期\day6\1 本节内容'))

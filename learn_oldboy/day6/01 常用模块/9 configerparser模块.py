import configparser

config=configparser.ConfigParser()
config.read('my.ini')

# print(config.sections())
# print(config.options('mysqld'))

# print(config.get('mysqld','charater-server-set'))

# if config.has_option('mysqld','aaa'):
#     print(config.get('mysqld','aaa'))

# print(config.getboolean('mysqld','skip-grant-table'))
# print(config.getint('mysqld','port'))
# print(config.getfloat('mysqld','port'))


# config.add_section('egon')
# config.set('egon','name','egon')
# config.set('egon','age','18')

config.set('client','password','alex3714')

config.write(open('my.ini','w',encoding='utf-8'))


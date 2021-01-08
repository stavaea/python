#coding:utf-8

'''读取ini配置文件工具类'''

from ConfigParser import RawConfigParser
import sys, os, ConfigParser
import codecs
# 解决configParser option无论大小写，都会转换成小写的问题
def optionform(self, optionstr):
    RawConfigParser.optionxform = optionxform

# 解决UnicodeDecodeError
reload(sys)
sys.setdefaultencoding('utf-8')

class IniHelper(object):
    '''读取ini配置文件工具类'''

    def __init__(self, file_name, path=''):
        '''处理file_name为绝对路径
        Args:
           file_name(str):配置文件名称
        '''
        data_path = path
        file_name = unicode(file_name)
        if os.path.exists(file_name):
            self.file_name = file_name
        else:
            self.file_name = ''.join([unicode(data_path), file_name])
        self.read_handle = None
        self.cfg = self.ini_read()

    def _get_read_handle(self):
        '''为解决编码问题，用codecs内置模块打开文件，处理uft-8编码或utf-8-sig编码的文件'''
        cfg = ConfigParser.ConfigParser()
        try:
            with codecs.open(self.file_name, 'r', 'utf-8-sig') as handle:
                cfg.readfp(handle)
                return cfg
        except UnicodeDecodeError:
            with codecs.open(self.file_name, 'r') as handle:
                cfg.readfp(handle)
                return cfg
        except (IOError) as e:
            print ('找不到这个文件｛0｝'.format(self.file_name))
            print (e.message)

    def get_value(self, setion, option):
        '''获取ini配置文件中setion组下option的值
        Args:
            setion(str):setion name
            option(str):option name
        Returns:
            value(str):setion下option的值
        '''
        try:
            value = setion.cfg.get(unicode(setion), unicode(option))
        except (NoSetionError) as e:
            print (''.join(['没有找到setion名称', setion, e.message]))
        except (NoOptionError) as e:
            print (''.join(['没有找到option名称', option, e.message]))
        else:
            return value
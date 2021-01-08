#coding:utf-8

import subprocess

#获取连接电脑且具有具有操作权限的设备的deviceID
'''实例一：获取手机的设备号
场景一：电脑连接单个设备时，基本常用的adb命令执行比较方便，可以通过adb命令完成apk的安装以及日志信息的获取。
但是当电脑同时连接多台手机时，就会出现异常提示信息，超过adb支持的设备数；

这个问题有两种解决方案：
1、物理隔断大法，直接拔掉不用的设备连接。但是如果操作次数较多时就会出现画面：一个人像古老的接线员一样在反复插拔数据线。
2、针对特定的设备号进行操作： adb -s devicesID command 。但是手动执行命令获取设备ID，然后再手动配置，还是比较繁琐。
如果想用通过脚本执行adb命令，那么我们就需要过滤获取设备ID。

可以基于该脚本再优化满足自己的需求'''
def getDevicesInfo():
    out = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
    devicesList = out.stdout.read().splitlines()
    serial_nos = []#序列号
    if len(devicesList) > 2:
        for item in devicesList:
            print item
            if 'List' in item:
                continue
            elif 'no permissions' in item:
                continue
            elif item.strip() == '':
                continue
            else:
                serial_nos.append(item.split()[0])
                pass
            pass
        return serial_nos
    else:
        return -1

# 通过进程名获取并返回对应的PID
'''实例二：如何获取特定进程的pid
Python可以成功获取所有连接电脑的手机设备ID后，就可以针对特定手机来执行adb命令。
小编在实际开发和调试过程发现，经常需要查看手机进程信息，并通过PID对特定进程执行操作。
为此，开始思考如何通过进程名获取对应的PID。'''
def getPid(devices, process):
    cmd = 'adb -s %s shell ps|grep %s ' % (devices, process)
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    infos = out.stdout.read().splitlines()
    print infos
    pidList = []
    if len(infos) >= 1:
        for i in infos:
            pid = i.split()[1]
            if pid not in pidList:
                pidList.append(pid)
        return pidList
    else:
        return -1

# 获取特定设备所有monkey进程ID并强制结束monkey测试
'''实例三：如何停止疯狂的monkey
开发和测试同学在调试APP时，经常会使用monkey来测试APP的稳定性，
但是经常会出现这种场景：脚本运行结束了，但是monkey进程并没有结束，一直疯狂操作，着实很无奈。

小编从毫无经验开始历经过三种解决方案：
1、物理键强制关机后重启手机，刚开始的工作小白阶段，重启大法就是如此的万能。但是设备一多时，关机就可以按到你的手指隐隐作痛；
2、通过adb命令重启手机（adb shell reboot）,手指是不疼了，但是关机重启还是需要等待一定时间，心急时所有等待都会让人冒火；
3、通过脚本获取monkey进程ID并杀死进程：通过python脚本，只有一个双击就可以搞定之前的一切烦恼。'''
def stopMonkey(devices):
    if (devices):
        pidList = getPid.getPid(devices, 'monkey')
        if (pidList == -1):
            pass
        else:
            for index in range(len(pidList)):
                try:
                    cmd = 'adb -s %s shell kill %s ' % (devices, pidList[index])
                    subprocess.Popen(cmd, shell=True)
                    pass
                except:
                    pass
            pass
        pass
    pass

# 获取特定设备日志信息并写入本地文件
'''实例四：如何读取日志并停止
android log可以有效的帮助程序员排查和定位问题，如果通过python实现记录log信息可以避免反复输入命令的繁琐，
同时自己定义符合自己习惯的命名规则可以有效避免其他的log被覆盖的问题。

在编写python脚本时，由于没有考虑到一些细节点，导致问题，这里进行简单的分享：
在执行脚本几个小时后发现，获取并存储到本地的log文件大小居然有3.0G！！！
排查发现是由于执行脚本，文件读写忘记关闭且手机端logcat获取也并没有停止，所以logcat 输出并没有停止，并一直写入到文件。

针对这个问题尝试了很多种解决方案，最后尝试有两种方法相对有效：
1、在获取到所有的log信息后通过命令重启adb server，这种方法十分有效，但是本质上还是重启大法，实现略显简陋；
2、在关闭文件的同时，寻找方法直接停止logcat，这种方法更为合理些。'''
import time
def Logcat(devices):
    t = time.time()
    dataTag = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(t))
    path = './crash'
    try:
        file = '%s/Logcat_ApplicationName_%s_%s.txt' % (path, devices, dataTag)
        logcat_file = open(file, 'w')
        cmdLine = 'adb -s %s logcat -v time' % devices
        subprocess.Popen(cmdLine, stdout=logcat_file, shell=True, stderr=subprocess.PIPE)
        time.sleep(5)
        pidList = getPid.getPid(devices, 'logcat')
        if (pidList == -1):
            pass
        else:
            for index in range(len(pidList)):
                try:
                    cmd = 'adb -s %s shell kill %s '% (devices, pidList[index])
                    subprocess.Popen(cmd, shell=True)
                    pass
                except:
                    pass
            pass
        pass
        logcat_file.close()
        pass
    except:
        pass
    pass
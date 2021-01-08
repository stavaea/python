# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='106.74.230.135', port=22101, username='root', password='123456')
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# # 关闭连接
# ssh.close()


import paramiko

transport = paramiko.Transport(('106.74.230.135', 22101))
transport.connect(username='root', password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put(r'D:\video\python20期\day9\02 多线程\7 GIL测试.py', '/root/test.txt')
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')

transport.close()
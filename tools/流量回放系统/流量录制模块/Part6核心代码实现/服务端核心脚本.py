# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2023/12/7 17:15
# @Author : waxberry
# @File : 服务端核心脚本.py
# @Software : PyCharm


def buildContainer(taskInfo, mountPort, wsMountPort, projectDir):
    for i in range(5):
        if len(os.listdir(projectDir)) > 0:
            break
        time.sleep(1)
    if sys.platform.startswith('win'):
        projectDir = "/taskFile/"+projectDir.split('taskFile\\')[1]
    formatHost = {}
    try:
        if taskInfo:
            if taskInfo['hosts']:
                hosts = taskInfo['hosts'].split('\n')
                for host in hosts:
                    host = ' '.join(host.split())
                    host = host.split(' ')
                    if len(host) == 2:
                        formatHost[host[1]] = host[0]
            try:
                container = docker_client.containers.get(str(mountPort))
                if container.status == 'exited':
                    container.remove()
                    logger.info('移除容器成功：{}'.format(str(mountPort)))
            except:
                logger.info('can build')
            docker_client.containers.run(
                name=mountPort,
                image='myproxy:0.0.13',
                command='/bin/bash -c "sh /root/script/start_sync.sh"',
                volumes={
                    projectDir: {'bind': '/root/script', 'mode': 'rw'}
                },
                ports={'8080': mountPort, '8081': wsMountPort},
                extra_hosts=formatHost,
                stderr=True,
                detach=True
            )
            logger.info('任务 {} 创建容器 {} 成功，ws端口 {}'.format(taskInfo['id'], mountPort, wsMountPort))
            return str(mountPort)
    except Exception as e:
        logger.error(e)
        logger.error('创建容器：{} 失败'.format(mountPort))
        logger.error('请检查你的docker服务')

def copyDumpFile(projectDir, content):
    dumpFilePath = content['suiteInfo']['dumpFile']
    dumpFilePath = '../../' + dumpFilePath if os.path.isfile('../../' + dumpFilePath) else dumpFilePath
    replayDumpFile = projectDir + '/replayDumpFile'
    shutil.copyfile(dumpFilePath, replayDumpFile)

def makeSyncReplayShell(projectDir, mountPort, content):
    shellPath = '../../templte/start_sync.sh' if os.path.isfile('../../templte/start_sync.sh') else 'templte/start_sync.sh'
    with open(shellPath, 'r', encoding='utf-8') as shellFile:
        shellTemplte = shellFile.read()
        cmd = "mitmdump -nC /root/script/replayDumpFile -s /root/script/getReplayResponse.py --ssl-insecure --set ssl_version_client=all --set ssl_version_server=all"
        if content['proxySetting']:
            cmd = cmd + " --set http2=false --set mode=upstream:{proxySetting}".format(proxySetting=content['proxySetting'])
        if content['cerPem'] and content['domain']:
            cmd = cmd + " --certs {domain}=/root/script/cer.pem".format(domain= content['domain'])
        shellConfig = shellTemplte.format(cmd= cmd)
        with open(projectDir + '/start_sync.sh', 'w', encoding='utf-8') as file:
            file.write(shellConfig)

def makePem(content,projectDir):
    if content['cerPem'] and content['domain']:
        with open(projectDir + '/cer.pem', 'w', encoding='utf-8') as file:
            file.write(content['cerPem'])

def makeMiddlareScript(content,projectDir):
    responsePath = '../../templte/getReplayResponse.py' if os.path.isfile('../../templte/getReplayResponse.py') else 'templte/getReplayResponse.py'
    with open(responsePath, 'r', encoding='utf-8') as middlareFile:
        middlareTemplte = middlareFile.read()
        middlareConfig = middlareTemplte.format(appHost= app.config['HOST'],taskId=content['id'])
        with open(projectDir + '/getReplayResponse.py', 'w', encoding='utf-8') as file:
            file.write(middlareConfig)

def makeConfig(projectDir, mountPort, content):
    copyDumpFile(projectDir,content)
    makeSyncReplayShell(projectDir, mountPort,content)
    makePem(content, projectDir)
    makeMiddlareScript(content, projectDir)

@manager.option('-i','--taskId',dest='taskId',default='')
def runScript(taskId):
    now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    taskRootPath = encrypt_name(now)
    content = getTaskInfo(taskId)
    for i in range(2):
        if i == 0:
            proxyMountPort = freeport.get()
        else:
            wsMountPort = freeport.get()
    projectDir = createProjectDir(taskRootPath)
    makeConfig(projectDir, proxyMountPort, content)
    setTaskStatus(taskId, 2, taskRootPath)
    containName = buildContainer(content, proxyMountPort, wsMountPort, projectDir)
    if containName:
        setTaskStatus(taskId, 3, taskRootPath, containName, wsMountPort)
    else:
        setTaskStatus(taskId, 6)
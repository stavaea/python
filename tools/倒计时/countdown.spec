#conutdown.spec

block_cipher = None

a = Analysis(['countdown_tool.py'],
             pathex = [],
             binaries = [],
             datas = [],
             hiddenimports = [],
             hookspath = [],
             runtime_hooks = [],
             excludes = [],
             win_no_prefer_redirects = False,
             win_private_assemblies = False,
             cipher = block_cipher,
             noarchive = False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries = True,
          name = 'CountdownTool',
          debug = False,
          bootloader_ignore_signals = False,
          strip = False,
          upx = True,
          console = False, #不显示控制台窗口
          icon = 'countdown.ico') #可选，添加图标

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip = False,
               upx = True,
               name = 'CountdownTool')

#打包命令:D:\python\tools\倒计时>pyinstaller countdown.spec
from lib import common
from lib import sql

def shop():
    print('购物......')

def check_balance():
    print('查看余额......')
    res=sql.execute('select balance from user where id=3')
    print(res)

def transfer_accounts():
    print('转账......')
    #记录日志
    log_msg='egon给alex转了1毛钱'
    # 调用日志功能记录日志
    # common.logger(log_msg)
    logger=common.logger_handle('转账')
    logger.debug(log_msg)

def run():
    msg='''
    1 购物
    2 查看余额
    3 转账
    '''
    while True:
        print(msg)
        choice=input('>>: ').strip()
        if not choice:continue
        if choice == '1':
            shop()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            transfer_accounts()
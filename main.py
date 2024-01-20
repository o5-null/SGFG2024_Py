import time
import subprocess
import os
import platform #获取系统类型
from pathlib import Path
from loguru import logger
Path('log').mkdir(exist_ok = True)
log_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())

def naive_proxy(listen_port, proxy, type ='https'):
    log_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    log_path = str(Path('log/naive_'+proxy+'_'+log_time+'.log').resolve())
    log_net_path = str(Path('log/naive_net_'+proxy+'_'+log_time+'.log').resolve())
    if proxy == '龟苓膏':
        cmd = 'naive --listen=socks://127.0.0.1:'+listen_port+' --proxy='+type+'://sgfg:t2GhiyJOJlzk9fKm26O5eg==@worst-proxy.digital:443 --log='+log_path+' --log-net-log='+log_net_path
    elif proxy == '烧仙草':
        cmd = 'naive --listen=socks://127.0.0.1:'+listen_port+' --proxy='+type+'://sgfg:Q52uG0m0BeibMT49IzMc0g==@ni.su.dwg.us.in:443 --log='+log_path+' --log-net-log='+log_net_path
    elif proxy == '黑凉粉':
        cmd = 'naive --listen=socks://127.0.0.1:'+listen_port+' --proxy='+type+'://sgfg:toi7eOpDfgdqrIdIuHgs7w==@ns.iu.dwg.us.in:443 --log='+log_path+' --log-net-log='+log_net_path
    subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT,cwd=str(Path('res').resolve()))#启动核心且设置工作目录为res
    logger.info(proxy+'节点启动成功')

naive_proxy('17788','龟苓膏')
naive_proxy('17789','烧仙草')
naive_proxy('17790','黑凉粉')
log_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
log_path = str(Path('log/core_'+log_time+'.log').resolve())
logger.info('控制器启动完成')
logger.success('访问http://0.0.0.0:9090控制面板 代理路径为0.0.0.0:7788(请手动设置 支持socks/http/https)')
time.sleep(3)
subprocess.run('sing-box run -c sub.json',shell=True,cwd=str(Path('res').resolve()))#启动核心且设置工作目录为res
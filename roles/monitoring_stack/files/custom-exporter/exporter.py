from prometheus_client import start_http_server, Gauge
import psutil
import time
import os

# 定义指标
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Host CPU usage percentage')
MEMORY_USAGE = Gauge('system_memory_usage_percent', 'Host memory usage percentage')
DISK_USAGE = Gauge('system_disk_usage_percent', 'Host disk usage percentage for /')

# 检测是否运行在容器中且挂载了宿主机目录
HOST_ROOT = '/host' if os.path.exists('/host/proc') else '/'

def get_disk_usage():
    try:
        # 如果挂载了宿主机根目录，直接读 /host
        usage = psutil.disk_usage(HOST_ROOT)
        return usage.percent
    except Exception as e:
        print(f"Error reading disk: {e}")
        return 0

def collect_metrics():
    # 1. CPU
    CPU_USAGE.set(psutil.cpu_percent(interval=None))
    
    # 2. 内存
    mem = psutil.virtual_memory()
    MEMORY_USAGE.set(mem.percent)
    
    # 3. 磁盘
    DISK_USAGE.set(get_disk_usage())

if __name__ == '__main__':
    # 启动 HTTP 服务
    start_http_server(8000)
    print(f"Custom Exporter running on port 8000. Monitoring root: {HOST_ROOT}")
    
    # 初次调用以初始化 CPU 计数器
    psutil.cpu_percent(interval=None)
    
    while True:
        collect_metrics()
        time.sleep(15)

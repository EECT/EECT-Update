from loguru import logger
import os
import datetime
import core

print("EECT Update")

# 配置日志
# 创建logs目录，如果不存在
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前日期和时间yyyy-mm-dd HH:MM:SS
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H`%M`%S")
# 设置日志文件名为当前日期和时间
log_file_name = f"EECT Update {time_now}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# 配置日志
logger.add(log_file_path, level='DEBUG', format='\n{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {module} | {message}')
logger.remove(handler_id=None)

logger.info("EECT更新程序已启动\n")
core.main()

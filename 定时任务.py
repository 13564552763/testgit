import schedule
import subprocess
import time
import logging
from datetime import datetime

# 配置日志记录
logging.basicConfig(
    filename='scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


def run_selenium_script():
    """执行Selenium脚本的主函数"""
    try:
        logging.info("开始执行订单通脚本...")
        print(f"{datetime.now()} - 开始执行订单通脚本...")

        # 使用Python解释器直接运行脚本
        result = subprocess.run(
            ["python", "订单通-后台查询.py"],
            capture_output=True,
            text=True
        )

        # 记录执行结果
        logging.info(f"脚本输出:\n{result.stdout}")
        if result.stderr:
            logging.error(f"错误信息:\n{result.stderr}")

        print(f"{datetime.now()} - 脚本执行完成!")
        logging.info("脚本执行完成")

    except Exception as e:
        error_msg = f"执行失败: {str(e)}"
        print(error_msg)
        logging.exception(error_msg)


# 设置定时任务 (每天08:00执行)
schedule.every().day.at("10:02").do(run_selenium_script)

logging.info("定时任务调度器已启动，等待执行...")
print("定时任务已启动，等待每天上午10:02点执行脚本...")

# 持续运行调度器
while True:
    try:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次任务
    except KeyboardInterrupt:
        logging.info("程序已被手动终止")
        print("\n定时任务已停止")
        break
    except Exception as e:
        error_msg = f"调度器错误: {str(e)}"
        print(error_msg)
        logging.exception(error_msg)
        time.sleep(300)  # 出错后等待5分钟再重试
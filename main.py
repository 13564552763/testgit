import subprocess

test_files = [
    "采销通-商品新增.py",
    "订单通-商品新增.py",
    "采销通-商品详情.py",
    "订单通-交收管理+调货管理.py",
    "仓单管理.py",
    "统一交收.py",
    "仓单管理.py"
]

for file in test_files:
    try:
        result = subprocess.run(["python", file], check=True)
        print(f"{file} 执行成功")
    except subprocess.CalledProcessError as e:
        print(f"{file} 执行失败: {e}")
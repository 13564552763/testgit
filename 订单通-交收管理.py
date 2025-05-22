from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # 登录流程
    driver.get("https://center-uat2.tjpgx.cn/system/login.htm")
    driver.maximize_window()

    # 输入账号密码
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "account"))
    ).send_keys("xt")
    driver.find_element(By.ID, "password").send_keys("1234567a")

    # 点击登录
    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@onclick='doLogin()']"))
    )
    login_button.click()

    # 等待登录完成后的页面加载
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '订单交易')]"))
    )

    # 点击订单交易按钮
    order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '订单交易')]"))
    )
    order_button.click()
    print("成功进入订单交易页面")
    time.sleep(2)

    # 定位并点击「交收管理」菜单（核心代码）
    jiaoshou_menu = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='交收管理']")  # 任选上述定位方式
        )
    )
    jiaoshou_menu.click()
    print("成功点击交收管理菜单")
    time.sleep(2)

    # 点击交收成交列表按钮
    ctbasegoods_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收成交列表']"))
    )
    ctbasegoods_button.click()
    print("成功进入交收成交列表页面")
    time.sleep(2)

    # 点击历史交收成交列表按钮
    JSPP_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史交收成交列表']"))
    )
    JSPP_button.click()
    print("成功进入历史交收成交列表页面")
    time.sleep(2)

    # 点击交收匹配按钮
    JSPP_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收匹配']"))
    )
    JSPP_button.click()
    print("成功进入交收匹配列表页面")
    time.sleep(2)

    # 点击交收匹配结果列表按钮
    JSPPJGLB_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收匹配结果列表']"))
    )
    JSPPJGLB_button.click()
    print("成功进入交收匹配结果列表页面")
    time.sleep(2)

    # 点击交收匹配结果列表按钮
    JSPPLSLB_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收匹配历史列表']"))
    )
    JSPPLSLB_button.click()
    print("成功进入交收匹配历史列表页面")
    time.sleep(2)
    print("操作成功")

except Exception as e:
    print(f"操作失败：{str(e)}")
    traceback.print_exc()

finally:
    driver.quit()
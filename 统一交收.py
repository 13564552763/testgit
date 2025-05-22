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
        EC.presence_of_element_located((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '统一交收')]"))
    )

    # 点击统一交收按钮
    settlement_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '统一交收')]"))
    )
    settlement_button.click()
    print("成功进入统一交收页面")
    time.sleep(3)

    # 点击合同管理按钮
    contract_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='合同管理']"))
    )
    contract_button.click()
    print("成功进入合同管理页面")
    time.sleep(3)

    # 点击交收申请按钮
    shipments_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收申请']"))
    )
    shipments_button.click()
    print("成功进入交收申请页面")
    time.sleep(3)

    # 点击付款申请按钮
    pay_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='付款申请']"))
    )
    pay_button.click()
    print("成功进入付款申请页面")
    time.sleep(3)

    # 点击异议管理按钮
    dissent_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='异议管理']"))
    )
    dissent_button.click()
    print("成功进入异议管理页面")
    time.sleep(3)

except Exception as e:
    print(f"操作失败：{str(e)}")
    traceback.print_exc()

finally:
    driver.quit()
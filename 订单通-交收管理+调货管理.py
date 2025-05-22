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
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '订单交易')]"))
    )

    # 点击订单交易按钮
    order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '订单交易')]"))
    )
    order_button.click()
    print("成功进入订单交易页面")
    time.sleep(2)

    # 定位并点击「交收管理」菜单
    Settlement_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='交收管理']"))
    )
    Settlement_management.click()
    print("成功点击交收管理菜单")
    time.sleep(2)

    # 点击交收成交列表按钮
    Settlement_transaction_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收成交列表']"))
    )
    Settlement_transaction_list.click()
    print("成功进入交收成交列表页面")
    time.sleep(2)

    # 点击提前交收挂单列表按钮
    Early_settlement_order_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='提前交收挂单列表']"))
    )
    Early_settlement_order_list.click()
    print("成功进入提前交收挂单列表页面")
    time.sleep(2)

    # 点击到期申报查看按钮
    Early_settlement_order_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='到期申报查看']"))
    )
    Early_settlement_order_list.click()
    print("成功进入到期申报查看页面")
    time.sleep(2)

    # 点击历史交收成交列表按钮
    Historical_settlement_transaction_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史交收成交列表']"))
    )
    Historical_settlement_transaction_list.click()
    print("成功进入历史交收成交列表页面")
    time.sleep(2)

    # 点击交收匹配按钮
    Settlement_matching = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收匹配']"))
    )
    Settlement_matching.click()
    print("成功进入交收匹配列表页面")
    time.sleep(2)

    # 点击交收匹配结果列表按钮
    Settlement_matching_results_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收匹配结果列表']"))
    )
    Settlement_matching_results_list.click()
    print("成功进入交收匹配结果列表页面")
    time.sleep(2)

    # 点击交收匹配历史列表按钮
    Settlement_matching_history_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收匹配历史列表']"))
    )
    Settlement_matching_history_list.click()
    print("成功进入交收匹配历史列表页面")
    time.sleep(2)

    # 定位并点击「调货管理」菜单
    Inventory_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='调货管理']"))
    )
    Inventory_management.click()
    print("成功点击调货管理菜单")
    time.sleep(2)

    # 点击普通调货按钮
    Regular_replenishment = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='普通调货']"))
    )
    Regular_replenishment.click()
    print("成功进入普通调货页面")
    time.sleep(2)

    # 点击调货列表按钮
    Transfer_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='调货列表']"))
    )
    Transfer_list.click()
    print("成功进入调货列表页面")
    time.sleep(2)

    # 点击历史调货查询按钮
    Historical_stock_transfer_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史调货查询']"))
    )
    Historical_stock_transfer_inquiry.click()
    print("成功进入历史调货查询页面")
    time.sleep(2)

except Exception as e:
    print(f"操作失败：{str(e)}")
    traceback.print_exc()

finally:
    driver.quit()

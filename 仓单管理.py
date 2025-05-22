from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# 初始化 WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    # 登录流程
    driver.get("https://center-uat2.tjpgx.cn/system/login.htm")
    driver.maximize_window()

    # 输入账号密码
    account_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "account"))
    )
    account_input.send_keys("xt")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("1234567a")

    # 点击登录按钮
    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@onclick='doLogin()']"))
    )
    login_button.click()
    print("成功登录系统")

    # 等待登录完成后的页面加载
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '仓单系统')]"))
    )

    # 点击订单交易按钮
    order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '仓单系统')]"))
    )
    order_button.click()
    print("成功进入仓单系统页面")
    time.sleep(2)

    # 点击仓库管理按钮
    ctbasegoods_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓库管理'][name*='warehouse'][uniq='15332']"))
    )
    ctbasegoods_button.click()
    print("成功进入仓库管理页面")
    time.sleep(2)

    # 点击库区管理按钮
    ctbasegoods_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='库区管理'][name*='place'][uniq='15337']"))
    )
    ctbasegoods_button.click()
    print("成功进入库区管理页面")
    time.sleep(2)

    # 定位并点击「仓单历史」菜单（核心代码）
    warehouse_receipt_history = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='仓单历史']")  # 任选上述定位方式
        )
    )
    warehouse_receipt_history.click()
    print("成功点击仓单历史菜单")
    time.sleep(2)

    # 点击交仓单历史记录查询按钮
    Bill_of_lading_history_query = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='仓单历史记录查询']"))
    )
    Bill_of_lading_history_query.click()
    print("成功进入仓单历史记录查询页面")
    time.sleep(2)

except Exception as e:
    print(f"操作失败: {str(e)}")

finally:
    # 返回主文档并关闭浏览器
    driver.switch_to.default_content()
    driver.quit()
    print("浏览器已关闭")
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
    warehouse_receipt_system = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '仓单系统')]"))
    )
    warehouse_receipt_system.click()
    print("成功进入仓单系统主页面")
    time.sleep(2)

    # 点击仓库管理按钮
    warehouse_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓库管理'][name*='warehouse'][uniq='15332']"))
    )
    warehouse_management.click()
    print("成功进入仓库管理页面")
    time.sleep(2)

    # 点击库区管理按钮
    Reservoir_area_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='库区管理'][name*='place'][uniq='15337']"))
    )
    Reservoir_area_management.click()
    print("成功进入库区管理页面")
    time.sleep(2)

    # 定位并点击「仓单管理」菜单
    warehouse_receipt_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='仓单管理']")
        )
    )
    warehouse_receipt_management.click()
    print("成功点击仓单管理菜单")
    time.sleep(2)

    # 点击库存仓单审核按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='库存仓单审核'][name*='whReceiptBatch'][uniq='15343']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入库存仓单审核页面")
    time.sleep(2)

    # 点击预制仓单审核按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='预制仓单审核'][name*='inventory'][uniq='15346']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入预制仓单审核页面")
    time.sleep(2)

    # 点击仓单管理按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓单管理'][name*='whReceipt'][uniq='15351']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入仓单管理页面")
    time.sleep(2)

    # 点击仓单注销按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓单注销'][name*='whCancel'][uniq='15357']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入仓单注销页面")
    time.sleep(2)

    # 点击仓单提货按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓单提货'][name*='whPickApply'][uniq='15360']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入仓单提货页面")
    time.sleep(2)

    # 点击仓库缩期按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓库缩期'][name*='whreduce'][uniq='15363']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入仓库缩期页面")
    time.sleep(2)

    # 点击厂库缩期按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='厂库缩期'][name*='whreduce'][uniq='15365']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入厂库缩期页面")
    time.sleep(2)

    # 点击仓单展期按钮
    Inventory_warehouse_receipt_review = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='仓单展期'][name*='whextend'][uniq='15367']"))
    )
    Inventory_warehouse_receipt_review.click()
    print("成功进入仓单展期页面")
    time.sleep(2)

    # 定位并点击「仓单历史」菜单
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
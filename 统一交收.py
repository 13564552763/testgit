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

    # 点击开票管理按钮
    pay_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='开票管理']"))
    )
    pay_button.click()
    print("成功进入开票管理页面")
    time.sleep(3)

    # 点击异议管理按钮
    Dispute_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='异议管理']"))
    )
    Dispute_management.click()
    print("成功进入异议管理页面")
    time.sleep(3)

    # 定位并点击「升贴水参数设置」菜单
    Premium_and_discount_parameter_settings = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='升贴水参数设置']")
        )
    )
    Premium_and_discount_parameter_settings.click()
    print("成功点击升贴水参数设置菜单")
    time.sleep(2)

    # 点击品质升贴水列表按钮
    Quality_premium_and_discount_list = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='品质升贴水列表']"))
    )
    Quality_premium_and_discount_list.click()
    print("成功进入品质升贴水列表页面")
    time.sleep(3)

    # 定位并点击「结算单管理」菜单
    Settlement_document_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='结算单管理']")
        )
    )
    Settlement_document_management.click()
    print("成功点击结算单管理菜单")
    time.sleep(2)

    # 点击交收合同结算单管理按钮
    Settlement_management_for_delivery_contracts = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='交收合同结算单管理']"))
    )
    Settlement_management_for_delivery_contracts.click()
    print("成功进入交收合同结算单管理页面")
    time.sleep(3)

    # 定位并点击「基础配置」菜单
    Settlement_document_management = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='基础配置']")
        )
    )
    Settlement_document_management.click()
    print("成功点击基础配置菜单")
    time.sleep(2)

    # 点击合同模板配置按钮
    Contract_template_configuration = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='合同模板配置']"))
    )
    Contract_template_configuration.click()
    print("成功进入合同模板配置页面")
    time.sleep(3)

except Exception as e:
    print(f"操作失败：{str(e)}")
    traceback.print_exc()

finally:
    driver.quit()
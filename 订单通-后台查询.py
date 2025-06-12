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
    time.sleep(5)

    # 定位并点击「后台查询」菜单
    Back_end_query = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h3[text()='后台查询']"))
    )
    Back_end_query.click()
    print("成功点击后台查询菜单")
    time.sleep(5)

    # 点击当日委托查询按钮
    Today_orders_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='当日委托查询']"))
    )
    Today_orders_inquiry.click()
    print("成功进入当日委托查询页面")
    time.sleep(5)

    # 点击历史委托查询按钮
    Historical_order_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史委托查询']"))
    )
    Historical_order_inquiry.click()
    print("成功进入历史委托查询页面")
    time.sleep(5)

    # 点击当日代转委托查询按钮
    Same_day_proxy_transfer_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='当日代转委托查询']"))
    )
    Same_day_proxy_transfer_inquiry.click()
    print("成功进入当日代转委托查询页面")
    time.sleep(5)

    # 点击历史代转委托查询按钮
    Historical_proxy_transfer_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史代转委托查询']"))
    )
    Historical_proxy_transfer_inquiry.click()
    print("成功进入历史代转委托查询页面")
    time.sleep(5)

    # 点击当日成交查询按钮
    Daily_transaction_query = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='当日成交查询']"))
    )
    Daily_transaction_query.click()
    print("成功进入当日成交查询页面")
    time.sleep(5)

    # 点击历史成交查询按钮
    Historical_transaction_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史成交查询']"))
    )
    Historical_transaction_inquiry.click()
    print("成功进入历史成交查询页面")
    time.sleep(5)

    # 点击当日持单明细查询按钮
    Daily_transaction_details_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='当日持单明细查询']"))
    )
    Daily_transaction_details_inquiry.click()
    print("成功进入当日持单明细查询页面")
    time.sleep(5)

    # 点击历史到期意向查询按钮
    Historical_expiration_intention_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史到期意向查询']"))
    )
    Historical_expiration_intention_inquiry.click()
    print("成功进入历史到期意向查询页面")
    time.sleep(5)

    # 点击历史提前交收查询按钮
    Historical_early_settlement_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史提前交收查询']"))
    )
    Historical_early_settlement_inquiry.click()
    print("成功进入历史提前交收查询页面")
    time.sleep(5)

    # 点击历史持单汇总查询按钮
    Historical_order_summary_query = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史持单汇总查询']"))
    )
    Historical_order_summary_query.click()
    print("成功进入历史持单汇总查询页面")
    time.sleep(10)

    # 点击商品查询按钮
    Product_search = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='商品查询']"))
    )
    Product_search.click()
    print("成功进入商品查询页面")
    time.sleep(5)

    # 点击成交统计按钮
    Transaction_statistics = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='成交统计']"))
    )
    Transaction_statistics.click()
    print("成功进入成交统计页面")
    time.sleep(5)

    # 点击提前交收摘单历史列表按钮
    Early_settlement_pick_list_history = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='提前交收摘单历史列表']"))
    )
    Early_settlement_pick_list_history.click()
    print("成功进入提前交收摘单历史列表页面")
    time.sleep(5)

    # 点击历史到期意向申报查询按钮
    Historical_maturity_intention_declaration_inquiry = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='历史到期意向申报查询']"))
    )
    Historical_maturity_intention_declaration_inquiry.click()
    print("成功进入历史到期意向申报查询页面")
    time.sleep(5)

    # 点击最后交易日持单查询按钮
    Query_for_holding_positions_on_the_last_trading_day = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='最后交易日持单查询']"))
    )
    Query_for_holding_positions_on_the_last_trading_day.click()
    print("成功进入最后交易日持单查询页面")
    time.sleep(5)

except Exception as e:
    print(f"操作失败：{str(e)}")
    traceback.print_exc()

finally:
    driver.quit()
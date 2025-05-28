from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("https://center-uat2.tjpgx.cn/system/login.htm")
    driver.maximize_window()

    # 输入账号密码
    account_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "account"))
    )
    account_input.send_keys("xt")

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("1234567a")

    # 点击登录按钮
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@onclick='doLogin()']"))
    )
    login_button.click()
    print("成功登录系统")

    # 向右切换三次
    right_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "subsystem_right"))
    )
    for _ in range(3):
        right_button.click()
        time.sleep(1)
        print(f"已向右切换第 {_ + 1} 次")

    # 进入采销通页面
    order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '采销通')]"))
    )
    order_button.click()
    print("成功进入采销通页面")

    # 进入商品管理页面
    ctbasegoods_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='商品管理'][name*='ctbasegoods']"))
    )
    ctbasegoods_button.click()
    print("成功进入商品管理页面")

    # 切换到第一个 iframe
    first_iframe = WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[src^='https://pspms-uat2.tjpgx.cn/base/ctbasegoods']"))
    )
    print("成功切换到第一个 iframe")

    # 切换到第二个 iframe
    second_iframe = WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[src*='/ctbasegoodsinit/list.htm']"))
    )
    print("成功切换到第二个 iframe")

    try:
        # 显式等待并获取所有符合条件的元素
        buttons = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//a[contains(@href, "view") and text()="详情"]')
            )
        )

        # 点击第一个找到的符合条件的按钮
        if buttons:
            # 滚动到元素可见（应对遮挡问题）
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[0])

            # 带重试机制的点击  定位按钮位置，从0开始
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(buttons[0])
            ).click()

            print("成功点击第一个详情按钮，进入商品详情页")
        else:
            print("未找到符合条件的详情按钮")

        time.sleep(3)

    except Exception as e:
        print(f"操作失败: {str(e)}")

    try:
        return_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "btn1"))
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'end', inline: 'nearest'});",
            return_button
        )
        time.sleep(0.5)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "btn1"))
        ).click()
        print("返回按钮点击成功,返回商品管理页面")
        time.sleep(3)

    except Exception as e:
        print(f"操作失败: {str(e)}")

except Exception as e:
        print(f"操作失败: {str(e)}")

finally:
    driver.switch_to.default_content()
    driver.quit()
    print("浏览器已关闭")
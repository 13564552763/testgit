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

    # 点击切换菜单【向右】
    try:
        right_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "subsystem_right"))
        )

        # 向右切换三次
        for _ in range(3):
            right_button.click()
            time.sleep(1)  # 等待切换完成
            print(f"已向右切换第 {_ + 1} 次")

    except Exception as e:
        print("操作失败:", e)

    # 等待登录完成后的页面加载
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '采销通')]"))
    )

    # 点击订单交易按钮
    order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '采销通')]"))
    )
    order_button.click()
    print("成功进入采销通页面")

    # 点击商品管理按钮
    ctbasegoods_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='商品管理'][name*='ctbasegoods'][uniq='15716']"))
    )
    ctbasegoods_button.click()
    print("成功进入商品管理页面")

    # 切换到第一个 iframe
    first_iframe = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[src='https://pspms-uat2.tjpgx.cn/base/ctbasegoods.htm']")
        )
    )
    driver.switch_to.frame(first_iframe)
    print("成功切换到第一个 iframe")

    # 点击下一交易日生效按钮
    tab_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.tab[tab='tab_2'][tab_src*='ctbasegoods/list.htm']"))
    )
    tab_element.click()
    print("成功进入下一交易日生效页面")

    # 切换到第二个 iframe
    second_iframe = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[src='https://pspms-uat2.tjpgx.cn/base/ctbasegoods/list.htm']")
        )
    )
    driver.switch_to.frame(second_iframe)
    print("成功切换到第二个 iframe")

    # 点击新增按钮
    add_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.bt_add[href='https://pspms-uat2.tjpgx.cn/base/ctbasegoods/add.htm']")
        )
    )
    add_button.click()
    print("成功打开商品新增页面")

    # 点击参照商品信息
    goods_selector = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "templateGoodsCode"))
    )
    goods_selector.click()
    print("成功打开选择参照商品页面")

    # 切换到第三层 iframe
    try:
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)

        # 定位并切换到第三个 iframe
        third_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src*='goodsReference.htm']")  # 使用模糊匹配
            )
        )
        print("成功切换到第三个 iframe")

        # 选择参数商品
        select_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@onclick, '压力测试专用25年12月下') and text()='选择']")
            )
        )
        select_button.click()
        print("成功选择商品压力测试专用25年12月下")

    except Exception as e:
        print(f"切换到第三个 iframe 失败：{str(e)}")
        raise

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 等待商品代码输入框加载完成，并输入商品代码
        goods_code_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "goodsCode"))
        )
        goods_code_input.clear()  # 清空输入框
        goods_code_input.send_keys("Automation01")
        print("成功输入商品代码")

        # 等待商品名称输入框加载完成，并输入商品名称
        goods_name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "goodsName"))
        )
        goods_name_input.clear()  # 清空输入框
        goods_name_input.send_keys("自动化01")
        print("成功输入商品名称")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 点击触发下拉框展开
        driver.find_element(By.ID, "nDay").click()

        # 定位并点击「当日定转」选项
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='允许']"))
        ).click()
        print("成功选择 允许当日定转")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 点击触发下拉框展开
        driver.find_element(By.ID, "isDailyDelivery").click()

        # 定位并点击「提前交收」选项
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='允许']"))
        ).click()
        print("成功选择 允许提前交收")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 点击触发下拉框展开
        driver.find_element(By.ID, "deliveryType").click()

        # 定位并点击「线下交收」选项
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='线下交收']"))
        ).click()
        print("成功选择线下交收")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 点击触发下拉框展开
        driver.find_element(By.ID, "settleType").click()

        # 定位并点击「线下结算」选项
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='线下结算']"))
        ).click()
        print("成功选择结算方式")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 定位上市日期输入框
        date_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "validDate"))
        )

        # 点击输入框触发上市日期选择器
        driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        date_input.click()
        print("成功触发日期控件弹出")

        # 定位并切换到第四个 iframe
        four_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src*='My97DatePicker.html']")  # 使用模糊匹配
            )
        )
        print("成功切换到第四个 iframe")

        # 定位上市日期选择器元素
        # 等待上市上市日期选择器完全加载
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Wselday"))
        )

        # 选择指定日期
        # 定位目标日期元素
        target_date = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, "dpOkInput"))
        )
        # 点击选择上市日期
        target_date.click()
        print("成功选择上市日期")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 定位最后交易日期输入框
        date_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "invalidDate"))
        )

        # 点击输入框触发最后交易日期选择器
        driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        date_input.click()
        print("成功触发最后交易日期控件弹出")

        # 定位并切换到第四个 iframe
        four_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src*='My97DatePicker.html']")  # 使用模糊匹配
            )
        )
        print("成功切换到第四个 iframe")

        # 选择指定日期
        # 定位目标日期元素
        target_date = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, "dpOkInput"))
        )
        # 点击选择最后交易日期
        target_date.click()
        print("成功选择最后委托日期")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 定位交收开始日期输入框
        date_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "deliveryBeginDate"))
        )

        # 点击输入框触发交收开始日期选择器
        driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        date_input.click()
        print("成功触发交收开始日期控件弹出")

        # 定位并切换到第四个 iframe
        four_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src*='My97DatePicker.html']")  # 使用模糊匹配
            )
        )
        print("成功切换到第四个 iframe")

        # 选择指定日期
        # 定位目标日期元素
        target_date = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, "dpOkInput"))
        )
        # 点击选择交收开始日期
        target_date.click()
        print("成功选择交收开始日期")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 定位交收结束日期输入框
        date_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "deliveryEndDate"))
        )

        # 点击输入框触发交收结束日期选择器
        driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        date_input.click()
        print("成功触发交收结束日期控件弹出")

        # 定位并切换到第四个 iframe
        four_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src*='My97DatePicker.html']")  # 使用模糊匹配
            )
        )
        print("成功切换到第四个 iframe")

        # 选择指定日期
        # 定位交收结束日期日期元素
        target_date = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, "dpOkInput"))
        )
        # 点击选择交收结束日期
        target_date.click()
        print("成功选择交收结束日期")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 定位双向持单截止日期输入框
        date_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "expireDate"))
        )

        # 点击输入框触发双向持单截止日期选择器
        driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        date_input.click()
        print("成功触发双向持单截止日期日期控件弹出")

        # 定位并切换到第四个 iframe
        four_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src*='My97DatePicker.html']")  # 使用模糊匹配
            )
        )
        print("成功切换到第四个 iframe")

        # =================== 选择指定日期 ===================
        # 定位双向持单截止日期元素（2025年4月29日）
        target_date = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, "dpOkInput"))
        )
        # 点击选择双向持单截止日期
        target_date.click()
        print("成功选择双向持单截止日期")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 点击行纪服务商信息
        Brokerage_service_provider = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "brokerAccountNo"))
        )
        Brokerage_service_provider.click()
        print("成功打开选择行纪服务商信息页面")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)

        # 定位并切换到第五个 iframe（使用更宽松的 CSS 选择器）
        five_iframe = WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//iframe[contains(@src, 'userTypeChooseReference.htm')]")  # 使用模糊匹配
            )
        )
        print("成功切换到第五个 iframe")

        # 选择行纪服务商参数
        select_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='选择' and contains(@onclick, 'zhangyue-hangji')]")
            )
        )

        # 点击操作
        select_button.click()
        print("成功选择行纪服务商 买方测试")

    except Exception as e:
        print(f"切换到第五个 iframe 失败：{str(e)}")
        raise  # 抛出异常以便外部捕获

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 定位并点击保存按钮
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@class="button-s4" and normalize-space()="保 存"]')
            )
        )
        save_button.click()
        print("成功点击保存按钮")

    except Exception as e:
        print(f"操作失败: {str(e)}")
        driver.save_screenshot("error.png")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)

        # 定位并点击按钮
        confirm_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(@class, "aui_strongButton") and normalize-space()="确定"]')
            )
        )
        confirm_button.click()
        print("成功点击确定按钮")

    except Exception as e:
        print(f"操作失败: {str(e)}")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)
        driver.switch_to.frame(second_iframe)

        # 显式等待并点击
        back_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'button-s10') and text()='返回']")
            )
        )
        back_button.click()
        print("成功点击返回按钮")
        time.sleep(3)

    except Exception as e:
        print(f"操作失败: {str(e)}")

finally:
    # 返回主文档并关闭浏览器
    driver.switch_to.default_content()
    driver.quit()
    print("浏览器已关闭")

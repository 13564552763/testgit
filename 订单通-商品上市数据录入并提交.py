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
            (By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '订单交易')]"))
    )

    # 点击订单交易按钮
    order_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@onclick, 'menuV2.htm') and contains(text(), '订单交易')]"))
    )
    order_button.click()
    print("成功进入订单交易页面")

    # 点击商品管理按钮
    ctbasegoods_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='商品管理'][name*='ctbasegoods'][uniq='14996']"))
    )
    ctbasegoods_button.click()
    print("成功进入商品管理页面")

    # 切换到第一个 iframe
    first_iframe = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe[src='https://ctms-uat2.tjpgx.cn/base/ctbasegoods.htm']")
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
            (By.CSS_SELECTOR, "iframe[src='https://ctms-uat2.tjpgx.cn/base/ctbasegoods/list.htm']")
        )
    )
    driver.switch_to.frame(second_iframe)
    print("成功切换到第二个 iframe")

    try:
        # 显式等待并获取所有符合条件的元素
        buttons = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//a[contains(@href, "doSubmitCompanyListing") and text()="上市"]')
            )
        )

        # 点击第一个找到的符合条件的按钮
        if buttons:
            # 滚动到元素可见（应对遮挡问题）
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[0])

            # 带重试机制的点击
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(buttons[0])
            ).click()

            print("成功点击第一个上市按钮")
        else:
            print("未找到符合条件的上市按钮")

    except Exception as e:
        print(f"操作失败: {str(e)}")

    # 点击交易节设置勾选框按钮
    go_public = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[type="checkbox"][name="phaseUniqueCode_all"]')
        )
    )
    go_public.click()
    print("成功勾选交易节设置日期")

#基础订货量设置
    # 输入商品总订货量(批)
    totalAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.totalAmount"))
    )
    totalAmount.clear()
    totalAmount.send_keys("1000")
    print("成功输入商品总订货量(批)")

    # 输入客户最大净订货量(批)
    netAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.netAmount"))
    )
    netAmount.clear()
    netAmount.send_keys("200")
    print("成功输入客户最大净订货量(批)")

    # 输入客户最大双边订货量(批)
    amountAll = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.amountAll"))
    )
    amountAll.clear()
    amountAll.send_keys("500")
    print("成功输入客户最大双边订货量(批)")

    # 输入最大单边订货量(批)
    unilateralAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.unilateralAmount"))
    )
    unilateralAmount.clear()
    unilateralAmount.send_keys("200")
    print("成功输入最大单边订货量(批)")

    # 输入单笔买订立量(批)
    openLongAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.openLongAmount"))
    )
    openLongAmount.clear()
    openLongAmount.send_keys("100")
    print("成功输入单笔买订立量(批)")

    # 输入单笔卖订立量(批)
    openShortAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.openShortAmount"))
    )
    openShortAmount.clear()
    openShortAmount.send_keys("100")
    print("成功输入单笔卖订立量(批)")

    # 输入单笔买转让量(批)
    closeShortAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.closeShortAmount"))
    )
    closeShortAmount.clear()
    closeShortAmount.send_keys("100")
    print("成功输入单笔买转让量(批)")

    # 输入单笔卖转让量(批)
    closeLongAmount = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseOrderLimit.closeLongAmount"))
    )
    closeLongAmount.clear()
    closeLongAmount.send_keys("100")
    print("成功输入单笔卖转让量(批)")

# 交易基础设置
    # 手续费设置
      # 输入买订立(%)
    openLongRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.openLongRatio"))
    )
    openLongRatio.clear()
    openLongRatio.send_keys("10")
    print("成功输入买订立(%)")

      # 输入卖订立(%)
    openShortRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.openShortRatio"))
    )
    openShortRatio.clear()
    openShortRatio.send_keys("12")
    print("成功输入卖订立(%)")

      # 输入当天买转让(元)
    closeShortFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.closeShortFixing"))
    )
    closeShortFixing.clear()
    closeShortFixing.send_keys("13")
    print("成功输入当天买转让(元)")

      # 输入当天卖转让(元)  历史买转让(%)
    closeLongFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.closeLongFixing"))
    )
    closeLongFixing.clear()
    closeLongFixing.send_keys("14")
    print("成功输入当天卖转让(元)")

      # 输入历史买转让(%)
    closeShortHisRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.closeShortHisRatio"))
    )
    closeShortHisRatio.clear()
    closeShortHisRatio.send_keys("15")
    print("成功输入历史买转让(%)")

      # 输入历史卖转让(%)
    closeLongHisRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.closeLongHisRatio"))
    )
    closeLongHisRatio.clear()
    closeLongHisRatio.send_keys("16")
    print("成功输入历史卖转让(%)")

      # 输入当天买代为转让(元)
    forceCloseShortFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.forceCloseShortFixing"))
    )
    forceCloseShortFixing.clear()
    forceCloseShortFixing.send_keys("17")
    print("成功输入当天买代为转让(元)")

      # 输入当天卖代为转让(元)  历史买代为转让(%)
    forceCloseLongFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.forceCloseLongFixing"))
    )
    forceCloseLongFixing.clear()
    forceCloseLongFixing.send_keys("18")
    print("成功输入当天卖代为转让(元)")

      # 输入历史买代为转让(%)
    forceCloseHisShortRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.forceCloseHisShortRatio"))
    )
    forceCloseHisShortRatio.clear()
    forceCloseHisShortRatio.send_keys("19")
    print("成功输入历史买代为转让(%)")

      # 输入历史卖代为转让(%)
    forceCloseHisLongRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.forceCloseHisLongRatio"))
    )
    forceCloseHisLongRatio.clear()
    forceCloseHisLongRatio.send_keys("20")
    print("成功输入历史卖代为转让(%)")

    # 履约定金设置
      # 输入买方历史持单履约定金固定值(元)
    longMarginFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.longMarginFixing"))
    )
    longMarginFixing.clear()
    longMarginFixing.send_keys("21")
    print("成功输入买方历史持单履约定金固定值(元)")

      # 输入卖方历史持单履约定金固定值(元)
    shortMarginFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.shortMarginFixing"))
    )
    shortMarginFixing.clear()
    shortMarginFixing.send_keys("22")
    print("成功输入卖方历史持单履约定金固定值(元)")

      # 输入买方当日订立履约定金百分比(%)
    longTempMarginRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.longTempMarginRatio"))
    )
    longTempMarginRatio.clear()
    longTempMarginRatio.send_keys("23")
    print("成功输入买方当日订立履约定金百分比(%)")

      # 输入卖方当日订立履约定金百分比(%)
    shortTempMarginRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseTradeRate.shortTempMarginRatio"))
    )
    shortTempMarginRatio.clear()
    shortTempMarginRatio.send_keys("24")
    print("成功输入卖方当日订立履约定金百分比(%)")

# 交收基础设置
    # 输入买方交收手续费(元)
    longDeliveryFeeFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseDeliveryRate.longDeliveryFeeFixing"))
    )
    longDeliveryFeeFixing.clear()
    longDeliveryFeeFixing.send_keys("25")
    print("成功输入买方交收手续费(元)")

    # 输入卖方交收手续费(元)
    shortDeliveryFeeFixing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseDeliveryRate.shortDeliveryFeeFixing"))
    )
    shortDeliveryFeeFixing.clear()
    shortDeliveryFeeFixing.send_keys("26")
    print("成功输入卖方交收手续费(元)")

    # 输入买方交收履约定金(%)
    longDeliveryMarginRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseDeliveryRate.longDeliveryMarginRatio"))
    )
    longDeliveryMarginRatio.clear()
    longDeliveryMarginRatio.send_keys("27")
    print("成功输入买方交收履约定金(%)")

    # 输入卖方交收履约定金(%)
    shortDeliveryMarginRatio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "baseDeliveryRate.shortDeliveryMarginRatio"))
    )
    shortDeliveryMarginRatio.clear()
    shortDeliveryMarginRatio.send_keys("28")
    print("成功输入卖方交收履约定金(%)")

# 价格参数设置
    # 定位涨跌幅算法下拉框后点击展开
    driver.find_element(By.ID, "goodsPriceConfig.priceRule").click()

    # 直接定位百分比选项点击
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//option[text()="百分比"]'))
    ).click()
    print("成功选择百分比")

    # 输入涨幅限制
    priceUpLimit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "goodsPriceConfig.priceUpLimit"))
    )
    priceUpLimit.clear()
    priceUpLimit.send_keys("5")
    print("成功输入涨幅限制")

    # 输入跌幅限制
    priceDownLimit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "goodsPriceConfig.priceDownLimit"))
    )
    priceDownLimit.clear()
    priceDownLimit.send_keys("5")
    print("成功输入跌幅限制")

    # 下拉选择收盘价格算法
    driver.find_element(
        By.XPATH,'//select[@id="closePriceRule"]/option[contains(text(), "当日结算价")]'
    ).click()

    # 下拉选择结算价算法
    driver.find_element(
        By.XPATH, '//select[@id="settPriceRule"]/option[contains(text(), "每日最后N分钟加权平均,若无成交取全天加权平均")]'
    ).click()

    # 输入结算价算法N值
    settRuleExtent = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "settRuleExtent"))
    )
    settRuleExtent.clear()
    settRuleExtent.send_keys("3")
    print("成功输入结算价算法N值")

    # 下拉选择交收结算价算法
    driver.find_element(
        By.XPATH, '//select[@id="deliverySettPriceRule"]/option[contains(text(), "商品最后N个交易日交易结算价算术平均值")]'
    ).click()

    # 输入交收结算价算法N值
    deliverySettRuleExtent = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "deliverySettRuleExtent"))
    )
    deliverySettRuleExtent.clear()
    deliverySettRuleExtent.send_keys("3")
    print("成功输入交收结算价算法N值")

    submit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="提交审核"]'))
    )
    submit_btn.click()
    print("成功点击提交审核")

    try:
        # 先返回到默认顶层框架，确保后续定位不受嵌套影响
        driver.switch_to.default_content()
        driver.switch_to.frame(first_iframe)

        # 定位并点击按钮
        confirm_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'aui_strongButton') and normalize-space()='确定']")
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

    except Exception as e:
        print(f"操作失败: {str(e)}")

except Exception as e:
        print(f"操作失败: {str(e)}")

finally:
    # 返回主文档并关闭浏览器
    driver.switch_to.default_content()
    driver.quit()
    print("浏览器已关闭")
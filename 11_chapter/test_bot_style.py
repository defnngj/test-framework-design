from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from design_patterns.bot_style import ActionBot


driver = Chrome()
driver.get("https://cn.bing.com")

# 调用 ActionBot类
action_bot = ActionBot(driver)
action_bot.type(By.ID, "sb_form_q", text="bot style tests")
action_bot.click(By.ID, "search_icon", times=1)

driver.quit()

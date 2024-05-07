# poium_page.py
from poium import Page, Element, Elements


class BingPage(Page):
    """bing 搜索页面"""
    search_input = Element("#sb_form_q", describe="bing搜索输入框")
    search_icon = Element("#search_icon", describe="bing搜索输入框")
    search_result = Elements("//h2/a", describe="搜索结果")


class CalculatorPage(Page):
    """Android(华为) 默认计算器"""
    number_1 = Element(id_="com.huawei.calculator:id/digit_1")
    number_2 = Element(id_="com.huawei.calculator:id/digit_2")
    add = Element(id_="com.huawei.calculator:id/op_add")
    eq = Element(id_="com.huawei.calculator:id/eq")

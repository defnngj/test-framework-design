# spf_page.py
from seleniumpagefactory.Pagefactory import PageFactory


class BingPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.highlight = True

    # 使用PageFactory定义定位器字典
    locators = {
        "searchInput": ('ID', 'sb_form_q'),
        "searchIcon": ('ID', 'search_icon'),
    }

    def search(self, text):
        """
        Bing search
        """
        self.searchInput.set_text(text)
        self.searchIcon.click_button()

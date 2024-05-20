import seldom


class WebTest(seldom.TestCase):

    def test_bing_search(self):
        """
        bing web search
        """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.assertTitle("seldom - 搜索")


if __name__ == '__main__':
    seldom.main(browser="chrome")

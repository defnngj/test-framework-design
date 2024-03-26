from common import case


class MyTest(case.TestCase):

    def test_case(self):
        self.open("https://www.selenium.dev/")
        self.assertTitle("Selenium")
        self.assertInTitle("Se")
        self.assertUrl("https://www.selenium.dev/")
        self.assertInText("Selenium automates browsers. That's it!")
        self.assertElement(css="#main_navbar > ul > li:nth-child(3) > a")


if __name__ == '__main__':
    case.main()

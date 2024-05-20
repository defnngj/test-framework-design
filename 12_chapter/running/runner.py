import json
import unittest

from running.loader_extend import MyTestLoader


class TestMain:
    """
    TestMain tests class.
    1. Collect use case information and return to the list
    2. Execute the use cases based on the use case list
    """
    TestSuits = []

    def __init__(self, path: str = None):
        """
        runner test case
        :param path:
        """
        self.path = path
        if path is None:
            raise FileNotFoundError("Specify a file path")

        self.TestSuits = MyTestLoader().discover(start_dir=self.path)

    @staticmethod
    def run(suits):
        """
        run test case
        """
        runner = unittest.TextTestRunner()
        runner.run(suits)

    @staticmethod
    def collect_cases(is_json: bool = False):
        """
        Return the collected case information.
        MyTestLoader.collectCaseInfo = True
        :param is_json: Return JSON format
        """
        cases = MyTestLoader.collectCaseList

        if is_json is True:
            return json.dumps(cases, indent=2, ensure_ascii=False)

        return cases

    def _load_testsuite(self):
        """
        load test suite and convert to mapping
        """
        mapping = {}

        for suits in self.TestSuits:
            for cases in suits:
                if isinstance(cases, unittest.suite.TestSuite) is False:
                    continue

                for case in cases:
                    file_name = case.__module__
                    class_name = case.__class__.__name__

                    key = f"{file_name}.{class_name}"
                    if mapping.get(key, None) is None:
                        mapping[key] = []

                    mapping[key].append(case)

        return mapping

    def run_cases(self, data: list):
        """
        run list case
        :param data: test case list
        """
        if isinstance(data, list) is False:
            raise TypeError("Use cases must be lists.")

        if len(data) == 0:
            raise ValueError("There are no use cases to execute")

        suit = unittest.TestSuite()

        case_mapping = self._load_testsuite()
        for d in data:
            d_file = d.get("file", None)
            d_class = d.get("class").get("name", None)
            d_method = d.get("method").get("name", None)
            if (d_file is None) or (d_class is None) or (d_method is None):
                raise NameError("""Use case format error""")

            cases = case_mapping.get(f"{d_file}.{d_class}", None)
            if cases is None:
                continue

            for case in cases:
                method_name = str(case).split(" ")[0]
                if method_name == d_method:
                    suit.addTest(case)

        self.run(suit)


main = TestMain

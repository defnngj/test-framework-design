# tools/scaffolding.py
import os

import click


@click.command()
@click.option("-P", "--project", help="指定自动化项目名称。")
def main(project):
    """自动化测试脚手架工具."""
    if project:
        create_scaffold(project)
        return 0


def create_scaffold(project_name: str) -> None:
    """
    创建指定项目名称的脚手架。
    :param project_name:  项目名称
    :return:
    """

    if os.path.isdir(project_name):
        print(f"Folder {project_name} exists, please specify a new folder name.")
        return

    print(f"Start to create new test project: {project_name}")
    print(f"CWD: {os.getcwd()}\n")

    def create_folder(path: str):
        """
        创建目录
        :param path: 路径
        :return:
        """
        os.makedirs(path)
        print(f"created folder: {path}")

    def create_file(path: str, file_content: str = ""):
        """
        创建文件
        :param path: 路径
        :param file_content: 文件内容
        :return:
        """
        with open(path, 'w', encoding="utf-8") as py_file:
            py_file.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    # 测试用例模板
    test_sample = '''import unittest


class MyTest(unittest.TestCase):

    def test_case(self):
        self.assertEqual(2+2, 4)


if __name__ == '__main__':
    unittest.main()

'''

    # 运行测试脚本
    run = '''import unittest

suit = unittest.defaultTestLoader.discover("test_dir", "test_*.py")

runner = unittest.TextTestRunner()
runner.run(suit)

'''
    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_folder(os.path.join(project_name, "test_data"))
    create_file(os.path.join(project_name, "test_dir", "__init__.py"))
    create_file(os.path.join(project_name, "test_dir", "test_sample.py"), test_sample)
    create_file(os.path.join(project_name, "run.py"), run)


if __name__ == '__main__':
    main()

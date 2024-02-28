from jinja2 import Environment, FileSystemLoader, select_autoescape

# 加载 templates 目录
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape())

# 指定 table.html 文件
template = env.get_template("table.html")

# 准备写入数据
cases_list = [
    {"name": "test_pass", "doc": "pass case"},
    {"name": "test_skip", "doc": "skip case"},
    {"name": "test_fail", "doc": "fail case"},
    {"name": "test_error", "doc": "error case"}]

tmp = template.render(cases=cases_list)
# 保存HTML结果
with open("./result.html", "w", encoding="utf-8") as f:
    f.write(tmp)

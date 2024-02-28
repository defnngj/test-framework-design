from jinja2 import Template

template = Template("""
<html>
<body>
<h1> bobby: </h1>
{% for item in hobby %}
    <input type="checkbox" checked>{{item}}
{% endfor %}
</body>
</html>
""")
tmp = template.render(hobby=["eat", "sleep", "code"])
print(tmp)

from jinja2 import Template

template = Template('Hello {{ name }}!')
html = template.render(name='John Doe')
print(html)

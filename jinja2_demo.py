from mako.template import Template

t = Template('hello, ${name}!')

print(t.render(name='Johnny'))

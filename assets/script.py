from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_env.get_template('layout.html')

with open('wiki.md') as markdown_file:
    wiki = markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly'])

with open('config.json') as config_file:
    config = load(config_file)

with open('../index.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            description=config['description'],
            authors=config['authors'],
            wiki=wiki
        )
    )
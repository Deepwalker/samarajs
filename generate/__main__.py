import os
import yaml
import jinja2

dir_path = os.path.dirname(os.path.realpath(__file__))

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(dir_path),
    trim_blocks=True,
    lstrip_blocks=True,
    )
template = env.get_template('template.html')

meetups = yaml.load(open(os.path.join(dir_path, 'data.yaml')))['meetups']

for i, meetup in enumerate(meetups):
    if i == 0:
        meetup['filename'] = 'index.html'
        meetup['link'] = '/'
    else:
        meetup['filename'] = f'date-{meetup["date"]}.html'
        meetup['link'] = f'/{meetup["filename"]}'

for i, meetup in enumerate(meetups):
    render = template.render(**meetup, i=i, meetups=meetups)
    with open(os.path.join(dir_path, '..', meetup['filename']), 'w') as f:
        f.write(render)

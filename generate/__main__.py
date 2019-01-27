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
    render = template.render(**meetup, i=i, meetups=meetups)
    with open(os.path.join(dir_path, '..', f"date-{meetup['date']}.html"), 'w') as f:
        f.write(render)
    if not meetup['completed']:
        with open(os.path.join(dir_path, '..', "index.html"), "w") as f:
            f.write(render)

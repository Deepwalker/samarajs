import os
import yaml
import jinja2

dir_path = os.path.dirname(os.path.realpath(__file__))

env = jinja2.Environment(loader=jinja2.FileSystemLoader(dir_path))
template = env.get_template('template.html')

meetups = yaml.load(open('data.yaml'))['meetups']

for i, meetup in enumerate(meetups):
    render = template.render(**meetup, i=i, meetups=meetups)
    with open(f"date-{meetup['date']}.html", 'w') as f:
        f.write(render)
    if not meetup['completed']:
        with open("index.html", "w") as f:
            f.write(render)


# SamaraJS

### Setup

```
pip install -r frozen.txt
```

### Edit

[data](/generate/data.yaml)

[template](/generate/template.yml)

### Update static files

```
python -m generate
```

### Update on file change

Install [entr](http://eradman.com/entrproject/), then
```
find ./* | entr python -m generate
```

## For developers
You can rebuild `style.css` (and `readme.md`) from `resources.json` via Python script in Docker container:
```sh
docker-compose run -w /application python python builder.py
```

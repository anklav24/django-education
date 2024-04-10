# Env
- Windows WSL Ubuntu 22.04 LTS

# Start
```bash
source venv/bin/activate
./manage.py makemigrations && ./manage.py migrate
./manage.py runserver 0.0.0.0:9000
```

# UI
- http://127.0.0.1:9000/catalog/
# Admin UI
- http://127.0.0.1:9000/admin/

# RESTful API
- http://127.0.0.1:9000/users/
- http://127.0.0.1:9000/users/1
- http://127.0.0.1:9000/groups/
- http://127.0.0.1:9000/groups/2
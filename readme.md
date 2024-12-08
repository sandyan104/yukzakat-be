### Aktivasi VEnv
- `python -m venv venv`
- `venv\Scripts\activate`
### Install Library
- `python install -r requirements.txt`
### Menambah App
- `python manage.py startapp {app_name} api/{app_name}`
- Tambahkan `'api.{app_name}'` di `INSTALLED_APPS settings.py`
### Database
- Buat database dengan nama `yukzakat` di phpmyadmin
- `py manage.py makemigrations`
- `py manage.py migrate` jika ada perubahan dan perlu migrate ulang
### Run
- `python manage.py runserver`

##### Jangan lupa tambahkan folder `__pycache__` dan migrations pada app yang baru dibuat ke dalam file `.gitignore`
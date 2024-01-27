<div align="center">
<h1>Task Management</h1>
DRF Project
<br>
<br>
<div style="text-align: center;">
  <div style="display: inline-block; text-align: left; border: 1px solid #ddd; padding: 20px; border-radius: 5px; width: 70%;">
   
      DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }

  </div>
</div>




Migrate Database

```bash
python manage.py make migrations
```

```bash
python manage.py migrate
```

python manage.py runserver
```

-   Open the browser and go to http://127.0.0.1:8000/

-   To access the admin panel, go to http://127.0.0.1:8000/admin/

-   Login with the following credentials:

    -   Username: `admin`
    -   Password: `admin`




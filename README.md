# [Django Admin Argon](https://github.com/app-generator/django-admin-argon-dashboard) `playground`

Minimal **Django** project with `Docker` support - actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

> Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Docker`
- ✅ Theme: [Django Admin Argon](https://github.com/app-generator/django-admin-argon-dashboard)

<br />

## ✨ Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/django-argon-theme-playground.git
$ cd django-argon-theme-playground
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-argon-theme-playground.git
$ cd django-argon-theme-playground
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
 [Django Admin Argon](https://github.com/app-generator/django-admin-argon-dashboard) `playground` - Minimal **Django** core provided by **[AppSeed](https://appseed.us/)**

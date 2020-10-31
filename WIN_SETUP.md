# Windows Development Setup

The easiest way to setup for local development in windows is
to use Visual Studio Code and powershell. (currently) :sparkles:

1. Clone down the repository by preferred method.
```ps
PS> git clone https://github.com/ollydevulder/thingreview.git
```

2. Create a virtual environment for python and start it.
```ps
PS> python -m venv venv
PS> .\venv\Scripts\Activate.ps1
(venv) PS>
```

3. Install requirements. This will most likely fail but don't be
   concerned. Just ensure that `whitenoise` does get installed.
```ps
(venv) PS> pip install -r .\requirements.txt
(venv) PS> pip install whitenoise
```

4. Migrate the migrations and make a superuser.
```ps
(venv) PS> python .\manage.py migrate
(venv) PS> python .\manage.py createsuperuser
```

5. Collect static files.
```ps
(venv) PS> python .\manage.py collectstatic [--noinput]
```

6. Test and run development server.
```ps
(venv) PS> python .\manage.py test
(venv) PS> python .\manage.py runserver
```

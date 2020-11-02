# Thing Review
A web app that lets people review things.
Hosted by heroku at [thingreview.xyz](https://thingreview.xyz).

### Contributors
* [@ollydevulder](https://github.com/ollydevulder) (owner)
* [@physi3](https://github.com/physi3)

## Setup
1. Clone repository
```bash
$ git clone https://github.com/ollydevulder/thingreview.git
```

2. Create python virtual environment (and start it)
```bash
$ python -m venv venv
$ source venv/bin/activate
```

3. Install requirements
```bash
(venv) $ make install
```

4. Migrate database
```bash
(venv) $ make migrate
```

5. Create superuser
```bash
(venv) $ make superuser
```

6. Collect static files
```bash
(venv) $ make collectstatic
```

7. Test and run the development server :sparkles:
```bash
(venv) $ make test
(venv) $ make
```

If you are using windows, follow [this guide](WIN_SETUP.md).

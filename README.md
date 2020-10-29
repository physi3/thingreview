# Thing Review

An idea by me.

Hosted by heroku at [thingreview.xyz](https://thingreview.xyz).

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
6. Test and run the development server :sparkles:
```bash
(venv) $ make
```

If you are using windows, follow [this guide](WIN_SETUP.md).
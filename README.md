# Ticket Dashboard

## Setup

1. `git clone … && cd ticket_dashboard`
2. Create `.env` from the template above.
3. `python3 -m venv venv && source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python bot.py`  # runs the Discord listener
7. `python manage.py runserver`

Visit `http://localhost:8000/` and login via Discord.

## Deployment

- Run Django with Gunicorn / your WSGI server.
- Run `bot.py` as a systemd service or background process.

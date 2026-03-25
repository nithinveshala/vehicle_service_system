# Vehicle Service Booking System

This project is a Django-based vehicle service booking system for managing vehicles, services, and service bookings.

## CI/CD Flow

The project now includes a GitHub Actions pipeline in [`.github/workflows/cicd.yml`](C:\Users\nithi\OneDrive\Desktop\vehicle_service_system\.github\workflows\cicd.yml).

### CI stage

On every push and pull request to `main` or `master`, GitHub Actions will:

1. Install Python 3.12 and the project dependencies.
2. Check that all migrations are committed.
3. Apply migrations on a clean runner.
4. Run Django tests.
5. Run Django deployment checks.
6. Collect static files to confirm the app is build-ready.

### CD stage

On every successful push to `main` or `master`, GitHub Actions will:

1. Create a submission-ready ZIP artifact of the project source.
2. Upload that artifact in the workflow run as `vehicle-service-system-build`.

This gives you a clean CI/CD story for project submission: code is validated automatically, and a delivery package is produced from the same pipeline.

## Run Locally

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## AWS EC2 Deployment

If you are deploying with Nginx and Gunicorn on Ubuntu EC2:

1. Copy the project to `/home/ubuntu/vehicle_service_system`
2. Install dependencies and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

3. Use [gunicorn.service](C:\Users\nithi\OneDrive\Desktop\vehicle_service_system\deploy\gunicorn.service) as your systemd service template.
4. Use [nginx.conf](C:\Users\nithi\OneDrive\Desktop\vehicle_service_system\deploy\nginx.conf) as your Nginx site config.
5. Restart both services:

```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo systemctl status gunicorn
sudo journalctl -u gunicorn -n 50 --no-pager
```

#!/user/bin/env bash
# Exit immediately if any command fails
set -o errexit

#Install all Python dependecies
pip install -r requirements.txt

#Collect static files (CSS, JavaScript, Images)
python manage.py collectstatic --no-input

#Run database migrations
python manage.py migrate
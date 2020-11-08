source secret.sh
export DEPLOY=DEV
export SECRET_KEY='secretStuff!@#'
export CLEARDB_DATABASE_URL='mysql://root:password@0.0.0.0:3306/db'

python manage.py runserver 0.0.0.0:9999
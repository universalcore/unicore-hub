manage="${VENV}/bin/python ${INSTALLDIR}/${REPO}/manage.py"

$manage syncdb --noinput --no-initial-data --migrate
$manage collectstatic --noinput

sudo supervisorctl restart unicore_hub

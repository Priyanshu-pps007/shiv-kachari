echo " BUILD START"
pip3 install django==4.2.1
python manage.py collectstatic --noinput --clear
echo " BUILD END" 

echo " BUILD START"
pip3 install django
pip3 install razorpay
python manage.py collectstatic --noinput --clear
echo " BUILD END" 

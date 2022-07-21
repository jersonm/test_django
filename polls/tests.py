from django.test import TestCase
from polls.models import User
from django.utils import timezone
from datetime import datetime
from datetime import timedelta

class UserModelTest(TestCase):
    def Charge(User,monto): 
         print(User.id)
         return True

    def setUp(self):
        User.objects.create( email="test@test.com", first_name="test", last_name="test", phone="test", credit_card_token="1234", active_until="2022-07-20 10:00")
        User.objects.create( email="test1@test.com", first_name="test1", last_name="test", phone="123", credit_card_token="12341", active_until="2022-07-20 10:00")
        User.objects.create( email="test2@test.com", first_name="test2", last_name="test", phone="123", credit_card_token="", active_until="2022-07-20 10:00")
        User.objects.create( email="test3@test.com", first_name="test3", last_name="test", phone="123", credit_card_token="12342", active_until="2022-07-20 10:00")
        User.objects.create( email="test1@test.com", first_name="test1", last_name="test", phone="123", credit_card_token="121121", active_until="2022-07-22 10:00")
        User.objects.create( email="test2@test.com", first_name="test2", last_name="test", phone="123", credit_card_token="", active_until="2022-07-21 10:00")
        User.objects.create( email="test3@test.com", first_name="test3", last_name="test", phone="123", credit_card_token="12342", active_until="2022-07-21 10:00")
    
    def test_process_payments(self):
        now = datetime.now()
        enddate = now + timedelta(days=1)
        
        if enddate.day < now.day:
            if now.day == 30:
                enddate = now + timedelta(days=1)
            elif now.day == 29:
                enddate = now + timedelta(days=2)
            elif now.day == 28:
                enddate = now + timedelta(days=3)
            else: 
                enddate = now
            start_set = User.objects.filter(active_until__day__gte=now.day,active_until__day__lte=enddate.day).exclude(credit_card_token__isnull=True).exclude(credit_card_token__exact='')
            for star in start_set.iterator():
                charge = self.Charge(star)           
        else: 
            star_set = User.objects.filter(active_until__day=timezone.now().day).exclude(credit_card_token__isnull=True).exclude(credit_card_token__exact='') 
            for star in star_set.iterator():
                charge = self.Charge(star)
   

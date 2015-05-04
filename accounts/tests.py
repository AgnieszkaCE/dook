from django.test import TestCase
from accounts.forms import UserCreationForm
from cowork.forms import CompanyCreationForm, LocationCreationForm
from cowork.models import Address


class RegisterTest(TestCase):

    def setUp(self):
        Address.objects.create(street="Sandomierska",  street_numer = "100", city ="Cracow", post_numer = "27-545")

    def test_form_user(self):
        form_data = {"email": "cceellkkaa@onet.pl", "password1": "zosia12", "password2": "zosia12"}
        form = UserCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_form_company(self):
        form_data = {'name': "Zosia Company"}
        form = CompanyCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_form_location(self):
        form_data = {'address': 1, 'total_desks': 10, 'reserved_desks': 2, 'price': 100}
        form = LocationCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), True)


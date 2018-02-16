from django.test import TestCase
from .forms import *

class Setup_Class(TestCase):
    def setUp(self):
        self.post = ghnPost.objects.create(title="test this form title", description="to make sure all is well validated", link="url", photo="image")
        self.contact = Contact.objects.create(office_name="valid name of office branch", contact_number="679866532")

class Post_ghn_Form_Test(TestCase):

    # Valid Form Data
    def test_PostForm_valid(self):
        form = ghnPostForm(data={'title': "test this form title", 'description': "to make sure all is well validated", 'link': "url", 'photo': "image"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_PostForm_invalid(self):
        form = ghnPostForm(data={'title': "", 'description': "", 'link': "is not a url", 'photo': "non"})
        self.assertFalse(form.is_valid())

class Ghn_Contact_Form(TestCase):

    #valid Form Data for Contact Form
    def test_ghn_ContactForm_valid(self):
        contact = ContactForm(data={'office_name': "valid name of office branch", 'contact_number': "679866532"})
        self.assertTrue(contact.is_valid())

    # Invalid Form Data for Contact Form
    def test_ghn_ContactForm_invalid(self):
        contact = ContactForm(data={'office_name': "null", 'contact_number': "string"})
        self.assertFalse(contact.is_valid())
        

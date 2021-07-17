from django.http import response
from django.test import TestCase, Client
from django.urls import resolve, reverse

class IndexViewTestCase(TestCase):
    
    # criar alguma coisa, criamos aqui
    def setUp(self):
        client = Client()
        #testar url pelo nome
        self.url = reverse('index')
      
    # remove algo após o teste
    def tearDown(self):
        pass
    
    def test_status_code(self):
        # response = self.client.get('/')
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        
    def test_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/index.html')
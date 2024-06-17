from django.test import TestCase

class AgendaTest(TestCase):
  def setUp(self):
    self.resp= self.client.get('/')
    
    
    def teste_200_response(self):
      self.assertEqual(200, self.resp.status_code)
      
      
      def test_texto(self):
        self.assertContains(self.resp,'agenda')

from django.test import TestCase
from core.models import TarefaModel
from datetime import datetime

class AgendaTest(TestCase):
  def setUp(self):
    self.resp= self.client.get('/')
    
    
    def teste_200_response(self):
      self.assertEqual(200, self.resp.status_code)
      
      
      def test_texto(self):
        self.assertContains(self.resp,'agenda')



    class TarefaFormTest(TestCase):

    def test_tarefa_nome_unico(self):
        # Criar uma tarefa existente
        tarefa_existente = TarefaModel.objects.create(titulo="Tarefa Existente")
    

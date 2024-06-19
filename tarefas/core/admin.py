from django.contrib import admin
from core.models import TarefaModel

class TarefaModelAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'inicio', 'conclusao', 'descricao', 'categoria')
  search_fields = ('conclusao', 'titulo')


admin.site.register(TarefaModel, TarefaModelAdmin)

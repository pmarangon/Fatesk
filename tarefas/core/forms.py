from django import forms
from core.models import TarefaModel

class TarefaModelForm(forms.ModelForm):
    class Meta:
        model= TarefaModel
        fields ='__all__'
            
        
        
    
    



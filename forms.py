from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        # Substitua pelos campos do perfil que você deseja editar

        fields = {
            'campo1':'user',
            'campo2':'nome',
            'campo3':'email'

        }
 
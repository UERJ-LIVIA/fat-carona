from django import forms
from .models import Profile


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Substitua pelos campos do perfil que você deseja editar

        fields = ['name','email','password']

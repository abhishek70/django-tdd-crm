from django import forms
from leads.models import Agent


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
        widgets = {
            'user': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }

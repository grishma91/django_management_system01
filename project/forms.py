from django import forms
from .models import Project, ProjectTeam, ProjectModule
from user.models import User

Widgets = {

        
      'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'user'}),
      'description': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'description'}),
      'technology': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'technology'}),
      'estimated_time': forms.TimeInput(attrs= {'class': 'form-control', 'placeholder': 'estimated_time'}),
      'start_date': forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'start_date'}),
      'completion_date': forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'completion_date'}),
        

    }
class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields ='__all__'
        
class ProjectTeamCreationForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.filter(is_devloper=True))
    
    class Meta:
        model =ProjectTeam
        fields ='__all__'


class CreateProjectModuleForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'


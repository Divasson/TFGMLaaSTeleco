from django import forms
from .models import Project
from autenticacion.models import Usuario

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['projectName', 'archivoDatos']
    
    def clean_document(self):
        document = self.cleaned_data['archivoDatos']
        if not document.name.endswith(('.csv', '.xlsx')):
            raise forms.ValidationError('File must be a .csv or .xlsx file')
        return document
            
def handle_uploaded_file(f):
    print(f)
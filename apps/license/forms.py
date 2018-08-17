from django import forms

from apps.license.models import License

class LicenseForm(forms.ModelForm):

	class Meta:
			model = License

			fields = [
				'user',
				'company_name',
				'serial',
				'valid_date',
			]

			labels = {
				'user': 'Usuario',
				'company_name': 'Nombre Empresa',
				'serial': 'Serial',
				'valid_date': 'Fecha Validacion',	
			}

			widgets = {
				'user': forms.TextInput(attrs={'class': 'form-control'}),
				'company_name': forms.TextInput(attrs={'class': 'form-control'}),
				'serial': forms.TextInput(attrs={'class': 'form-control'}),
				'valid_date': forms.TextInput(attrs={'class': 'form-control'}),
			}
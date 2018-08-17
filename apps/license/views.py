from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.license.forms import LicenseForm
from apps.license.models import License

def index(request):
	return render(request, 'license/index.html')

def license_view(request):
	if request.method == 'POST':
		form = LicenseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('license:index')
	else:
		form = LicenseForm()
 
	return render(request, 'license/license_form.html', {'form':form})

def license_list(request):
	license = License.objects.all().order_by('id')
	contexto = {'licenses': license}
	return render(request, 'license/license_list.html', contexto)

def license_edit(request, id_license):
	license = License.objects.get(id=id_license)
	if request.method == 'GET':
		form = LicenseForm(instance=license)
	else:
		form = LicenseForm(request.POST, instance=license)
		if form.is_valid():
			form.save()
		return redirect('license:license_list')
	return render(request, 'license/license_form.html', {'form': form})

def license_delete(request, id_license):
	license = License.objects.get(id=id_license)
	if request.method == 'POST':
		license.delete()
		return redirect('license:license_list')
	return render(request, 'license/license_delete.html', {'license': license})

from rest_framework.serializers import ModelSerializer
from apps.license.models import License

class LicenseSerializer(ModelSerializer):

	class Meta:
		model = License
		fields = ('user', 'company_name', 'serial', 'valid_date')

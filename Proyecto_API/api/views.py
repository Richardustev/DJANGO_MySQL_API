from django.views import View
from django.http import JsonResponse
from .models import Company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
class CompanyView(View):
    # Decorator to exempt this view from CSRF verification
    @method_decorator(csrf_exempt)
    # This class-based view handles requests for the Company model
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Handle GET requests to retrieve all companies
    def get(self, request, id=0):
        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]  # Get the first company from the QuerySet
                data = {'message': 'Company found', 'company': company}
            else:
                data = {'message': 'Company not found'}
            return JsonResponse(data, safe=False)
        else:
            companies = Company.objects.all().values()  # This returns a QuerySet of dictionaries
            if len(companies) > 0:
                data = {'message': 'Companies found', 'companies': list(companies)}
            else:
                data = {'message': 'No companies found'}
            
            return JsonResponse(data, safe=False)

    def post(self, request):
        jd = json.loads(request.body)

        Company.objects.create(
            name=jd['name'],
            website=jd['website'],
            foundation=jd['foundation'],
        )

        data = {'message': 'success'}
        return JsonResponse(jd, safe=False)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        company = list(Company.objects.filter(id=id).values())
        if len(company) > 0:
            c = Company.objects.get(id=id)
            c.name = jd['name']
            c.website = jd['website']
            c.foundation = jd['foundation']
            c.save()

            data = {'message': 'Company updated successfully'}
        else:
            data = {'message': 'No companies found'}

        return JsonResponse(data, safe=False)
    
    def delete(self, request,id):
        company = list(Company.objects.filter(id=id).values())
        if len(company) > 0:
            Company.objects.filter(id=id).delete()
            data = {'message': 'Company deleted successfully'}
        else:
            data = {'message': 'Company not found'}
        return JsonResponse(data, safe=False)
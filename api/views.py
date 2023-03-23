from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
# Create your views here.


class HomeView(View):
    def get(self, request):
        users = User.objects.all()

        data = {
            'Users': []
        }
        for user in users:
            data['Users'].append(
                {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            )
        
        return JsonResponse(data)
    
    def post(self, request):
        return JsonResponse({"Message":"POST"})

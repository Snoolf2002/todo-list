from django.views import View
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
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

def index(request: HttpRequest) -> JsonResponse:

    if request.method == 'POST':
        decoded = request.body.decode()
        user = json.loads(decoded)

        username = user.get("username")
        password = user.get('password')

        if username == None:
            return JsonResponse({'error': "Username field is required"})
        if password == None:
            return JsonResponse({'error': "Password field is required"})
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            return JsonResponse({"message": "You are authenticated"})
        return JsonResponse({"message": "You are not authenticated"})
        
    return JsonResponse({"message": "Hey, you must send post request!"})

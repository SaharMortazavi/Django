from django.shortcuts import render
from django.http import HttpResponse
from users.models import UserProfile

# Create your views here.
def index(request):
    return HttpResponse('<em>Go to the /userpage to see the users information</em>')

def userpage(request):
    users_list=UserProfile.objects.order_by('id')
    users_info={"users_info":users_list}
    #first one is the app name=users
    return render(request,'users/userpage.html',context =users_info)

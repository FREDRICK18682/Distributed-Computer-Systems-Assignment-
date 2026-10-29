from django.shortcuts import render

# Create your views here.
#function for the chat page
def chart_Room(request):
    return render(request, 'chartRoom/chartRoom.html')

#function for the login page
def login(request):
    return render(request, 'chartRoom/login.html')

#function for the signup page
def signup(request):
    return render(request, 'chartRoom/signup.html')
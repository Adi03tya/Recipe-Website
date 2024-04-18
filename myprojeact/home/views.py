from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def about(request):

    peoples=[
        {
            'name':'John Doe',
            'email':'johndoe@gmail.com'
        },
        {
            'name':'Jane Doe',
            'email':'Janedoe@yahoo.com'
        },
        {
            'name':'stieve Smith',
            'email':'stievesmith@gamil.com'
        }
    ]

    vegetables = ['potato', 'tomato', 'cabbage', 'onion']

    return render(request, 'index.html', {'peoples':peoples , 'vegetables':vegetables})
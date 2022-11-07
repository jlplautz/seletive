from django.shortcuts import render


# Create your views here.
def nova_empresa(request):
    return render(request, 'nova_empresa.html')

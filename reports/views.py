from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login_url')
def bomView(request):
    return render(request,'bom.html')

@login_required(login_url='login_url')
def costView(request):
    return render(request,'cost.html')

@login_required(login_url='login_url')
def viView(request):
    return render(request,'vi.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required()
def demo(request):
    return render(request, 'demo.html')
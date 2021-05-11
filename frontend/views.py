from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request, ff=None):
    print(ff)
    return render(request, "frontend/index.html", {"isAuthificated": request.user.is_authenticated})

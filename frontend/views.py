from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import os
import fnmatch


def find(pattern, path):
    result = []
    for name in os.listdir(path):
        if fnmatch.fnmatch(name, pattern):
            result.append('frontend/' + name)
    return result


# Create your views here.


def index(request, ff=None):
    path_to_chunk = find('*.js', os.path.abspath('./frontend/static/frontend'))
    return render(request, "frontend/index.html", {"isAuthificated": request.user.is_authenticated, 'chunkname': path_to_chunk[0]})

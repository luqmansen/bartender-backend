import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("luqmansen.pythonanywhere.com/")
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def healtz(request):
    return HttpResponse(status=200)

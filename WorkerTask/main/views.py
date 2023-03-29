from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


# Create your views here.
def index(request):
    return render(request, "main/index.html",
                  context={"bosses": get_all_bosses()})


def generate(request):
    db_seeder()
    return HttpResponse("50000 employes was generated")


@require_POST
def worker_AJAX_RESPONSE(request):
    bid = request.POST["boss_id"]
    workers = get_worker_by_boss_id(int(bid))
    return JsonResponse(workers, safe=False)


def workers(request):
   return render(request, "main/workers.html", context={"workers":get_all_workers()})
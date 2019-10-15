from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
from .models import Images,Category,Location


def photo_today(request):
    locations = Location.objects.all()
    if request.GET.get('location'):
        photo = Images.filter_by_location(request.GET.get('location'))
    elif request.GET.get('search_term'):
        photo = Images.search_results(request.GET.get('search_term'))
    else:
        photo = Images.objects.all()
    return render(request, 'all-photo/home.html', {"photo":photo, "locations":locations})



def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "No photo found"
        return render(request, 'all-photo/search.html',{"message":message})

def picture(request,picture_id):
    try:
        picture = Images.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/photo.html", {"picture":picture})
    


    




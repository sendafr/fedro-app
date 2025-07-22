from django.shortcuts import render, HttpResponse
from .models import Video
from .forms import VideoForm

# Create your views here.
def video_home(request):
    all_videos = Video.objects.all()
    if request.method == "POST":
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("The video uploaded successfuly!")
        elif request.method == 'DELETE':
            form.delete()
            return HttpResponse("The video was deleted successfully")
    else:
        form = VideoForm()   
    return render(request, 'video/video_home.html', {'form':form, 'all':all_videos})

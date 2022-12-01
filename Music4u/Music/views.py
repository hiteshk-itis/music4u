from django.shortcuts import render
from Music.models import Collaborative_Music
from django.contrib import messages
# Create your views here.
def Postmusic(request):
    if request.method=="POST":
        title = request.POST['title']
        user_id= request.POST['user_id']
        rating= request.POST['rating']
        song_id= request.POST['song_id'] 
        music= Collaborative_Music(title=title, song_id=song_id, user_id=user_id,rating=rating)
        music.save()
        messages.success(request, "your form have been submitted")
    return render (request,"postmusic.html")
    
        

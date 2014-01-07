# Create your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from notes.models import Note
from notes.forms import *

class Notes(View):
    """class to fetch and store Notes"""
    template_name="notes.html"
    

    def get(self,request):
	ci= RequestContext(request)
	notes=Note.objects.filter(user=request.user)
	return render_to_response(self.template_name,{'notes':notes} ,ci)



class CreateNote(View):
    """create notes"""
    noteform = Noteform
    template_name="createnote.html"
    
    def get(self, request, *args, **kwargs):
	ci=RequestContext(request)
	form = self.noteform
	return render_to_response(self.template_name , {'form':form}, ci)
    
    def post(self , request , *args, **kwargs ):
        form = self.noteform(request.POST)
	if form.is_valid():
		note=form.save(commit=False)
		note.user=request.user
		note.save()
		return HttpResponseRedirect('/notes/')
		
	 
	    
		 

# Create your views here
from django.Http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from notes.models import Note

class Notes(View):
    """class to fetch and store Notes"""
    template_name="notes.html" 

    def get(self,request):
	notes=Note.objects.all()
	return render_to_response(template_name,{'notes':notes} , ci)



class Create_notes(View):
    """create notes"""
    form = noteform()
    template_name="createnote.html"
    
    def get(self, request, *args, **kwargs):
	form = self.form
	render_to_response(template_name , {'form':form}, ci)
    
    def post(self , request , *args, **kwargs ):
        form = self.form(request.POST)
	if form.is_valid():
		note=form.save(commit=False)
		note.user=request.user
		note.save()
		return HttpResponseRedirect('/notes/')
		
	 
	    
		 

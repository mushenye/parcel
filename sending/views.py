from django.shortcuts import redirect, render

from sending.forms import PersonForm

# Create your views here.

def home(request):
    return render(request, 'sending/home.html')


def person_details (request):
    if request.method == 'POST':
        form =PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("/")
        
    else:
        form=PersonForm()
    return render(request, 'sending/detailform.html',
                  context={
                      'form':form
                  }
                  )

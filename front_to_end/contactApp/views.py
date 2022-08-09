from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Ad
from .forms import ResumeForm


# Create your views here.
def contact(request):
    return render(request, 'contact.html', {
        'active_menu': 'employ',
        'sub_menu': 'contact',
    })


def recruit(request):
    AdList = Ad.objects.all().order_by('-publishDate')
    if request.method == 'POST':
        resumeForm = ResumeForm(data=request.POST, files=request.FILES)
        if resumeForm.is_valid():
            resumeForm.save()
            return render(request, 'success.html', {
                'active_menu': 'contactus',
                'sub_menu': 'recruit',
            })
    else:
        resumeForm = ResumeForm()
    return render(
        request, 'recruit.html', {
            'active_menu': 'contactus',
            'sub_menu': 'recruit',
            'AdList': AdList,
            'resumeForm': resumeForm,
        })
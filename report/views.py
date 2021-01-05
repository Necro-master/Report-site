from django.shortcuts import render, redirect
from .models import Person, Url_data
from .forms import UrlForm

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'report/person_list.html', {'persons': persons})

def url_list(request, person_id):
    try:

        urls = Url_data.objects.filter(tone=-1, person=Person.objects.get(pk=person_id))
    except Person.DoesNotExist as e:
        return redirect('person_list')
    if not urls:
        return redirect('person_list')

    if request.method == 'POST':
        if 'tone' in dict(request.POST):
            tones = dict(request.POST)['tone']
            for url, tone in zip(urls, tones):
                url.tone = tone
                url.save()
        #form = UrlForm(request.POST)
        try:
            person = Person.objects.get(pk=person_id)
        except Person.DoesNotExist:
            return redirect('person_list')

        person.status = 3
        person.save()
        return redirect('person_list')

    form = UrlForm
    return render(request, 'report/url_list.html', {'urls': urls, 'form': form})

# Create your views here.

from django.shortcuts import render
import requests as req

def doctors(request):
    if request.GET.get('page'):
        page = request.GET.get('page')
        if page == 'http://127.0.0.1:8000/api/doctors/?format=json':
            doctorsjson = req.get(page).json()
        else:
            doctorsjson = req.get(f'http://127.0.0.1:8000/api/doctors/?format=json&page={page}').json()
    else:
        doctorsjson = req.get('http://127.0.0.1:8000/api/doctors/?format=json').json()
        
    if request.GET.get('filexp'):
        filexp = request.GET.get('filexp') 
        doctorsjson = req.get(f'http://127.0.0.1:8000/api/doctors/?experience={filexp}').json()
    
    if request.GET.get('filexpbutton'):
        doctorsjson = req.get('http://127.0.0.1:8000/api/doctors/?format=json').json()
        
    if request.GET.get('fildirection'):
        fildirection = request.GET.get('fildirection')
        try:
            idx = [i['title'].lower().strip() for i in req.get('http://127.0.0.1:8000/api/directions/?format=json').json()].index(fildirection)
            doctorsjson = req.get(f'http://127.0.0.1:8000/api/doctors/?directions={idx + 1}&format=json').json()
        except:
            pass
        
    return render(request, 'program\doctors.html', {'doctors': doctorsjson,})

def sort(request, name):
    doctorsjson = []
    try:
        directions = req.get('http://127.0.0.1:8000/api/directions/?format=json').json()

        idx = [i['title'].lower().strip() for i in directions].index(name.lower().strip())

        doctorsjson = req.get(f'http://127.0.0.1:8000/api/doctors/?directions={idx+1}&experience=&format=json').json()

        if request.GET.get('page'):
            page = request.GET.get('page')
            doctorsjson = req.get(f'http://127.0.0.1:8000/api/doctors/?directions={idx+1}&experience=&format=json&page={page}').json()
        else:
            doctorsjson = req.get(f'http://127.0.0.1:8000/api/doctors/?directions={idx+1}&experience=&format=json&page=1').json()
    except Exception as e:
        print(f"Error occurred: {e}")
    print(doctorsjson)
    return render(request, 'program/sort.html', {'sorted_doctors': doctorsjson})


def home(request):
    return render(request, 'program\home.html')

def directions(request):
    directionsjson = req.get('http://127.0.0.1:8000/api/directions/?format=json').json()
    return render(request, r'program\directions.html', {'directions': directionsjson})
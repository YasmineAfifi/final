from django.shortcuts import render
from .forms import CarForm
from .models import Car,Reserve
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import CarForm ,ReserveForm

# display home page html 
@login_required
def get_home_page(request):
     all_cars= Car.objects.all()
     return render(request ,'cars/home.html',{'cars':all_cars})

# add car function  
@login_required
def add_car(request):
    if request.method == 'POST':
        car_data = CarForm(request.POST, request.FILES)
        # print(car_data.errors)
        if car_data.is_valid():
            car_data.save()
            return redirect('home')
    else:
        car_data = CarForm()
        
    return render(request,'cars/addcar.html',{'carForm':car_data})



@login_required
def get_details(request,car_id):
    try:
        car = Car.objects.get(id=car_id)
        if request.method == 'POST':
            reserve_form = ReserveForm(request.POST)
            if reserve_form.is_valid():
                reserve_form.save()
                return redirect('reservations')
        else:
            reserve_form = ReserveForm()

        return render(request,'cars/carDetails.html',{"details":car,'reservation_form':reserve_form,"user_id":request.user.id})
    
    except Car.DoesNotExist:

        return HttpResponse('Car does not exist')
    
    
    

# delete specific object
def delete_car(request,car_id):

    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('/home')

# update the form 
@login_required
def update_car(request,car_id):

    car = Car.objects.get(id=car_id)

    if request.method =="POST":
        car_form = CarForm(request.POST, request.FILES,instance=car)
        if car_form.is_valid():
            if 'img' in request.FILES:
                car.image = request.FILES['img']
            car_form.save()
            return redirect('home')
    else:
        return render(request,"cars/updateCar.html",{'car':car})
    

@login_required
def get_reservations(request):

    all_reservations = Reserve.objects.all()

    

    return render(request,'cars/reservations.html',{"reservations":all_reservations})
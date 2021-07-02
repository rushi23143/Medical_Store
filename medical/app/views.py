from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('manage_store')
        else:
            messages.error(request, 'Wrong username and password.')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken!')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.info(request, "Successfully registered!\n login now. ")
                user.save()
                return redirect('login')
        except Exception as e:
            print(e)
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def manage_store(request):
    store_list = MedicalStore.objects.all()
    return render(request, 'manage_store.html', {'store_list':store_list})

def add_store(request):
    if request.POST:
        store_name = request.POST['storename']
        username = request.POST['username']
        password = request.POST['password']
        store_email_id = request.POST['email']
        mobile_number = request.POST['mobile']
        address_1 = request.POST['address1']
        address_2 = request.POST['address2']
        store_licence = request.POST['storelic']
        store_type_id = request.POST['storetype']
        store_type = StoreType.objects.get(id=store_type_id)
        store_registration_no = request.POST['regno']
        try:
            MedicalStore.objects.create(store_name=store_name, username=username, password=password, store_email_id=store_email_id,
            mobile_number=mobile_number, address_1=address_1, address_2=address_2, store_licence=store_licence,
            store_type=store_type, store_registration_no=store_registration_no)
            return redirect("manage_store")

        except Exception as e:
            print(e)
        
    return render(request, 'add_store.html', {'storetype':StoreType.objects.all()})

def delete_store(request, id):
    if request.method == 'POST':
        store = MedicalStore.objects.get(pk=id)
        store.delete()
    return redirect("manage_store")

def edit_store(request, id):
    store = MedicalStore.objects.get(id=id)
    storetype = StoreType.objects.all()
    return render(request, 'edit_store.html', {'store':store, 'storetype':storetype})

def update(request, id):
    try:
        store = MedicalStore.objects.get(id=id)
        store.store_name = request.POST['storename']
        store.username = request.POST['username']
        store.password = request.POST['password']
        store.store_email_id = request.POST['email']
        store.mobile_number = request.POST['mobile']
        store.address_1 = request.POST['address1']
        store.address_2 = request.POST['address2']
        store.store_licence = request.POST['storelic']
        #store.store_type = request.POST['storetype']
        store.store_type_id = request.POST['storetype']
        store.store_type = StoreType.objects.get(id=store.store_type_id)
        store.store_registration_no = request.POST['regno']
        store.save()
        return redirect("manage_store")
    except:
        return redirect("manage_store")

def manage_medicine(request):
    medicine_list = MedicineDetails.objects.all()
    return render(request, 'manage_medicine.html', {'medicine_list':medicine_list})

def add_medicine(request):
    if request.POST:
        medicine_name = request.POST['medicinename']
        medicine_details = request.POST['medicinedetails']
        medicine_price = request.POST['price']
        medicine_quantity = request.POST['quantity']
        medicine_expiry_date = request.POST['date']
        store_id = request.POST['medicinestore']
        store = MedicalStore.objects.get(id=store_id)
        medicine_type_id = request.POST['medicinetype']
        medicine_type = MedicineType.objects.get(id=medicine_type_id)
        try:
            MedicineDetails.objects.create(medicine_name=medicine_name, medicine_price=medicine_price, medicine_details=medicine_details,
            medicine_quantity=medicine_quantity, medicine_expiry_date=medicine_expiry_date, store=store, medicine_type=medicine_type)
            return redirect("manage_medicine")
        except Exception as e:
            print(e)
    return render(request, 'add_medicine.html', {'medtype':MedicineType.objects.all(), 'storename':MedicalStore.objects.all()})

def delete_medicine(request, id):
    if request.method == 'POST':
        medicine = MedicineDetails.objects.get(pk=id)
        medicine.delete()
    return redirect('manage_medicine')

def edit_medicine(request, id):
    medicine = MedicineDetails.objects.get(id=id)
    medtype = MedicineType.objects.all()
    storename = MedicalStore.objects.all()
    return render(request, 'edit_medicine.html', {'medicine':medicine, 'medtype':medtype, 'storename':storename})

def upmedicine(request, id):
    try:
        medicine = MedicineDetails.objects.get(id=id)
        medicine.medicine_name = request.POST['medicinename']
        medicine.medicine_details = request.POST['medicinedetails']
        medicine.medicine_price = request.POST['price']
        medicine.medicine_quantity = request.POST['quantity']
        medicine.medicine_expiry_date = request.POST['date']
        medicine.store_id = request.POST['medicinestore']
        medicine.store = MedicalStore.objects.get(id=medicine.store_id)
        medicine.medicine_type_id = request.POST['medicinetype']
        medicine.medicine_type = MedicineType.objects.get(id=medicine.medicine_type_id)
        #medicine.store = request.POST['medicinestore']
        #medicine.medicine_type = request.POST['medicinetype']
        medicine.save()
        return redirect("manage_medicine")
    except:
        return redirect('manage_medicine')
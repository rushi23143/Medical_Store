from django.db import models

# Create your models here.
class StoreType(models.Model):
    type_name = models.CharField(max_length=45)

    def __str__(self):
        return self.type_name

class MedicalStore(models.Model):
    store_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    store_email_id = models.EmailField(max_length=30)
    mobile_number = models.IntegerField(blank=True, null=True)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    store_licence = models.CharField(max_length=30)
    store_type = models.ForeignKey(StoreType, on_delete=models.CASCADE)
    store_registration_no = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name

class MedicineType(models.Model):
    medicine_type_name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine_type_name

class MedicineDetails(models.Model):
    medicine_name = models.CharField(max_length=60)
    medicine_details = models.CharField(max_length=100)
    medicine_price = models.IntegerField()
    medicine_quantity = models.IntegerField()
    medicine_expiry_date = models.DateField()
    store = models.ForeignKey(MedicalStore, on_delete=models.CASCADE)
    medicine_type = models.ForeignKey(MedicineType, on_delete=models.CASCADE)


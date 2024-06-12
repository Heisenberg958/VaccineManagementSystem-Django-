from django.db import models


class SlotBook(models.Model):
    name=models.CharField(max_length=300)
    center_id=models.IntegerField()
    age=models.IntegerField()
    dose_name=models.CharField(max_length=300)
    gender=models.CharField(max_length=300)
    contacts=models.CharField(max_length=300)
    id_proof_type=models.CharField(max_length=300)
    id_proof_number=models.CharField(max_length=300)
    slot_date=models.DateField(null=True)
    slot_time=models.CharField(max_length=300)
    approved=models.CharField(max_length=300)


class Certificate(models.Model):
    slotno=models.IntegerField()
    centerid=models.IntegerField()
    employeeid=models.IntegerField()
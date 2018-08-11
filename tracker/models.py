from django.db import models

# Create your models here.
class Store(models.Model):
    store_ip = models.CharField(max_length=50)
    name = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 10)
    current_weather = models.CharField(max_length=100) 
    date_created = models.DateTimeField(auto_now=True)


class CallType(models.Model):
    code = models.CharField(max_length = 100)
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length=500)


class CallSubType(models.Model):
    request_code = models.IntegerField()
    name = models.CharField(max_length = 50)
    call_id = models.ForeignKey(CallType, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

class CallerType(models.Model):
    name = models.CharField(max_length=50)

class ServiceLocation(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
class Request(models.Model):
    parent_workorder = models.CharField(max_length = 20)
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    call_type = models.ForeignKey(CallType, on_delete = models.CASCADE)
    call_subtype = models.ForeignKey(CallSubType, on_delete = models.CASCADE)
    workorder_description = models.CharField(max_length=500)
    service_locationid = models.ForeignKey(ServiceLocation, on_delete = models.CASCADE)
    report_datetime = models.DateTimeField(auto_now=True)
    reported_by = models.CharField(max_length = 200)
    requesting_contact = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    caller_type = models.ForeignKey(CallerType, on_delete = models.CASCADE)
    designation = models.CharField(max_length=100)
    local_time = models.CharField(max_length=50)

class RequestProgress(models.Model):
    request = models.ForeignKey(Request, on_delete = models.CASCADE)
    notes = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField()
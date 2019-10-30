from django.db import models
from django.contrib.postgres import fields as pgJson

# Create your models here.


class ApiRequest(models.Model):
    REQUEST_TYPE = [("GET", "get"), ("POST", "post"), ("PUT", "put"), ("DELETE", "delete")]
    request_type = models.CharField(choices=REQUEST_TYPE, max_length=16)
    request_url = models.CharField(max_length=1024)
    body = pgJson.JSONField(null=True, blank=True)
    response = pgJson.JSONField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class ApiFields(models.Model):
    field_name = models.CharField(max_length=64)
    data_type = models.CharField(max_length=16)
    optional = models.BooleanField(default=True)
    api_request = models.ForeignKey(ApiRequest, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class ApiRequestVersion(models.Model):
    api_request = models.ForeignKey(ApiRequest, on_delete=models.CASCADE)
    removed_field = models.ForeignKey(ApiFields, on_delete=models.CASCADE)
    response = pgJson.JSONField(null=True, blank=True)

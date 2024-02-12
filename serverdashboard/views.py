from django.shortcuts import render
from .models import dashboard_collection
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>App is Running</h1>")


def add_data(request):
    records = {
        "sku": "IND-EBAY-001",
        "name": "NY-Test4",
        "category": "Furniture",
        "tags": ["Amazon", "Fashion", "Furniture"],
        "stock_status": {"total_stock": 20000, "available_stock": 1050},
    }
    dashboard_collection.insert_one(records)
    return HttpResponse("Inserted Successfully")

def get_data(request):
    data = dashboard_collection.find()
    return HttpResponse(data)


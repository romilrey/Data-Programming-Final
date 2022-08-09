from django.shortcuts import  render
from forex.models import Forex
from pymongo import MongoClient
from datetime import datetime
# import requests

def connect_():
    uri = "mongodb+srv://finalprojectDP:Georgian123@finalproject.zroift8.mongodb.net/test"
    client = MongoClient(uri)
    db = client.forex
    collection = db['rates']
    return collection


# def get_rates(request):
#     print(request)
#     # date_today = datetime.now().strftime("%Y-%m-%d")
#     # collection.find({"date": date_today})
#     # return collection
#     # return render (request, 'forex/forex.html', { "all_rates": all_rates} )


def get_rates(request, date):
    data = list(connect_().find({"date": date}))
    print(data[0]['date'])
    # for key in data[0]['rates'].keys():
    max_value_key = max(data[0]['rates'], key=data[0]['rates'].get)
    print(max_value_key) 
    min_value_key = min(data[0]['rates'], key=data[0]['rates'].get)
    print(min_value_key)   

    # sorted_value = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}

    return render (
        request,
        'forex/rate_detail.html',
        {'date': data[0]['date'],
        'rates': data[0]['rates'],
        'max' :  data[0]['rates'][max_value_key],
        'min' :  data[0]['rates'][min_value_key]
        # 'sorted' : data[0][sorted_value]
        }
    )
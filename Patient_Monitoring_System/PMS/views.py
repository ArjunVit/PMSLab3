import csv
from django.shortcuts import render

def display_data(request):
    data=[]
    with open('static/patient_data.csv', 'r') as file:
        csv_data = csv.DictReader(file)
        data = list(csv_data)  # Convert CSV data to a list of dictionaries

    return render(request, 'PMS/page.html', {'data': data})




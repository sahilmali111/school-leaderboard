from django.shortcuts import render, redirect
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.templatetags.rest_framework import data

from .models import student_marks
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework.decorators import api_view
import requests


# Create your views here.

def index(request):
    callapi = requests.get('http://127.0.0.1:8000/leaderboard_api')
    results = callapi.json()

    for i in results:
        i["total"] = i["maths"] + i["chemistry"] + i["physics"]  # calculate total
        i["percentage"] = round(i["total"] / 3, 2)  # calculate percentage

    for i in range(len(results)):  # sort according to percentage
        for j in range(len(results) - 1):
            a = results[i]
            if a["percentage"] > results[j]["percentage"]:
                b = results[j]
                results[j] = a
                a = b
            results[i] = a

    for i in range(len(results)):
        results[i]["rank"] = i + 1

    max = 0
    temp = 0
    for i in range(len(results)):  # topper of physics
        if max < results[i]["physics"]:
            temp = i
            max = results[i]["physics"]
    results[temp]["maxp"] = results[temp]["physics"]
    results[temp]["namep"] = results[temp]["name"]

    temp = 0
    max = 0
    for i in range(len(results)):  # topper of chemistry
        if max < results[i]["chemistry"]:
            temp = i
            max = results[i]["chemistry"]
    results[temp]["maxc"] = results[temp]["chemistry"]
    results[temp]["namec"] = results[temp]["name"]

    temp = 0
    max = 0
    for i in range(len(results)):  # topper of maths
        if max < results[i]["maths"]:
            temp = i
            max = results[i]["maths"]
    results[temp]["maxm"] = results[temp]["maths"]
    results[temp]["namem"] = results[temp]["name"]
    return render(request, 'index.html', {'student_marks': results})


@api_view(['POST'])
def student_api(request):
    if request.method == "POST":
        saveserializer = Studentserializer(data=request.data)
        if saveserializer.is_valid():
            saveserializer.save()
            return Response(saveserializer.data, status=status.HTTP_201_CREATED)
            return Response(saveserializer.data, status=status.HTTP_400_BAD_REQUEST)
    # return render(request, 'add_data.html')


def student_data(request):
    if request.method == "POST":
        rollno = request.POST.get('rollno')
        name = request.POST.get('name')
        physics = request.POST.get('physics')
        chemistry = request.POST.get('chemistry')
        maths = request.POST.get('maths')
        if student_marks.objects.filter(rollno=rollno).count() > 0:
            return render(request, "add_data.html", {"error": "Roll number Already exist "})
        data = {'rollno': rollno, 'name': name, 'physics': physics, 'chemistry': chemistry, 'maths': maths}
        headers = {'Content-Type': 'application/json'}
        read = requests.post('http://127.0.0.1:8000/student', json=data, headers=headers)
        return redirect('leaderboard')
    else:
        return render(request, 'add_data.html')


@api_view(['GET'])
def leaderboard_api(request):
    if request.method == 'GET':
        results = student_marks.objects.all()
        serialize = Studentserializer(results, many=True)
        return Response(serialize.data)
    # return render(request, 'leaderboard.html')


def leaderboard(request):
    callapi = requests.get('http://127.0.0.1:8000/leaderboard_api')
    results = callapi.json()
    for i in results:
        i["total"] = i["maths"] + i["chemistry"] + i["physics"]  # calculate total
        i["percentage"] = round(i["total"] / 3, 2)  # calculate percentage

    for i in range(len(results)):  # sort according to percentage
        for j in range(len(results) - 1):
            a = results[i]
            if a["percentage"] > results[j]["percentage"]:
                b = results[j]
                results[j] = a
                a = b
            results[i] = a

    for i in range(len(results)):
        results[i]["rank"] = i + 1

    return render(request, 'leaderboard.html', {'student_marks': results})

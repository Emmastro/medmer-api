from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from patient.models import Patient
from patient.serializers import PatientSerializer


# Create your views here.
@csrf_exempt
def patient_list(request):
    """
    List all or create a new patient
    """
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serilizer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status(400))
        
@csrf_exempt
def patient_detail(request, pk):
    """
    Retrieve, update or delete a patient.
    """
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patient, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return HttpResponse(status=204)

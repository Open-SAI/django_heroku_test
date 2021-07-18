from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from concepto.models import Concepto
from concepto.serializers import ConceptoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'PUT', 'DELETE'])
def concepto_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        concepto = Concepto.objects.get(pk=pk) 
    except Concepto.DoesNotExist: 
        return JsonResponse({'message': 'El concepto noooooo existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        concepto_serializer = ConceptoSerializer(concepto) 
        return JsonResponse(concepto_serializer.data) 
    elif request.method == 'PUT':
        concepto_data = JSONParser().parse(request)
        concepto_serializer = ConceptoSerializer(concepto, data=concepto_data)
        if concepto_serializer.is_valid():
            concepto_serializer.save()
            return JsonResponse(concepto_serializer.data)
        return JsonResponse(concepto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        concepto.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def concepto_list_published(request):
    # GET all published tutorials
    conceptos = Concepto.objects.filter(published=True)
        
    if request.method == 'GET': 
        conceptos_serializer = ConceptoSerializer(conceptos, many=True)
        return JsonResponse(conceptos_serializer.data, safe=False)
    

@api_view(['GET', 'POST', 'DELETE'])
def concepto_list(request):
    if request.method == 'GET':
        conceptos = Concepto.objects.all()
        
        title = request.GET.get('titulo', None)
        if title is not None:
            conceptos = conceptos.filter(titulo__icontains=titulo)
        
        conceptos_serializer = ConceptoSerializer(conceptos, many=True)
        return JsonResponse(conceptos_serializer.data, safe=False)
        # 'safe=False' for objects serialization    ...
    elif request.method == 'POST':
        concepto_data = JSONParser().parse(request)
        concepto_serializer = ConceptoSerializer(data=concepto_data)
        if concepto_serializer.is_valid():
            concepto_serializer.save()
            return JsonResponse(concepto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(concepto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Concepto.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



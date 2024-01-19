from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import School
from .serializers import SchoolSerializer

# Create your views here.

# get all schools
@api_view(['GET'])
def getSchools(request):
    users = School.objects.all()
    serializer = SchoolSerializer(users, many=True)
    return Response(serializer.data)

# get single school
@api_view(['GET'])
def getSchool(request, pk):
    school = School.objects.get(id=pk)
    serializer = SchoolSerializer(school, many=True)
    return Response(serializer.data)

# add school
@api_view(['POST'])
def addSchool(request):
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update school
@api_view(['PUT'])
def updateSchool(request, pk):
    school = School.objects.get(id=pk)
    serializer = SchoolSerializer(instance=school, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete school
@api_view(['PUT'])
def deleteSchool(request, pk):
    school = School.objects.get(id=pk)
    school.delete()
    return Response('School successfully deleted.')
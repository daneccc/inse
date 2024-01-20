from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import School
from .serializers import SchoolSerializer

# Create your views here.

# get all schools
@api_view(['GET'])
def getSchools(request):
    try:
        users = School.objects.all()
        serializer = SchoolSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# get single school
@api_view(['GET'])
def getSchool(request, pk):
    try:
        school = School.objects.get(id_escola=pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)
    except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)

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
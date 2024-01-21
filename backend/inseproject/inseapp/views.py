from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import School
from .serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

class InseViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=False, methods=['GET'])
    def getSchools(self, request):
        try:
            users = School.objects.all()
            serializer = SchoolSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True, methods=['GET'])
    def getSchoolDetail(self, request, pk=None):
        try:
            school = School.objects.get(id_escola=pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data)
        except School.DoesNotExist:
                return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['GET'])
    def getSchoolByState(self, request, co_uf=None):
        try:
            schools = School.objects.filter(co_uf=co_uf)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "State not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['GET'])
    def getSchoolByCity(self, request, co_municipio=None):
        try:
            schools = School.objects.filter(co_municipio=co_municipio)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
                
    @action(detail=False, methods=['GET'])
    def getSchoolByNetworkType(self, request, tp_tipo_rede=None):
        try:
            schools = School.objects.filter(tp_tipo_rede=tp_tipo_rede)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "Network type not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['GET'])
    def getSchoolByLocation(self, request, tp_localizacao=None):
        try:
            schools = School.objects.filter(tp_localizacao=tp_localizacao)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def getFilteredSchools(self, request):
        try:
            # Recupera os parâmetros de consulta da URL
            co_uf = request.GET.get('co_uf', None)
            co_municipio = request.GET.get('co_municipio', None)
            tp_tipo_rede = request.GET.get('tp_tipo_rede', None)
            tp_localizacao = request.GET.get('tp_localizacao', None)

            # Constrói um dicionário de filtros com base nos parâmetros fornecidos
            filters = {}
            if co_uf is not None:
                filters['co_uf'] = co_uf
            if co_municipio is not None:
                filters['co_municipio'] = co_municipio
            if tp_tipo_rede is not None:
                filters['tp_tipo_rede'] = tp_tipo_rede
            if tp_localizacao is not None:
                filters['tp_localizacao'] = tp_localizacao

            # Aplica os filtros ao queryset
            schools = School.objects.filter(**filters)

            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist

            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found with the specified filters"}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByDescending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'media_inse' de forma descendente
            schools = School.objects.all().order_by('-media_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByAscending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'media_inse' de forma ascendente
            schools = School.objects.all().order_by('media_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByStudentsDescending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'qtd_alunos_inse' de forma descendente
            schools = School.objects.all().order_by('-qtd_alunos_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByStudentsAscending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'qtd_alunos_inse' de forma ascendente
            schools = School.objects.all().order_by('qtd_alunos_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)
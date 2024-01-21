from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models.inse_model import School
from ..serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from inseapp.services.inse_service import *
from drf_spectacular.utils import extend_schema

class InseViewSet(viewsets.ModelViewSet):
    queryset = get_schools()
    serializer_class = SchoolSerializer

    @extend_schema(
        summary="Get all schools",
        description="Returns a list of all schools.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchools(self, request):
        try:
            users = get_schools()
            serializer = SchoolSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        summary="Get school detail",
        description="Returns details of a specific school.",
        responses={200: SchoolSerializer()}
    )    
    @action(detail=True, methods=['GET'])
    def getSchoolDetail(self, request, pk=None):
        try:
            school = get_school_detail(pk)
            serializer = SchoolSerializer(school)
            return Response(serializer.data)
        except School.DoesNotExist:
                return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        summary="Get schools by state",
        description="Returns a list of schools based on the specified state code.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchoolByState(self, request, co_uf=None):
        try:
            schools = get_schools_by_state(co_uf)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "State not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Get schools by city",
        description="Returns a list of schools based on the specified city code.",
        responses={200: SchoolSerializer(many=True)}
    ) 
    @action(detail=False, methods=['GET'])
    def getSchoolByCity(self, request, co_municipio=None):
        try:
            schools = get_schools_by_city(co_municipio)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Get schools by network type",
        description="Returns a list of schools based on the specified network type.",
        responses={200: SchoolSerializer(many=True)}
    )        
    @action(detail=False, methods=['GET'])
    def getSchoolByNetworkType(self, request, tp_tipo_rede=None):
        try:
            schools = get_schools_by_network_type(tp_tipo_rede)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "Network type not found"}, status=status.HTTP_404_NOT_FOUND)
        

    @extend_schema(
        summary="Get schools by location",
        description="Returns a list of schools based on the specified location type.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchoolByLocation(self, request, tp_localizacao=None):
        try:
            schools = get_schools_by_location(tp_localizacao)
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Get filtered schools",
        description="Returns a list of schools based on the specified filters.",
        responses={200: SchoolSerializer(many=True)}
    )
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

            # Aplica os filtros usando o método centralizado
            schools = filter_schools(**filters)

            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist

            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found with the specified filters"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Get schools ordered by descending media_inse",
        description="Returns a list of schools ordered by media_inse in descending order.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByDescending(self, request):   
        try:
            # Obtém todos os objetos escolares ordenados por 'media_inse' de forma descendente
            schools = order_schools(School.objects.all(), '-media_inse')

            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist

            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Get schools ordered by ascending media_inse",
        description="Returns a list of schools ordered by media_inse in ascending order.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByAscending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'media_inse' de forma ascendente
            schools = order_schools(School.objects.all(), 'media_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)
        
    @extend_schema(
        summary="Get schools ordered by descending qtd_alunos_inse",
        description="Returns a list of schools ordered by qtd_alunos_inse in descending order.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByStudentsDescending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'qtd_alunos_inse' de forma descendente
            schools = order_schools(School.objects.all(), '-qtd_alunos_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        summary="Get schools ordered by ascending qtd_alunos_inse",
        description="Returns a list of schools ordered by qtd_alunos_inse in ascending order.",
        responses={200: SchoolSerializer(many=True)}
    )
    @action(detail=False, methods=['GET'])
    def getSchoolsOrderedByStudentsAscending(self, request):
        try:
            # Obtém todos os objetos escolares ordenados por 'qtd_alunos_inse' de forma ascendente
            schools = order_schools(School.objects.all(), 'qtd_alunos_inse')
            
            # Verifica se há escolas encontradas no queryset
            if not schools.exists():
                raise School.DoesNotExist
            
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({"error": "No schools found"}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['GET'])
    def getUniqueUfs(self, request):
        try:
            # Chama o método do serviço para obter UFs únicas
            unique_ufs_list = get_unique_ufs()

            return Response(unique_ufs_list)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
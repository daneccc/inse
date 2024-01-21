from ..models.inse_model import School

def filter_schools(**filters):
    return School.objects.filter(**filters)

def order_schools(queryset, order_by):
    return queryset.order_by(order_by)

def get_schools():
    return School.objects.all()[:20]

def get_school_detail(pk):
    try:
        return School.objects.get(id_escola=pk)
    except School.DoesNotExist:
        raise School.DoesNotExist("School not found")

def get_schools_by_state(co_uf):
    schools = School.objects.filter(co_uf=co_uf)
    if not schools.exists():
        raise School.DoesNotExist("State not found")
    return schools


def get_schools_by_city(co_municipio):
    schools = School.objects.filter(co_municipio=co_municipio)
    if not schools.exists():
        raise School.DoesNotExist("City not found")
    return schools

def get_schools_by_network_type(tp_tipo_rede):
    schools = School.objects.filter(tp_tipo_rede=tp_tipo_rede)
    if not schools.exists():
        raise School.DoesNotExist("Network type not found")
    return schools

def get_schools_by_location(tp_localizacao):
    schools = School.objects.filter(tp_localizacao=tp_localizacao)
    if not schools.exists():
        raise School.DoesNotExist("Location not found")
    return schools

def get_unique_ufs():
    try:
        # Busca todas as UFs sem repetição
        unique_ufs = School.objects.values('co_uf').distinct()

        # Converte a queryset para uma lista de dicionários
        unique_ufs_list = list(unique_ufs)

        return unique_ufs_list
    except Exception as e:
        # Lide com a exceção conforme necessário
        raise e
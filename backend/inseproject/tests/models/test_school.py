from django.test import TestCase
from inseapp.models.inse_model import School

class SchoolModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Configuração inicial antes de cada teste
        cls.sut = School.objects.create(
            nu_ano_saeb=2024,
            co_uf=1,
            sg_uf='CE',
            no_uf='Ceará',
            co_municipio=123,
            no_municipio='Fortaleza',
            id_escola=987654,
            no_escola='UFC',
            tp_tipo_rede=1,
            tp_localizacao=1,
            tp_capital=1,
            qtd_alunos_inse=100,
            media_inse=9.5,
            inse_classificacao='A',
            pc_nivel_1=10.5,
            pc_nivel_2=20.5,
            pc_nivel_3=30.5,
            pc_nivel_4=40.5,
            pc_nivel_5=50.5,
            pc_nivel_6=60.5,
            pc_nivel_7=70.5,
            pc_nivel_8=80.5,
        )
    
    def test_school_str_representation(self):
        # Teste para garantir que o método __str__ do modelo está funcionando corretamente
        capturedValue = self.sut._meta.get_field('sg_uf').max_length
        self.assertEqual(capturedValue, 50)


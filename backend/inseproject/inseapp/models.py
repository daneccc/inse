from django.db import models

class School(models.Model):
    nu_ano_saeb = models.IntegerField()
    co_uf = models.IntegerField()
    sg_uf = models.CharField(max_lenght=50)
    no_uf = models.CharField(max_lenght=50)
    co_municipio = models.IntegerField()
    no_municipio = models.CharField(max_lenght=50)
    id_escola = models.IntegerField()
    no_escola = models.CharField(max_lenght=50)
    tp_tipo_rede = models.IntegerField()
    tp_localizacao = models.IntegerField()
    tp_capital = models.IntegerField()
    qtd_alunos_inse = models.IntegerField()
    media_inse = models.DecimalField(max_digits=5, decimal_places=2)
    inse_classificacao = models.CharField(max_lenght=50)
    pc_nivel_1 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_2 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_3 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_4 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_5 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_6 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_7 = models.DecimalField(max_digits=5, decimal_places=2)
    pc_nivel_8 = models.DecimalField(max_digits=5, decimal_places=2)
    


from django.db import models


class TypeBudget(models.Model):
    title = models.CharField(max_length=15, verbose_name="Title")

    def __str__(self):
        return self.title


class FormBudget(models.Model):
    salary_year = models.FloatField(verbose_name="Sueldo año")
    cesantias = models.FloatField(verbose_name="Cesantías")
    prima = models.FloatField(verbose_name="Prima")
    int_cesantias = models.FloatField(verbose_name="Int. Cesantías")
    vacaciones = models.FloatField(verbose_name="Vacaciones")
    total_prest = models.FloatField(verbose_name="Total Prestaciones")
    salud = models.FloatField(verbose_name="Salud")
    pension = models.FloatField(verbose_name="Pensión")
    arl = models.FloatField(verbose_name="ARL")
    comfama = models.FloatField(verbose_name="Comfama")
    sena = models.FloatField(verbose_name="SENA")
    icbf = models.FloatField(verbose_name="ICBF")
    total_aportes = models.FloatField(verbose_name="Total Aportes")
    typebudget_id = models.ForeignKey(TypeBudget,on_delete=models.CASCADE,verbose_name="Tipo de aporte")

    def __str__(self):
        return self.id


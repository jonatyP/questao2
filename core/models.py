from django.db import models

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    carga_horaria = models.IntegerField()
    ementa = models.CharField('Ementa', max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return '{} - {} - {}'.format(
            self.nome,
            self.carga_horaria,
            self.ementa,
            self.valor,
    )


class Professor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    valor_hora_aula = models.FloatField('Valor Hora Aula')

    class Meta:
        verbose_name_plural = 'Professores'
        verbose_name = 'Professor'

    def __str__(self):
        return '{} - {} - {}'.format(
            self.nome,
            self.telefone,
            self.valor_hora_aula,
    )

class Turma(models.Model):
    data_inicio = models.DateField('Data de inicio')
    data_termino = models.DateField('Data de termino')
    hora_inicio = models.TimeField('Hora de inicio')
    hora_termino = models.TimeField('Hora de termino')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.data_inicio,
            self.data_termino,
            self.hora_inicio,
            self.hora_termino,
    )

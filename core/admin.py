from django.contrib import admin

from core.models import Curso
from core.models import Turma
from core.models import Professor


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'ementa', 'valor')
    search_fields = ('nome',)

class TurmaInline(admin.TabularInline):
    model = Turma

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('data_inicio', 'data_termino', 'hora_inicio', 'hora_termino')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'valor_hora_aula')
    inlines = [TurmaInline]
    search_fields = ('nome',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Empresa de Cursos'
admin.site.site_title = 'Empresa de Cursos'
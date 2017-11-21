from django.contrib import admin
from examen.models import Materia, MateriaAdmin, Estudiante, EstudianteAdmin, Profesor, Grado, GradoAdmin

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Profesor)

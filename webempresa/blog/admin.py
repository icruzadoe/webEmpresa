from django.contrib import admin
from .models import Category,Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	#mostrar las columnas de titulo, autor y publicacion
	list_display = ('title', 'author', 'published','post_categories')
	#ordenar
	ordering = ('author',)
	#crea un campo para filtrar busquedas, por ser llave foranea se tiene que acceder con esta sintaxis author__username
	search_fields = ('title','content','author__username','categories__name')
	#ordenar por una gerarquia de fechas, se muestra debajo del cuadro de search
	date_hierarchy = 'published'
	#crea una lista en la parte lateral
	list_filter = ('author__username', 'categories__name')

	#se creo esta funcion para mostrar en forma de columna, hace referencia a cada fila que este 
	def post_categories(self,obj):
		return ", ".join([c.name for c in obj.categories.all().order_by("name")])
	#con esto cambiamos el nombre del titulo que se muestra en el panel de admin
	post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
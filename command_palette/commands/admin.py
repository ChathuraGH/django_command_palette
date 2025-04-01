from django.contrib import admin

# Register your models here.



from . import models


admin.site.register(models.Profile)




@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):


	# ADD AN BULK ACTION TO ADMIN

	# actions = ["active"]
	# def active(self, request, queryset):
	#     queryset.update(active=True)


	list_display = ['ptitle','author']
	# list_editable = ('active',)
	list_per_page = 1
	show_full_result_count = False

	search_fields = ['title','content']



	def ptitle(self, obj):
		return obj.title[:25]




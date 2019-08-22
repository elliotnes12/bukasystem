from django.contrib import admin
from contactapi.models import Contact
from .models import Sections,ProjectCategory,Project
#from blog.models import Post,Category



class CategoryAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")

class PostAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")

class ContactAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")
      list_display = ("name","asunto","email")

class SkillsAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")
      list_display = ("name",)

class SectionAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")

class ProjectCategoryAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")
    
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    list_filter = ("title",)

class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class DeparmentAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    list_display = ("name","employee_deparments")
    search_fields = ("name",'deparment__name')

    def employee_deparments(self,obj):
        return "".join([obj.deparment.name])

    employee_deparments.short_description = "departamento"



#admin.site.register(Category,CategoryAdmin)
#admin.site.register(Post,PostAdmin)
admin.site.register(ProjectCategory,ProjectCategoryAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Sections,SectionAdmin)

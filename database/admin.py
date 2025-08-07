from django.contrib import admin
from database.models import Testimonial,About, Aboutextra,Hero,HeroCV



class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('address','name', 'occupation', 'rating', 'opinion',)  
    search_fields = ('name', 'occupation', 'rating', 'opinion',) 
    
# About Admin
class AboutAdmin(admin.ModelAdmin):
    list_display = ('birthday', 'website', 'phone', 'city',)
    search_fields = ('website', 'phone', 'city',)

# Aboutextra Admin
class AboutextraAdmin(admin.ModelAdmin):
    list_display = ('age', 'degree', 'email', 'freelancer',)
    search_fields = ('degree', 'email', 'freelancer',)   
    
class HeroAdmin(admin.ModelAdmin):
    list_display = ('heroimg','heroname','favicon',)
    search_fields = ('heroimg','heroname','favicon',) 

class HeroCVAdmin(admin.ModelAdmin):
    list_display = ('file',)
    search_fields = ('file',)
    
    
admin.site.register(HeroCV, HeroCVAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Aboutextra, AboutextraAdmin)
admin.site.register(Testimonial,TestimonialAdmin)

# Register your models here.

from django.contrib import admin

from customermanager.models import Customer


# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ["first_name","last_name","email","display_password_strength"] #listenansicht
    '''fieldsets = [
        ("Basisdaten", {"fields": ["user__first_name","user__last_name","email"]}),
        ("Kundendetails", {"fields": ["salutation","birthday","user__password"]}) #gruppierung
    ] '''

    def display_password_strength(self, obj):
        if len(obj.user.password)>2:
            return True
        else:
            return False

    display_password_strength.short_despriction = "Passwort Sicherheit"
    display_password_strength.boolean = True

admin.site.register(Customer, AdminCustomer)
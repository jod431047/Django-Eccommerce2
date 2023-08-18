from django.contrib import admin


from .models import Profile , Phones , Address



class PhonesAdmin(admin.TabularInline):
    model = Phones


class AddressAdmin(admin.TabularInline):
    model = Address




class ProfileAdmin(admin.ModelAdmin):
    # inlines = [PhonesAdmin,AddressAdmin]
    pass
    


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Phones)
admin.site.register(Address)
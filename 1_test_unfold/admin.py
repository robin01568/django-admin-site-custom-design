from django import forms
from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from .models import *
from ckeditor.widgets import CKEditorWidget

# Custom Unfold Admin Site
admin.site.site_title = "Fame Tours and Mentors Admin"
admin.site.site_header = "Fame Tours and Mentors Administration"
admin.site.index_title = "Fame Tours and Mentors Site Management"


@admin.register(Banner)
class BannerAdmin(ModelAdmin): pass

@admin.register(CEOMessage)
class CEOMessageAdmin(ModelAdmin): pass

@admin.register(OurPartner)
class OurPartnerAdmin(ModelAdmin): pass

@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin): pass


class ServicesAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Services
        fields = '__all__'

@admin.register(Services)
class ServicesAdmin(ModelAdmin):
    form = ServicesAdminForm
    list_display = ('title', 'is_verify')
    search_fields = ('title',)
    list_filter = ('is_verify',)



class CountryAdminForm(forms.ModelForm):
  content = forms.CharField(widget=CKEditorWidget())
  class Meta:
    model = Country
    fields = '__all__'

@admin.register(Country)
class CountryAdmin(ModelAdmin):
  form = CountryAdminForm
  list_display = ('title', 'slug')
  prepopulated_fields = {'slug': ('title',)}
  search_fields = ('title',)



class PrivacyTermsAdminForm(forms.ModelForm):
  content = forms.CharField(widget=CKEditorWidget())
  class Meta:
    model = PrivacyTerms
    fields = '__all__'

@admin.register(PrivacyTerms)
class PrivacyTermsAdmin(ModelAdmin):
  form = PrivacyTermsAdminForm
  list_display = ('title',)
  search_fields = ('title',)
  


class PhoneInline(StackedInline):
    model = Phone
    extra = 0

class EmailInline(StackedInline):
    model = Email
    extra = 0

@admin.register(WebsiteInfo)
class WebsiteInfoAdmin(ModelAdmin):
    list_display = ('home_title', 'is_verify')
    inlines = [PhoneInline, EmailInline]


















# from django.contrib import admin
# from django import forms
# from ckeditor.widgets import CKEditorWidget
# from .models import *

# admin.site.register(Banner)
# admin.site.register(CEOMessage)
# admin.site.register(OurPartner)
# admin.site.register(ContactUs)


# class ServicesAdminForm(forms.ModelForm):
#   content = forms.CharField(widget=CKEditorWidget())
#   class Meta:
#     model = Services
#     fields = '__all__'

# @admin.register(Services)
# class ServicesAdmin(admin.ModelAdmin):
#   form = ServicesAdminForm
#   list_display = ('title',)
#   search_fields = ('title',)



# class CountryAdminForm(forms.ModelForm):
#   content = forms.CharField(widget=CKEditorWidget())
#   class Meta:
#     model = Country
#     fields = '__all__'

# @admin.register(Country)
# class CountryAdmin(admin.ModelAdmin):
#   form = CountryAdminForm
#   list_display = ('title', 'slug')
#   prepopulated_fields = {'slug': ('title',)}
#   search_fields = ('title',)


# class PrivacyTermsAdminForm(forms.ModelForm):
#   content = forms.CharField(widget=CKEditorWidget())
#   class Meta:
#     model = PrivacyTerms
#     fields = '__all__'

# @admin.register(PrivacyTerms)
# class PrivacyTermsAdmin(admin.ModelAdmin):
#   form = PrivacyTermsAdminForm
#   list_display = ('title',)
#   search_fields = ('title',)


# class PhoneAdmin(admin.StackedInline):
#   model = Phone
#   extra = 1
  
# class EmailAdmin(admin.StackedInline):
#   model = Email
#   extra = 1

# class WebsiteInfoAdmin(admin.ModelAdmin):
#   list_display = ("home_title", "is_verify")
#   inlines = [PhoneAdmin, EmailAdmin]
# admin.site.register(WebsiteInfo, WebsiteInfoAdmin)



# admin.site.site_title = "Fame Tours and Mentors Admin"
# admin.site.site_header = "Fame Tours and Mentors Administration"
# admin.site.index_title = "Fame Tours and Mentors Site Management"
from django.contrib import admin
from app.models import (Country, City, Province, UserProfile, JobCategory, Skill, EmploymentType, CompanyType, Language, Company, Job, JobSkill, JobSeekerWorkExperience, JobSeekerEducation, JobSeekerLanguage)


class CountryAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class CityAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class ProvinceAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class UserProfileAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class JobCategoryAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class SkillAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class EmploymentTypeAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class CompanyTypeAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class LanguageAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class CompanyAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class JobAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class JobSkillAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class JobSeekerWorkExperienceAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class JobSeekerEducationAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )


class JobSeekerLanguageAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', )



admin.site.register(Country, CountryAdmin)

admin.site.register(City, CityAdmin)

admin.site.register(Province, ProvinceAdmin)

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(JobCategory, JobCategoryAdmin)

admin.site.register(Skill, SkillAdmin)

admin.site.register(EmploymentType, EmploymentTypeAdmin)

admin.site.register(CompanyType, CompanyTypeAdmin)

admin.site.register(Language, LanguageAdmin)

admin.site.register(Company, CompanyAdmin)

admin.site.register(Job, JobAdmin)

admin.site.register(JobSkill, JobSkillAdmin)

admin.site.register(JobSeekerWorkExperience, JobSeekerWorkExperienceAdmin)

admin.site.register(JobSeekerEducation, JobSeekerEducationAdmin)

admin.site.register(JobSeekerLanguage, JobSeekerLanguageAdmin)

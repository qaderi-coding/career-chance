from django.contrib import admin
from .models import Country, City, Province, UserProfile, JobCategory, Skill, EmploymentType, CompanyType, Language, Company, Job, JobSkill, JobSeekerWorkExperience, JobSeekerEducation, JobSeekerLanguage

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(UserProfile)
admin.site.register(JobCategory)
admin.site.register(Skill)
admin.site.register(EmploymentType)
admin.site.register(CompanyType)
admin.site.register(Language)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobSkill)
admin.site.register(JobSeekerEducation)
admin.site.register(JobSeekerLanguage)
admin.site.register(JobSeekerWorkExperience)

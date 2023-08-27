from rest_framework import viewsets

from .models import Country, City, Province, UserProfile, JobCategory, Skill, EmploymentType, CompanyType, Language, Company, Job, JobSkill, JobSeekerWorkExperience, JobSeekerEducation, JobSeekerLanguage
from .serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class= CountrySerializer
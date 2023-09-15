from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
import django_filters.rest_framework
from app.serializers import (CountrySerializer, CitySerializer, ProvinceSerializer, UserProfileSerializer, JobCategorySerializer, SkillSerializer, EmploymentTypeSerializer, CompanyTypeSerializer, LanguageSerializer, CompanySerializer, JobSerializer, JobSkillSerializer, JobSeekerWorkExperienceSerializer, JobSeekerEducationSerializer, JobSeekerLanguageSerializer)
from app.models import (Country, City, Province, UserProfile, JobCategory, Skill, EmploymentType, CompanyType, Language, Company, Job, JobSkill, JobSeekerWorkExperience, JobSeekerEducation, JobSeekerLanguage)

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.order_by('pk')
    serializer_class = CountrySerializer
 

class CityViewSet(ModelViewSet):
    queryset = City.objects.order_by('pk')
    serializer_class = CitySerializer
 

class ProvinceViewSet(ModelViewSet):
    queryset = Province.objects.order_by('pk')
    serializer_class = ProvinceSerializer
 

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.order_by('pk')
    serializer_class = UserProfileSerializer
 

class JobCategoryViewSet(ModelViewSet):
    queryset = JobCategory.objects.order_by('pk')
    serializer_class = JobCategorySerializer
 

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.order_by('pk')
    serializer_class = SkillSerializer
 

class EmploymentTypeViewSet(ModelViewSet):
    queryset = EmploymentType.objects.order_by('pk')
    serializer_class = EmploymentTypeSerializer
 

class CompanyTypeViewSet(ModelViewSet):
    queryset = CompanyType.objects.order_by('pk')
    serializer_class = CompanyTypeSerializer
 

class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.order_by('pk')
    serializer_class = LanguageSerializer
 

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.order_by('pk')
    serializer_class = CompanySerializer
 

class JobViewSet(ModelViewSet):
    queryset = Job.objects.order_by('pk')
    serializer_class = JobSerializer
 

class JobSkillViewSet(ModelViewSet):
    queryset = JobSkill.objects.order_by('pk')
    serializer_class = JobSkillSerializer
 

class JobSeekerWorkExperienceViewSet(ModelViewSet):
    queryset = JobSeekerWorkExperience.objects.order_by('pk')
    serializer_class = JobSeekerWorkExperienceSerializer
 

class JobSeekerEducationViewSet(ModelViewSet):
    queryset = JobSeekerEducation.objects.order_by('pk')
    serializer_class = JobSeekerEducationSerializer
 

class JobSeekerLanguageViewSet(ModelViewSet):
    queryset = JobSeekerLanguage.objects.order_by('pk')
    serializer_class = JobSeekerLanguageSerializer
 

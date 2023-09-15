from rest_framework.serializers import ModelSerializer
from app.models import (Country, City, Province, UserProfile, JobCategory, Skill, EmploymentType, CompanyType, Language, Company, Job, JobSkill, JobSeekerWorkExperience, JobSeekerEducation, JobSeekerLanguage)


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        depth = 2
        fields = '__all__'

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        depth = 2
        fields = '__all__'

class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province
        depth = 2
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        depth = 2
        fields = '__all__'

class JobCategorySerializer(ModelSerializer):
    class Meta:
        model = JobCategory
        depth = 2
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        depth = 2
        fields = '__all__'

class EmploymentTypeSerializer(ModelSerializer):
    class Meta:
        model = EmploymentType
        depth = 2
        fields = '__all__'

class CompanyTypeSerializer(ModelSerializer):
    class Meta:
        model = CompanyType
        depth = 2
        fields = '__all__'

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        depth = 2
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        depth = 2
        fields = '__all__'

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        depth = 2
        fields = '__all__'

class JobSkillSerializer(ModelSerializer):
    class Meta:
        model = JobSkill
        depth = 2
        fields = '__all__'

class JobSeekerWorkExperienceSerializer(ModelSerializer):
    class Meta:
        model = JobSeekerWorkExperience
        depth = 2
        fields = '__all__'

class JobSeekerEducationSerializer(ModelSerializer):
    class Meta:
        model = JobSeekerEducation
        depth = 2
        fields = '__all__'

class JobSeekerLanguageSerializer(ModelSerializer):
    class Meta:
        model = JobSeekerLanguage
        depth = 2
        fields = '__all__'


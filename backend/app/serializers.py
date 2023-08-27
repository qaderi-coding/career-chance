from dataclasses import fields
from pyexpat import model
from .models import Country, City, Province, UserProfile, JobCategory, Skill, EmploymentType, CompanyType, Language, Company, Job, JobSkill, JobSeekerWorkExperience, JobSeekerEducation, JobSeekerLanguage
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
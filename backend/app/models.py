import re
from statistics import mode
from django.contrib.auth.models import User
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Province(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="user" )
    status = models.IntegerField(blank=False)
    phone = models.CharField(max_length=13, blank=True)
    address_line1 = models.CharField(max_length=100 ,blank=True)
    address_lin2 = models.CharField(max_length=100, blank=True)
    country = models.OneToOneField(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_country" )
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_city" )
    province = models.OneToOneField(Province, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_province" )
    zip = models.IntegerField(blank=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class JobCategory(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100,blank=False)
    job_category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=False, related_name="category_skills")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EmploymentType(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   
    
class CompanyType(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   
    
class Language(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False)
    website = models.CharField(max_length=100, blank=True)
    type = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=False, related_name="type_companies" )
    description = models.TextField(blank=True, null=True)
    size =models.CharField(max_length=20, blank=True, null=True)
    country = models.OneToOneField(Country, on_delete=models.SET_NULL, null=True, blank=False, related_name="country_companies" )
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True, blank=False, related_name="city_companies" )
    province = models.OneToOneField(Province, on_delete=models.SET_NULL, null=True, blank=False, related_name="province_companies" )
    contact_person_name =models.CharField(max_length=100, blank=False, null=True)
    contact_person_email =models.EmailField(max_length=100, blank=False, null=True)
    contact_person_phone =models.CharField(max_length=13, blank=False, null=True)
    # logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   

class Job(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False, null=False)
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.SET_NULL, null=True, blank=False, related_name="jobs")
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True,blank=False,related_name="jobs")
    salary = models.FloatField(max_length=100, blank=True, null=True)
    country = models.OneToOneField(Country, on_delete=models.SET_NULL, null=True, blank=False, related_name="jobs" )
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True, blank=False, related_name="jobs" )
    province = models.OneToOneField(Province, on_delete=models.SET_NULL, null=True, blank=False, related_name="jobs" )
    post_date = models.DateTimeField(auto_now_add=True, blank=False)
    end_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   

class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=False, related_name="job_skills")
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=False, related_name="job_skills")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{1}->{0}".format(self.job.name, self.skill.name)

class JobSeekerWorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="job_seeker_experiences")
    company_name = models.CharField(max_length=100, blank=False)
    position_title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False, null=False)
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.SET_NULL, null=True, blank=False, related_name="job_seeker_experiences")
    country = models.OneToOneField(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name="job_seeker_experiences" )
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="job_seeker_experiences" )
    province = models.OneToOneField(Province, on_delete=models.SET_NULL, null=True, blank=True, related_name="job_seeker_experiences" )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class JobSeekerEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="job_seeker_eduction")
    institute_name = models.CharField(max_length=100, blank=False)
    degree = models.CharField(max_length=100, blank=False)
    field = models.CharField(max_length=100, blank=False)
    grade = models.CharField(max_length=2, blank=False)
    description = models.TextField(blank=False, null=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class JobSeekerLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name="job_seeker_languages")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=False, related_name="language_job_seekers")
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=False, related_name="skill_jobs")


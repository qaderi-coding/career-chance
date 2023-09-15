from rest_framework import routers
from app import viewsets
router = routers.DefaultRouter()

router.register(r'country', viewsets.CountryViewSet, 'country')
router.register(r'city', viewsets.CityViewSet, 'city')
router.register(r'province', viewsets.ProvinceViewSet, 'province')
router.register(r'userprofile', viewsets.UserProfileViewSet, 'userprofile')
router.register(r'jobcategory', viewsets.JobCategoryViewSet, 'jobcategory')
router.register(r'skill', viewsets.SkillViewSet, 'skill')
router.register(r'employmenttype', viewsets.EmploymentTypeViewSet, 'employmenttype')
router.register(r'companytype', viewsets.CompanyTypeViewSet, 'companytype')
router.register(r'language', viewsets.LanguageViewSet, 'language')
router.register(r'company', viewsets.CompanyViewSet, 'company')
router.register(r'job', viewsets.JobViewSet, 'job')
router.register(r'jobskill', viewsets.JobSkillViewSet, 'jobskill')
router.register(r'jobseekerworkexperience', viewsets.JobSeekerWorkExperienceViewSet, 'jobseekerworkexperience')
router.register(r'jobseekereducation', viewsets.JobSeekerEducationViewSet, 'jobseekereducation')
router.register(r'jobseekerlanguage', viewsets.JobSeekerLanguageViewSet, 'jobseekerlanguage')
urlpatterns = router.urls

from django.contrib import admin
from .models import (
    Project,
    Skill,
    Education,
    ContactMessage,
    Experience,
    Training,
    Certification,
    Resume,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'github_link', 'live_link', 'created_at')
    search_fields = ('title', 'technologies', 'description', 'features')
    list_filter = ('created_at',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'percentage')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('category', 'order')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'college', 'university', 'year', 'percentage')
    search_fields = ('degree', 'college', 'university')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'location', 'start_date', 'end_date', 'is_current')
    search_fields = ('role', 'company', 'description')
    list_filter = ('is_current',)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'institution', 'duration', 'order')
    search_fields = ('program_name', 'institution', 'topics')
    list_editable = ('order',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'year', 'certificate_link')
    search_fields = ('name', 'organization')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("title", "file", "updated_at")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)
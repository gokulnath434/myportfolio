from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from portfolio import views


urlpatterns = [

    # =========================================================
    # ADMIN
    # =========================================================

    path("admin/", admin.site.urls),


    # =========================================================
    # HOME PAGE
    # URL: /
    # =========================================================

    path("", views.home, name="home"),


    # =========================================================
    # ABOUT PAGE
    # URL: /about/
    # =========================================================

    path("about/", views.about, name="about"),


    # =========================================================
    # EXPERIENCE & EDUCATION
    # URL: /experience/
    # =========================================================

    path("experience/", views.experience, name="experience"),


    # =========================================================
    # PROJECTS PAGE
    # URL: /projects/
    # =========================================================

    path("projects/", views.projects, name="projects"),


    # =========================================================
    # PROJECT DETAIL PAGE
    # URL: /projects/1/
    # =========================================================

    path("projects/<int:pk>/", views.project_detail, name="project_detail"),


    # =========================================================
    # CONTACT PAGE
    # URL: /contact/
    # =========================================================

    path("contact/", views.contact, name="contact"),


    # =========================================================
    # CONTACT SUCCESS PAGE
    # URL: /contact/success/
    # =========================================================

    path("contact/success/", views.contact_success, name="contact_success"),


    # =========================================================
    # RESUME REDIRECT
    # URL: /resume/
    # =========================================================

    path("resume/", views.resume, name="resume"),

]


# =========================================================
# MEDIA FILES
# =========================================================
# This allows uploaded project images to display
# while DEBUG = True.

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
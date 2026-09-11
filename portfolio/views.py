import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse
from django.conf import settings

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
from .forms import ContactForm


# =========================================================
# HOME PAGE
# =========================================================

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your message has been sent successfully. I will get back to you shortly."
            )
            return redirect("/#contact")
        else:
            messages.error(
                request,
                "Please review the errors in the form and try again."
            )
    else:
        form = ContactForm()

    projects = Project.objects.all().order_by("-created_at")
    skills = Skill.objects.all().order_by("category", "order", "name")
    
    # Categorized skills grouping
    categories = [
        ('BACKEND', 'Backend Development', 'bi-server'),
        ('DATABASE', 'Database & ORM', 'bi-database'),
        ('FRONTEND', 'Frontend Development', 'bi-window-stack'),
        ('TOOLS', 'Tools & Workflow', 'bi-tools'),
        ('OTHER', 'Other Technical Competencies', 'bi-gear-wide-connected'),
    ]
    categorized_skills = []
    for code, label, icon in categories:
        cat_skills = [s for s in skills if s.category == code]
        if cat_skills:
            categorized_skills.append({
                'code': code,
                'label': label,
                'icon': icon,
                'skills': cat_skills
            })

    experiences = Experience.objects.all().order_by("-id")
    education = Education.objects.all().order_by("-id")
    trainings = Training.objects.all().order_by("order", "-id")
    certifications = Certification.objects.all().order_by("-year")

    context = {
        "projects": projects,
        "skills": skills,
        "categorized_skills": categorized_skills,
        "experiences": experiences,
        "education": education,
        "trainings": trainings,
        "certifications": certifications,
        "form": form,
    }

    return render(request, "portfolio/home.html", context)


# =========================================================
# ABOUT PAGE
# =========================================================

def about(request):
    skills = Skill.objects.all().order_by("category", "order", "name")
    education = Education.objects.all().order_by("-id")
    experiences = Experience.objects.all().order_by("-id")
    trainings = Training.objects.all().order_by("order", "-id")
    certifications = Certification.objects.all().order_by("-year")

    context = {
        "skills": skills,
        "education": education,
        "experiences": experiences,
        "trainings": trainings,
        "certifications": certifications,
    }

    return render(request, "portfolio/about.html", context)


# =========================================================
# PROJECTS PAGE
# =========================================================

def projects(request):
    project_list = Project.objects.all().order_by("-created_at")
    return render(request, "portfolio/projects.html", {"projects": project_list})


# =========================================================
# PROJECT DETAIL PAGE
# =========================================================

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    other_projects = Project.objects.exclude(pk=pk).order_by("-created_at")[:2]
    
    return render(
        request,
        "portfolio/project_detail.html",
        {
            "project": project,
            "other_projects": other_projects,
        }
    )


# =========================================================
# EXPERIENCE & EDUCATION PAGE
# =========================================================

def experience(request):
    experiences = Experience.objects.all().order_by("-id")
    education = Education.objects.all().order_by("-id")
    trainings = Training.objects.all().order_by("order", "-id")
    certifications = Certification.objects.all().order_by("-year")

    context = {
        "experiences": experiences,
        "education": education,
        "trainings": trainings,
        "certifications": certifications,
    }

    return render(request, "portfolio/experience.html", context)


# =========================================================
# CONTACT PAGE
# =========================================================

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your message has been sent successfully. I will get back to you shortly."
            )
            return redirect("contact")
        else:
            messages.error(
                request,
                "Please review the errors in the form and try again."
            )
    else:
        form = ContactForm()

    return render(request, "portfolio/contact.html", {"form": form})


# =========================================================
# CONTACT SUCCESS PAGE (Optional / fallback)
# =========================================================

def contact_success(request):
    return render(request, "portfolio/contact_success.html")


# =========================================================
# RESUME DOWNLOAD / VIEW
# =========================================================

def resume(request):
    """
    Reliably serve the latest uploaded resume or the default static PDF.
    """
    resume_file = Resume.objects.order_by("-updated_at").first()
    if resume_file and resume_file.file:
        try:
            if os.path.exists(resume_file.file.path):
                return FileResponse(
                    open(resume_file.file.path, "rb"),
                    content_type="application/pdf",
                    filename="Gokulnath_S_Resume.pdf"
                )
        except Exception:
            pass

    # Static fallback
    static_resume = settings.BASE_DIR / "portfolio" / "static" / "portfolio" / "resume" / "Gokulnath_S_Resume.pdf"
    if static_resume.exists():
        return FileResponse(
            open(static_resume, "rb"),
            content_type="application/pdf",
            filename="Gokulnath_S_Resume.pdf"
        )

    return redirect("home")
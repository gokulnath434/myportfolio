from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Short overview of the project")
    detailed_description = models.TextField(
        blank=True,
        default="",
        help_text="In-depth project breakdown, problem statement, and solution"
    )
    features = models.TextField(
        blank=True,
        default="",
        help_text="Key features (one per line or comma-separated)"
    )
    technologies = models.CharField(
        max_length=300,
        help_text="Comma-separated list of technologies used (e.g. Python, Django, MySQL)"
    )
    github_link = models.URLField(blank=True, help_text="Repository URL")
    live_link = models.URLField(blank=True, help_text="Live deployment URL (leave empty if not deployed)")
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Project preview or architecture screenshot"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_features_list(self):
        """Return a clean list of feature bullet points."""
        if not self.features:
            return []
        lines = [line.strip().lstrip('•-* ').strip() for line in self.features.splitlines() if line.strip()]
        if len(lines) == 1 and ',' in lines[0]:
            return [x.strip() for x in lines[0].split(',') if x.strip()]
        return lines

    def get_technologies_list(self):
        """Return a clean list of tech badges."""
        if not self.technologies:
            return []
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('BACKEND', 'Backend Development'),
        ('DATABASE', 'Database'),
        ('FRONTEND', 'Frontend Development'),
        ('TOOLS', 'Tools & Workflow'),
        ('OTHER', 'Other Technical Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='BACKEND'
    )
    percentage = models.IntegerField(default=85, help_text="Internal proficiency indicator")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    university = models.CharField(max_length=200, blank=True, default='')
    year = models.CharField(max_length=50)
    percentage = models.CharField(max_length=20, blank=True, default='')

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.degree


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=True, default="Chennai, Tamil Nadu")
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField(help_text="Role summary or bullet points separated by newlines")
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.role} - {self.company}"

    def get_bullet_points(self):
        """Return clean list of responsibilities/achievements."""
        if not self.description:
            return []
        return [line.strip().lstrip('•-* ').strip() for line in self.description.splitlines() if line.strip()]


class Training(models.Model):
    program_name = models.CharField(max_length=200, default="Full Stack Development – Python")
    institution = models.CharField(max_length=200, default="Mastermind Techno Solution")
    duration = models.CharField(max_length=100, default="Nov 2024 – Jul 2025")
    topics = models.CharField(
        max_length=300,
        default="Python, Django, Web Development, Database, Full Stack Development"
    )
    description = models.TextField(blank=True, default="")
    certificate_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Training Program"
        verbose_name_plural = "Training Programs"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.program_name} - {self.institution}"

    def get_topics_list(self):
        if not self.topics:
            return []
        return [t.strip() for t in self.topics.split(',') if t.strip()]


class Certification(models.Model):
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    certificate_link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    title = models.CharField(
        max_length=200,
        default="Gokulnath S Resume"
    )
    file = models.FileField(
        upload_to="resume/"
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
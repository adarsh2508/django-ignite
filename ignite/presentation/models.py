from django.db import models

class Presentation(models.Model):
    """
    Presentation model to represent Ignite presentations.
    """
    presenter_name = models.CharField(maxlength=255, help_text="Name of person presenting.")
    presenter_email = models.EmailField(help_text="E-mail of person presenting for contact purposes, not displayed publicly.")
    presenter_url = models.URLField(help_text="Optional URL to link presenter name to.")
    presenter_bio = models.TextField(blank=True, help_text="Option short bio about presenter.")
    title = models.CharField(maxlength=255, help_text="Title of presentation.")
    description = models.TextField(help_text="Full description of presentation.")
    created = models.DateTimeField()
    # fields to help determine whether this presentation is chosen?

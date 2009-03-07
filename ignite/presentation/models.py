from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

class Presentation(models.Model):
    """
    Presentation model to represent Ignite presentations.
    """
    title = models.CharField(max_length=255, help_text="Title of presentation.")
    slug = models.SlugField(max_length=255)
    description = models.TextField(help_text="Full description of presentation.")
    presenter_name = models.CharField(max_length=255, help_text="Name of person presenting.")
    presenter_email = models.EmailField(help_text="E-mail of person presenting for contact purposes, not displayed publicly.")
    presenter_url = models.URLField(blank=True, help_text="Optional URL to link presenter name to.")
    presenter_bio = models.TextField(blank=True, help_text="Optional short bio about presenter.")
    created = models.DateTimeField(default=datetime.now)
    # fields to help determine whether this presentation is chosen?

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Presentation, self).save()


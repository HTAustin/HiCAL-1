from django.db import models
from config.settings.base import AUTH_USER_MODEL as User
from treccoreweb.progress.models import Task
from django.contrib.postgres.fields import JSONField


class Judgement(models.Model):
    class Meta:
        unique_together = ['user', 'doc_id', 'task']
        index_together = ['user', 'doc_id', 'task']

    LOGGING_MESSAGES = {
        "create": "New judgment.",
        "update": "Updated judgment."
    }

    user = models.ForeignKey(User)
    doc_id = models.CharField(null=False,
                              blank=False,
                              max_length=512)
    doc_title = models.CharField(null=False,
                                 blank=False,
                                 max_length=512)
    doc_CAL_snippet = models.TextField(null=False,
                                       blank=False)
    doc_search_snippet = models.TextField(null=False,
                                          blank=False)
    task = models.ForeignKey(Task)
    query = models.CharField(null=True,
                             blank=True,
                             max_length=512)
    relevant = models.BooleanField(null=False, blank=False)
    nonrelevant = models.BooleanField(null=False, blank=False)
    ontopic = models.BooleanField(null=False, blank=False)
    isFromCAL = models.BooleanField(null=False, blank=False)
    isFromSearch = models.BooleanField(null=False, blank=False)
    isFromSearchModal = models.BooleanField(null=False, blank=False)
    fromMouse = models.BooleanField(null=False, blank=False)
    fromKeyboard = models.BooleanField(null=False, blank=False)
    timeVerbose = JSONField(null=True, blank=True, default=[])

    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        judgment = 1 if self.relevant else -1 if self.nonrelevant else 0 if self.ontopic else None
        return "{} on {}: {}".format(self.user, self.doc_id, judgment)

    def __str__(self):
        return self.__unicode__()

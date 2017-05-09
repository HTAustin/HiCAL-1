from django.db import models
from config.settings.base import AUTH_USER_MODEL as User
from treccoreweb.topic.models import Topic


class Judgement(models.Model):
    LOGGING_MESSAGES = {
        "create": "New judgment."
    }

    user = models.ForeignKey(User)
    doc_id = models.CharField(null=False,
                              blank=False,
                              max_length=512)
    topic = models.ForeignKey(Topic)
    query = models.CharField(null=True,
                             blank=True,
                             max_length=512)
    relevant = models.BooleanField(null=False, blank=False)
    nonrelevant = models.BooleanField(null=False, blank=False)
    notsure = models.BooleanField(null=False, blank=False)
    time_to_judge = models.CharField(null=True, blank=True, max_length=512)
    isFromCAL = models.BooleanField(null=False, blank=False)
    fromMouse = models.BooleanField(null=False, blank=False)
    fromKeyboard = models.BooleanField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} on {}".format(self.user, self.doc_id)

    def __str__(self):
        return self.__unicode__()

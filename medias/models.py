from django.db import models
from common.models import CommonModel

class Photo(CommonModel):

    # Photo Model Definition
    file = models.ImageField()
    description = models.CharField(max_length=150)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, null=True, blank=True)
    experience = models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Photo File"

class Video(CommonModel):

    # Video Model Definition
    file = models.FileField()
    experience = models.OneToOneField("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Video File"

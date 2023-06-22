from webpfield.webp_storage import WebPStorage

from .settings import IMAGE_FIELD_CLASS, ENABLE_SVG
from django import forms


class WebPField(IMAGE_FIELD_CLASS):
    def __init__(self, *args, **kwargs):
        kwargs.update({"storage": WebPStorage()})
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        if ENABLE_SVG:
            kwargs.update({"form_class": forms.FileField})
        return super().formfield(**kwargs)

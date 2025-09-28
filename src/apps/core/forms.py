from .utils.django_forms import add_attr


class FormStylingMixin:
    """
    Mixin que adiciona classes CSS 'form-control' e 'is-invalid'
    automaticamente para os campos de um formulário.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            add_attr(field, 'class', 'form-control')
            if field_name in self.errors:
                add_attr(field, 'class', 'is-invalid')

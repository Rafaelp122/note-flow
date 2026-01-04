from .utils.django_forms import add_attr


class FormStylingMixin:
    """
    Mixin que adiciona classes CSS do Tailwind v4 / Flowbite
    automaticamente para os campos de um formulário.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Classes base baseadas na paleta profissional de azuis/cinzas
        base_classes = (
            "bg-neutral-secondary-medium border border-default-medium "
            "text-heading text-sm rounded-base focus:ring-brand "
            "focus:border-brand block w-full px-3 py-2.5 shadow-xs "
            "placeholder:text-body transition-all"
        )

        # Classes para quando o campo tem erro (usando o Vermelho da sua paleta)
        error_classes = "border-error text-error focus:ring-error focus:border-error"

        for field_name, field in self.fields.items():
            # Adiciona as classes base
            add_attr(field, 'class', base_classes)

            # Se o campo tiver erro, adiciona o destaque em vermelho
            if field_name in self.errors:
                add_attr(field, 'class', error_classes)

from django import template

register = template.Library()


@register.inclusion_tag("form_input_field.html")
def form_input_field(field):
    field.field.widget.attrs.update({"class": "form-control"})
    return {"field": field}
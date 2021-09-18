from django.views import generic
from django.apps import apps


class CustomBaseView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = self.model._meta.app_label
        context['model_name'] = self.model._meta.verbose_name
        context['model_name_plural'] = self.model._meta.verbose_name_plural
        context['view_name'] = self.__class__.__name__.lower().replace(
            context['model_name'], '').replace('view', '')
        context['app_config'] = apps.get_app_config(context['app_name'])
        # context['site_header'] = f"Listado de {self.model._meta.verbose_name_plural}"
        context['subtitle'] = f"Listado"
        return context


class BaseListView(CustomBaseView, generic.ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = f"{self.model._meta.app_label}/list.html"


class BaseDetailView(CustomBaseView, generic.UpdateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = f"{self.model._meta.app_label}/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = [f.name for f in context['object']._meta.fields]
        return context


class BaseDeleteView(CustomBaseView, generic.DeleteView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = f"{self.model._meta.app_label}/confirm_delete.html"


class BaseCreateView(CustomBaseView, generic.CreateView):
    template_name = f'create.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = f"{self.model._meta.app_label}/form.html"

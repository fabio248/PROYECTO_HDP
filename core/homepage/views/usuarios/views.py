from django.http import JsonResponse
from django.views.generic import CreateView

from core.homepage.form import UsuarioForm
from core.apps.models import Usuario


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/homepage.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Usuario.objects.filter(dui__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['text'] = i.dui
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as error:
            data['error'] = str(error)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Sistema Subidios - Index'
        context['titulo'] = 'Registro de subsidios'

        return context

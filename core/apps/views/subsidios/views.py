from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from core.apps.forms import *
from core.apps.models import *


# Subsidios trasnporte
class SubsidioTrasnporteListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioTransporte
    # vista a utilizar
    template_name = 'subsidiosTransporte/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': 'Fabio'}
        try:
            sub = SubsidioTransporte.objects.get(pk=request.POST['id']).toJSON()
        except Exception as error:
            data['error'] = str(error)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio transporte público'
        context['titulo'] = 'Subsidios transporte público'
        return context

    def get_queryset(self):
        return SubsidioTransporte.objects.all()


class SubsidioTransporteCreateView(CreateView):
    model = SubsidioTransporte
    form_class = SubsidioTransporteForm
    template_name = 'subsidiosTransporte/create.html'
    success_url = reverse_lazy('home:homepage')

    def post(self, request, *args, **kwargs):
        data = {}
        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Fomulario | Subsidio Transporte'
        context['panel'] = 'Fomulario | Subsidio Transporte'
        context['subtitulo'] = 'Formulario'
        context['action'] = 'add'
        return context


class SubsidioTransporteUpdateView(UpdateView):
    model = SubsidioTransporte
    form_class = SubsidioTransporteEditForm
    template_name = 'subsidiosTransporte/edit.html'
    success_url = reverse_lazy('apps:subsidio_transporte_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Edición subsidio transporte público'
        return context


class SubsidioTransporteDeleteView(DeleteView):
    model = SubsidioTransporte
    template_name = 'subsidiosTransporte/delete.html'
    success_url = reverse_lazy('apps:subsidio_transporte_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Eliminación subsidio transporte público'
        context['lista_url'] = reverse_lazy('apps:subsidio_transporte_lista')
        return context


# Subsidio agua
class SubsidioAguaListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioAgua
    # vista a utilizar
    template_name = 'subsidioAgua/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            action = request.POST['action']
            if action == 'buscardatos':
                for subsidio in SubsidioAgua.objects.all():
                    data.append(subsidio).toJSON()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         data = SubsidioAgua.objects.get(pk=request.POST['id']).toJSON()
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio servicio agua'
        context['titulo'] = 'Servicio agua'
        context['sumatoria'] = 'Total de sumatoria'
        return context

    def get_queryset(self):
        return SubsidioAgua.objects.all()


class SubsidioAguaCreateView(CreateView):
    model = SubsidioAgua
    form_class = SubsidioAguaForm
    template_name = 'subsidioAgua/create.html'
    success_url = reverse_lazy('home:homepage')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Formulario | Subsudio agua'
        context['titulo'] = 'Formulario subsidio agua'
        context['action'] = 'add'
        context['home_url'] = reverse_lazy('home:homepage')
        return context


class SubsidioAguaUpdateView(UpdateView):
    model = SubsidioAgua
    form_class = SubsidioAguaEditForm
    template_name = 'subsidioAgua/edit.html'
    success_url = reverse_lazy('apps:subsidio_agua_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Edición subsidio agua'
        context['lista_url'] = reverse_lazy('apps:subsidio_agua_lista')
        return context


class SubsidioAguaDeleteView(DeleteView):
    model = SubsidioAgua
    template_name = 'subsidioAgua/delete.html'
    success_url = reverse_lazy('apps:subsidio_agua_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Eliminación subsidio agua'
        context['lista_url'] = reverse_lazy('apps:subsidio_agua_lista')
        return context


# Subsidio luz
class SubsidioLuzListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioLuz
    # vista a utilizar
    template_name = 'subsidioLuz/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio energía eléctrica'
        context['titulo'] = 'Servicio energía eléctrica'

        return context

    def get_queryset(self):
        return SubsidioLuz.objects.all()


class SubsidioLuzCreateView(CreateView):
    model = SubsidioLuz
    form_class = SubsidioLuzForm
    template_name = 'subsidioLuz/create.html'
    success_url = reverse_lazy('home:homepage')

    def post(self, request, *args, **kwargs):
        data = {}
        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Fomulario | Subsidio energía eléctrica'
        context['titulo'] = 'Fomulario | Subsidio energía eléctrica'
        context['subtitulo'] = 'Formulario'
        return context


class SubsidioLuzUpdateView(UpdateView):
    model = SubsidioLuz
    form_class = SubsidioLuzEditForm
    template_name = 'subsidioLuz/edit.html'
    success_url = reverse_lazy('apps:subsidio_luz_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Edición subsidio energía eléctrica'
        context['lista_url'] = reverse_lazy('apps:subsidio_luz_lista')
        return context


class SubsidioLuzDeleteView(DeleteView):
    model = SubsidioLuz
    template_name = 'subsidioLuz/delete.html'
    success_url = reverse_lazy('apps:subsidio_luz_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Eliminación subsidio enegía eléctrica'
        context['lista_url'] = reverse_lazy('apps:subsidio_luz_lista')
        return context


# Subsidio Gas
class SubsidioGasListView(ListView):
    # modelo del que sacara los objetos
    model = SubsidioGasLicuado
    # vista a utilizar
    template_name = 'subsidioGas/lista.html'

    # sobreescribir con decoradores, solicitando que este logeado para entrar a esta pagina
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscardatos':
                data = []
                for i in SubsidioTransporte.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['subtitulo'] = 'Datos subisidio gas licuado'
        context['titulo'] = 'Subsidios gas lucuado'

        return context

    def get_queryset(self):
        return SubsidioGasLicuado.objects.all()


class SubsidioGasCreateView(CreateView):
    model = SubsidioGasLicuado
    form_class = SubsidioGasForm
    template_name = 'subsidioGas/create.html'
    success_url = reverse_lazy('home:homepage')

    def post(self, request, *args, **kwargs):
        data = {}
        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Formulario | Subsudio gas licuado'
        context['titulo'] = 'Formulario| Subsidio gas licuado'
        context['action'] = 'add'
        return context


class SubsidioGasUpdateView(UpdateView):
    model = SubsidioGasLicuado
    form_class = SubsidioGasEditForm
    template_name = 'subsidioGas/edit.html'
    success_url = reverse_lazy('apps:subsidio_gas_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Edición subsidio gas licuado'
        context['lista_url'] = reverse_lazy('apps:subsidio_gas_lista')
        return context


class SubsidioGasDeleteView(DeleteView):
    model = SubsidioGasLicuado
    template_name = 'subsidioGas/delete.html'
    success_url = reverse_lazy('apps:subsidio_gas_lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['titulo'] = 'Eliminación subsidio gas licuado'
        context['lista_url'] = reverse_lazy('apps:subsidio_gas_lista')
        return context

    def delete(self, request, *args, **kwargs):
        try:
            return super(SubsidioGasDeleteView, self).delete(request, *args, **kwargs)
        except models.ProtectedError as error:
            return HttpResponseForbidden('Este subsidio esta relacionado con un solicitud')


# Administrador
'''
class AdministradorCreateView(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'Administrador/create.html'
    success_url = reverse_lazy('apps:dashboard')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Fomulario | Creación administrador'
        context['panel'] = 'Panel Administrador'
        return context
'''

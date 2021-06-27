from django.contrib import admin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict


# Create your models here.
from django.http import HttpResponseForbidden

from primer_proyecto.settings import MEDIA_URL, STATIC_URL


class Departamento(models.Model):
    nombre = models.CharField(max_length=25,verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Depatamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamento'
        ordering = ['nombre']

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    codigo_postal = models.CharField(primary_key=True,max_length=5,verbose_name='Codigo postal')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        db_table = 'municipios'
        ordering = ['departamento','nombre']

class Usuario(models.Model):
    sexo = (('femenino','Femenino'),
            ('masculino','Masculino'),
            ('otro','Otro')
            )
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Municipio')
    dui = models.CharField(max_length=10,verbose_name='DUI',primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='Nombres')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    sexo = models.CharField(max_length=15,verbose_name='Sexo',choices=sexo)
    correo = models.EmailField(verbose_name='Correo electronico',null=True,blank=True)
    telefono = models.CharField(max_length=9,verbose_name='Telefono',null=True,blank=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    direccion = models.CharField(max_length=150,verbose_name='Direccion')

    def __str__(self):
        return self.nombre +" "+ self.apellido

    def toJSON(self):
        item = model_to_dict(self,exclude=['apellido','nombre','sexo','correo','telefono','fecha_nacimiento','departamento','municipio','direccion'])
        return item

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'

class SubsidioTransporte(models.Model):
    frecuenciaUso = (('diaramente', 'Diaramente'),
                    ('semanalmente', 'Semanalmente'),
                    ('mensualmente', 'Mensualmente')
            )
    #atributo
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad Subsidio',null=True,blank=True)
    cantidad_buses = models.IntegerField(verbose_name='Cantidad buses')
    cantidad_microbuses = models.IntegerField(verbose_name='Cantidad microbuses')
    frecuencia_uso = models.CharField(max_length=50,verbose_name='Frecuencia uso',choices=frecuenciaUso)

    def toJSON(self):
        item = model_to_dict(self,exclude=['cantidad_buses','cantidad_microbuses','frecuencia_uso'])
        return item

    def __str__(self):
        return 'Subsidio transporte,' +str(self.pertenece)

    def calcularCantidadSubsidio(cantidadBuses, cantidadMicrobuses, frecuenciaUso):
        cantidad = 0
        if frecuenciaUso == 'diaramente':
            cantidad = ((cantidadBuses * 0.04) * 30) + ((cantidadMicrobuses * 0.02) * 30)
        elif frecuenciaUso == 'semanalmente':
            cantidad = ((cantidadBuses * 0.04) * 4) + ((cantidadMicrobuses * 0.02) * 4)
        else:
            cantidad = (cantidadBuses * 0.04) + (cantidadMicrobuses * 0.02)
        return cantidad



    class Meta:
        verbose_name = 'Subsidio transporte'
        verbose_name_plural = 'Subsidios transporte'
        db_table = 'subsidio_transporte'
        ordering = ['id']

class SubsidioAgua(models.Model):
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.FloatField(verbose_name='Cantidad subsidiada',null=True,blank=True)
    cantidad_consumo = models.FloatField(verbose_name='Cantidad consumida',help_text='cantidad de consumo en metros cubicos')
    recibo_agua = models.ImageField(upload_to='recibosAgua/%Y/%m/%d/',null=True)
    verificado = models.BooleanField(verbose_name='Verificado',default=False,help_text='Seleccione si ya reviso la información del usuario')
    aprobado = models.BooleanField(verbose_name='Aprobación',default=False,help_text='Seleccione si la información brindada es correcta')

    def __str__(self):
        return 'Subsidio agua,' +str(self.pertenece)

    def get_image(self):
        if self.recibo_agua:
            return '{}{}'.format(MEDIA_URL,self.recibo_agua)
        return  '{}{}'.format(STATIC_URL,'img/vacio.png')

    def calcularCantidadSubsidioAgua(cantidad_consumida):
        PRECIO_UNITARIO_METRO_CUBICO_AGUA = 0.85
        cantidad_subsidida = 0
        if cantidad_consumida <= 2:
            cantidad_subsidida = 0.0
        elif cantidad_consumida <= 10:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - 2.29
        elif cantidad_consumida <= 20:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.21)
        elif cantidad_consumida == 21:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.250)
        elif cantidad_consumida == 22:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.280)
        elif cantidad_consumida == 23:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.310)
        elif cantidad_consumida == 24:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.340)
        elif cantidad_consumida <= 30:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.370)
        elif cantidad_consumida == 31:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.420)
        elif cantidad_consumida == 32:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.480)
        elif cantidad_consumida == 33:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.540)
        elif cantidad_consumida == 34:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.640)
        elif cantidad_consumida <= 40:
            cantidad_subsidida = (cantidad_consumida * PRECIO_UNITARIO_METRO_CUBICO_AGUA) - (cantidad_consumida * 0.760)
        else:
            cantidad_subsidida = 0.0

        return round(cantidad_subsidida,2)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Subsidio agua'
        verbose_name_plural = 'Subsidios agua'
        db_table = 'subsidio_agua'
        ordering = ['id']

class SubsidioLuz(models.Model):
    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad subsidiada',null=True,blank=True)
    cantidad_consumo = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad consumida',help_text='cantidad de consumo en kilowatts por hora')
    recibo_luz = models.ImageField(upload_to='recibosLuz/%Y/%m/%d/',null=True)
    verificado = models.BooleanField(verbose_name='Verificado', default=False,
                                     help_text='Seleccione si ya reviso la información del usuario')
    aprobado = models.BooleanField(verbose_name='Aprobación', default=False,
                                   help_text='Seleccione si la información brindada es correcta')

    def __str__(self):
        return 'Subsidio luz,' +str(self.pertenece)

    def get_image(self):
        if self.recibo_luz:
            return '{}{}'.format(MEDIA_URL,self.recibo_luz)
        return  '{}{}'.format(STATIC_URL,'img/vacio.png')

    def calcularCantidadSubsidio(cantidadConsumo):
        cantidad = 0
        if cantidadConsumo <= 105:
            cantidad = 5.0
        return cantidad
    class Meta:
        verbose_name = 'Subsidio luz'
        verbose_name_plural = 'Subsidios luz'
        db_table = 'subsidio_luz'
        ordering = ['id']

class SubsidioGasLicuado(models.Model):

    #Lista para la seleccion del tipo de establecimiento
    tipoEstablecimiento = (
        ('Hogar familiar','Hogar'),
        ('Negocio subsistencia',(
                                ('tortilleria','Tortillería'),
                                ('pupuseria','Pupusería'),
                                ('panaderia','Panadería'))
         )
    )

    pertenece = models.OneToOneField(Usuario, on_delete=models.PROTECT,verbose_name='Benefeciario',unique=True)
    cantidad_subsidio = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad subsidioTransporte',null=True,blank=True)
    cantidad_consumo = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Cantidad consumida',help_text='cantidad de consumo en kilowatts por hora')
    tipo_establecimiento = models.CharField(max_length=50,verbose_name='Tipo beneficiario',choices=tipoEstablecimiento)
    num_tarjeta = models.CharField(max_length=10,verbose_name='Numero tarjeta',null=True,blank=True)
    recibo_luz = models.ImageField(upload_to='recibosGas/%Y/%m/%d/',null=True)
    verificado = models.BooleanField(verbose_name='Verificado', default=False,
                                     help_text='Seleccione si ya reviso la información del usuario')
    aprobado = models.BooleanField(verbose_name='Aprobación', default=False,
                                   help_text='Seleccione si la información brindada es correcta')

    def calcularCantidadSubsidio(cantidadConsumo,establecimiento):
        SUBSIDIO_BASE = 8.04
        if establecimiento == 'Hogar':
            if cantidadConsumo <= 309.99:
                cantidad = SUBSIDIO_BASE = 8.04
            else:
                cantidad = 0.0
        elif establecimiento == 'panaderia':
            if cantidadConsumo <= 309.99:
                cantidad = (SUBSIDIO_BASE * 4)
            else:
                cantidad = 0.0
        else:
            if cantidadConsumo <= 309.99:
                cantidad = (SUBSIDIO_BASE  * 2)
            else:
                cantidad = 0.0
        return cantidad

    def get_recibo_luz(self):
        if self.recibo_luz:
            return '{}{}'.format(MEDIA_URL, self.recibo_luz)
        return '{}{}'.format(STATIC_URL, 'img/vacio.png')

    def __str__(self):
        return 'Subsidio gas licuado, ' +str(self.pertenece)

    class Meta:
        verbose_name = 'Subsidio gas licuado'
        verbose_name_plural = 'Subsidios gas licuado'
        db_table = 'subsidio_gas'
        ordering = ['id']

@receiver(post_save, sender=SubsidioAgua)
def set_cantidad_subsidio_agua_field(sender, instance, **kwargs):
    if kwargs.get('created'):
        sender.objects.filter(id=instance.id).update(cantidad_subsidio=SubsidioAgua.calcularCantidadSubsidioAgua
        (instance.cantidad_consumo))


@receiver(post_save, sender=SubsidioTransporte)
def set_cantidad_subsidio_transporte_field(sender, instance, **kwargs):
    if kwargs.get('created'):
        sender.objects.filter(id=instance.id).update(cantidad_subsidio=SubsidioTransporte.calcularCantidadSubsidio
        (instance.cantidad_buses,instance.cantidad_microbuses,instance.frecuencia_uso))


@receiver(post_save, sender=SubsidioLuz)
def set_cantidad_subsidio_luz_field(sender, instance, **kwargs):
    if kwargs.get('created'):
        sender.objects.filter(id=instance.id).update(cantidad_subsidio=SubsidioLuz.calcularCantidadSubsidio
        (instance.cantidad_consumo))

@receiver(post_save, sender=SubsidioGasLicuado)
def set_cantidad_subsidio_gas_field(sender, instance, **kwargs):
    if kwargs.get('created'):
        sender.objects.filter(id=instance.id).update(cantidad_subsidio=SubsidioGasLicuado.calcularCantidadSubsidio
        (instance.cantidad_consumo, instance.tipo_establecimiento))

from django.db import models
from django.utils import timezone


class Telefone(models.Model):

    ddd = models.CharField('DDD', max_length=2)
    numero = models.CharField('Numero', max_length=9)
    setor = models.CharField('Setor', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"

    def __str__(self):
        return '(%s) - %s' % (self.ddd, self.numero)


class Endereco(models.Model):

    rua = models.CharField('Rua', max_length=150)
    numero = models.CharField('Número', max_length=6)
    complemento = models.CharField('Complemento', max_length=50)
    bairro = models.CharField('Bairro', max_length=50)
    cep = models.CharField('Cep', max_length=8)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('País', max_length=50)
    referencia = models.CharField(
        'Referência', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return '%s, Número: %s %s' % (self.rua, self.numero, self.complemento)


class Condominio(models.Model):

    nome = models.CharField('Nome', max_length=150)
    endereco = models.ForeignKey(Endereco)
    telefone = models.ForeignKey(Telefone, blank=True, null=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Condomínio"
        verbose_name_plural = "Condomínios"

    def __str__(self):
        return self.nome

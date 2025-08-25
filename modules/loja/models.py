# Arquivo: modules/loja/models.py

from django.db import models

class Espelho(models.Model):
    """
    Modelo para representar um espelho na loja.
    """
    nome = models.CharField(max_length=200, verbose_name="Nome ou Modelo")
    descricao = models.TextField(blank=True, verbose_name="Descrição Detalhada")
    largura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Largura (cm)")
    altura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Altura (cm)")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        """Retorna uma representação em string do objeto."""
        return self.nome

    class Meta:
        verbose_name = "Espelho"
        verbose_name_plural = "Espelhos"
        ordering = ['nome']

class FotoEspelho(models.Model):
    """
    Modelo para armazenar as fotos de cada espelho.
    """
    espelho = models.ForeignKey(
        Espelho,
        on_delete=models.CASCADE,
        related_name='fotos',
        verbose_name="Espelho"
    )
    imagem = models.ImageField(
        upload_to='espelhos/galeria/',
        verbose_name="Imagem"
    )
    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordem de exibição"
    )

    def __str__(self):
        """Retorna uma representação em string da foto."""
        return f"Foto de {self.espelho.nome} (Ordem: {self.ordem})"

    class Meta:
        verbose_name = "Foto do Espelho"
        verbose_name_plural = "Fotos dos Espelhos"
        ordering = ['ordem']
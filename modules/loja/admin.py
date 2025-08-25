# Arquivo: modules/loja/admin.py

from django.contrib import admin
from .models import Espelho, FotoEspelho

# 1. Cria uma classe Inline para o modelo FotoEspelho
# Isso permite que você edite as fotos na mesma tela que o Espelho
class FotoEspelhoInline(admin.TabularInline):
    model = FotoEspelho
    extra = 1  # O número de formulários extras vazios que aparecem
    # Opcional: define os campos visíveis e a ordem
    fields = ('imagem', 'ordem',)

# 2. Configura a classe de administração do Espelho
@admin.register(Espelho)
class EspelhoAdmin(admin.ModelAdmin):
    # Adiciona a classe inline aqui
    inlines = [FotoEspelhoInline]

    list_display = ('nome', 'largura', 'altura', 'preco')
    search_fields = ('nome', 'descricao')
    ordering = ('nome',)

# 3. Não precisa mais registrar o modelo FotoEspelho separadamente, pois ele está no Inline
# admin.site.register(FotoEspelho) # Pode remover esta linha se tiver
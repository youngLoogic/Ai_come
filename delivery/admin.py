from django.contrib import admin
from .models import Restaurante #, Pedido, ItemPedido, Produto
from .forms import RestauranteForm #, PedidoForm, ItemPedidoForm, ProdutoForm
# Register your models here.

class RestauranteAdmin(admin.ModelAdmin):
    model = Restaurante
    form = RestauranteForm

# class PedidoAdmin(admin.ModelAdmin):
#     model = Pedido
#     form = PedidoForm
#     readonly_fields=('valor_total',)

# class ItemPedidoAdmin(admin.ModelAdmin):
#     model = ItemPedido
#     form = ItemPedidoForm
#     readonly_fields=('valor_total',)

# class ProdutoAdmin(admin.ModelAdmin):
#     model = Produto
#     form = ProdutoForm

admin.site.register(Restaurante, RestauranteAdmin)
# admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(ItemPedido, ItemPedidoAdmin)
# admin.site.register(Produto, ProdutoAdmin)
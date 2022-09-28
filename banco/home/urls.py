from django.urls import path
from . import views
from rest_framework_nested import routers


rota = routers.DefaultRouter()

rota.register('usuario', views.UsuarioViewSet)
rota.register('endereco', views.EnderecoViewSet)
rota.register('tipo_cliente', views.TipoClienteViewSet)
rota.register('cliente', views.ClienteViewSet)
rota.register('transferencia', views.TransferenciaViewSet)
rota.register('conta', views.ContaViewSet)
rota.register('bandeira', views.BandeiraViewSet)
rota.register('cartao', views.CartaoViewSet)
rota.register('emprestimo', views.EmprestimoViewSet)
rota.register('pgto_emprestimo', views.PgtoEmprestimoViewSet)
rota.register('extrato', views.ExtratoViewSet)
rota.register('fatura', views.FaturaViewSet)
rota.register('imagens', views.ImagemViewSet)
rota.register('adiconar-imagens', views.AdicionarImagemViewSet)

urlpatterns= rota.urls
from django.shortcuts import render
from rest_framework import viewsets
from .models import Bandeiras, Cartoes, Cliente, Conta, Emprestimos, Endereco, Extrato, Fatura, Imagem, Pgto_Emprestimos, Tipos_cliente, Transferencia, Usuario
from .serializer import BandeiraSerializer, CartaoSerializer, ClienteSerializer, ContaSerializer, EmprestimoSerializer, EnderecoSerializer, ExtratoSerializer, FaturaSerializer, ImagemSerializer, PgtoEmprestimoSerializer, TipoClienteSerializer, TransferenciaSerializer, UserSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class TipoClienteViewSet(viewsets.ModelViewSet):
    queryset = Tipos_cliente.objects.all()
    serializer_class = TipoClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    
class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class BandeiraViewSet(viewsets.ModelViewSet):
    queryset = Bandeiras.objects.all()
    serializer_class = BandeiraSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartaoSerializer
    
class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimoSerializer
       
class PgtoEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Pgto_Emprestimos.objects.all()
    serializer_class = PgtoEmprestimoSerializer

class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
       

    





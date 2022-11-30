from dataclasses import fields
from rest_framework import serializers
from .models import Bandeiras, Cartoes, Cliente, Conta, Emprestimos, Endereco, Extrato, Fatura, Imagem, Pgto_Emprestimos, Tipos_cliente, Transferencia, Usuario, PedidoCartao
from pictures.contrib.rest_framework import PictureField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nome','email','cpf','senha', 'bloqueio_acesso']

class PedidoCartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoCartao
        fields = ['id','nome', 'email', 'telefone', 'cidade', 'cpf', 'salario', 'senha']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','rua','numero','bairro','cidade','estado']
    
class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipos_cliente
        fields = ['id','tipo_cliente']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nome','email','data_nascimento','endereco','cod_usuario','data_cadastro','tipo_cliente']

class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = ['id','remetente','destinatario','valor','horario_transferencia','data_transferencia']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id','numero','agencia','tipo_cliente','cod_cliente']

class BandeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeiras
        fields = ['id','tipo_bandeira']

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartoes
        fields = ['id','numero_cartao','limite','cartao_fisico','cod_conta','bandeira','data_vencimento']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = ['id','cod_cliente','valor_emprestimo','juros','valor_parcelas','numero_parcelas','aprovado','pagamento_correto','data_emprestimo','horario_emprestimo']
        
class PgtoEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pgto_Emprestimos
        fields = ['id','cod_emprestimos','data_vencimento','data_pagamento']

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['id','cod_conta','operacao','valor','data_extrato','horario_extrato']

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = ['id','cod_cartao','valor_fatura']

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'titulo', 'foto']
        
    foto = PictureField()
    
class AdicionarImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'titulo', 'foto']
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cpf', 'senha']

        
        
        
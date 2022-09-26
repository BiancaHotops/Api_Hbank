from distutils.command.upload import upload
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Usuario (models.Model):
    cpf= models.CharField(max_length=11)
    senha = models.CharField(max_length= 15,
        validators=[MinValueValidator(6, message='O mínimo é 6 digitos'), MaxValueValidator(15, 'O máximo é 15 digitos')]
    )
    bloqueio_acesso = models.BooleanField()
    
    def __str__(self):
        return self.cpf

class Endereco (models.Model):
    rua = models.CharField(max_length=100)
    numero = models.PositiveSmallIntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return self.rua

class Tipos_cliente (models.Model):
    
    Assinatura_Basico = 'B'
    Assinatura_Gold = 'G'
    Assinatura_Platinum = 'P'
  
    Assinatura_Tipos = [ 
        (Assinatura_Basico, 'Basic'),
        (Assinatura_Gold, 'Gold'),
        (Assinatura_Platinum, 'Platinum'),
        
    ]
    
    tipo_cliente = models.CharField(max_length=1, choices=Assinatura_Tipos, default=Assinatura_Basico)
    
    
class Cliente (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    tipo_cliente = models.ForeignKey(Tipos_cliente, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome

class Transferencia (models.Model):
    remetente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='remetente')
    destinatario = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='destinatario')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    horario_transferencia = models.TimeField(auto_now_add=True)
    data_transferencia = models.DateField(auto_now_add=True)

class Conta (models.Model):
    numero = models.CharField(max_length=50)
    agencia = models.CharField(max_length=20)
    tipo_cliente = models.ForeignKey(Tipos_cliente, on_delete=models.PROTECT)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
class Bandeiras (models.Model):
    
    Bandeira_Visa = 'V'
    Bandeira_Mastercard = 'M'
    Bandeira_Elo = 'E'
    Bandeira_Hipercard = 'H'
  
    Tipos_Bandeira = [ 
        (Bandeira_Visa, 'Visa'),
        (Bandeira_Mastercard, 'MasterCard'),
        (Bandeira_Elo, 'Elo'),
        (Bandeira_Hipercard, 'Hipercard'),
     
    ]
    
    tipo_bandeira = models.CharField(max_length=1, choices=Tipos_Bandeira, default=Bandeira_Visa)
    

class Cartoes (models.Model):
    numero_cartao = models.CharField(max_length=25)
    limite = models.DecimalField(max_digits=6, decimal_places=2)
    cartao_fisico = models.BooleanField()
    cod_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    bandeira = models.ForeignKey(Bandeiras, on_delete=models.PROTECT)
    data_vencimento = models.DateField()

class Emprestimos (models.Model):
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    juros = models.DecimalField(max_digits=5, decimal_places=2)
    valor_parcelas = models.DecimalField(max_digits=6, decimal_places=2)
    numero_parcelas = models.PositiveSmallIntegerField()
    aprovado = models.BooleanField()
    pagamento_correto = models.BooleanField()
    data_emprestimo = models.DateField(auto_now_add=True)
    horario_emprestimo = models.TimeField(auto_now_add=True)
    
class Pgto_Emprestimos (models.Model):
    cod_emprestimos = models.ForeignKey(Emprestimos, on_delete=models.CASCADE)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    
class Extrato (models.Model):
    cod_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    operacao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_extrato = models.DateField(auto_now_add=True)
    horario_extrato = models.TimeField(auto_now_add=True)
    
class Fatura (models.Model):
    cod_cartao = models.ForeignKey(Cartoes, on_delete=models.PROTECT)
    valor_fatura = models.DecimalField(max_digits=6, decimal_places=2)

class Imagem(models.Model):
    titulo = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='home/imagens')
    

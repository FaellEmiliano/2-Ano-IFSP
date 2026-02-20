class conta:
  def __init__(self,saldo,dono) -> None:
    self.saldo = saldo
    self.dono = dono

  def debito(self,valor):
    if valor> self.saldo:
      print("saldo insuficiente")
    else:
      self.saldo -= valor

  def deposito(self,valor):
    self.saldo += valor

  def mostrar(self):
   print(f"Nome: {self.dono}")
   print(f"Saldo: R${self.saldo}") 






class conta_menor(conta):
  def __init__(self, saldo, dono,responsavel) -> None:
    super().__init__(saldo, dono)
    self.responsavel = responsavel

  def mostrar(self):
    super().mostrar()
    print(f"responśavel: {self.responsavel}")






class conta_adulta(conta):
  def __init__(self, saldo, dono,limite) -> None:
    super().__init__(saldo, dono)
    self.limite = limite
    self.divida = 0
  def credito(self,valor):
    if valor > self.limite:
      escolha = input("Sem limite no cartão! Deseja se endividar? (s/n): ")
      if escolha == "s":
        self.divida -= self.limite-valor
    else:
      self.limite -= valor
  def mostrar(self):
    super().mostrar()
    print(f"limite: R${self.limite}\nDívida: {self.divida}")






class pessoa:
  def __init__(self,nome,idade,mae) -> None:
    self.nome = nome
    self.idade = idade
    self.mae = mae
  def criar_conta(self):
    if self.idade >= 18:  
      self.conta_pessoal = conta_adulta(0,self.nome,1000)
    else:
      self.conta_pessoal = conta_menor(0,self.nome,self.mae)
  def trabalhar(self,horas):
    salario = 7.37
    self.conta_pessoal.deposito(salario*horas)



rafael = pessoa("Rafael",20,"ana")
rafael.criar_conta()
rafael.conta_pessoal.mostrar()
rafael.trabalhar(10)
rafael.conta_pessoal.mostrar()
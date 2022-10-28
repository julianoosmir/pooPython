from ContaBancaria import ContaBancaria

contaBancaria = ContaBancaria()
contaBancaria.depositar(10)
print(contaBancaria.ObterSaldoFormatado())
print(contaBancaria.ObterDataAberturaFormatada())


contaBancaria.sacar(9)
contaBancaria.sacar(10)
print(contaBancaria.ObterSaldoFormatado())
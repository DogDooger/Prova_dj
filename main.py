from Classes import ContaLuz,Contas

historicoContas = Contas()

historicoContas.addcontaLuz(ContaLuz("125","001",121))
historicoContas.addcontaLuz(ContaLuz("135","002",311))
historicoContas.addcontaLuz(ContaLuz("565","003",441))
historicoContas.addcontaLuz(ContaLuz("655","004",111))
print(historicoContas.mediaConsumoValor())
from DocumentoCPF import DocumentoCPF

try:

    cpf = DocumentoCPF("02486484540")
    cfp_valido = cpf.validarCPF(cpf.cpf)
    print(cpf)

except ValueError as e:
    print(e)

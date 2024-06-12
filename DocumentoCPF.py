from validate_docbr import CPF as CPFValidator

# Definindo a classe do CPF
class DocumentoCPF:

    # Ao iniciar o código, o mesmo transforma o número do CPF em sting e o adiciona ao documento, além de tratar o erro em caso de CPF inválido
    def __init__(self, documento):
        documento = str(documento)
        
        # Verifica se o CPF é válido ou não
        if self.validarCPF(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")
    

    # Verifica se o CPF possui 11 digitos
    def validarCPF(self, cpf):
        if len(cpf) == 11:
            validador = CPFValidator()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    # Função para formatar o CPF em 999.999.999-99   
    def format_cpf(self):
        mascara = CPFValidator()
        return mascara.mask(self.cpf)
    
    # Formata o CPF e o leva ao documento
    def __str__(self):
        return self.format_cpf()
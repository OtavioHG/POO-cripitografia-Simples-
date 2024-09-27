class CifraCesar:
    def __init__(self, chave):
        self.chave = chave

    def criptografar(self, texto, chave=None):
        if chave is None:  # Aqui ele vai pegar a numeração de troca dos caracteres. Se for vazio/None, ele vai colocar a troca inicial dos caracteres.
            chave = self.chave  # Pegando o número oficial dos caracteres.

        resultado = ""  # Iniciando a variável resultado.
        for i in texto:  # O laço for vai percorrer todos os caracteres do texto.
            if i.isalpha():  # Aqui ele vai verificar se o caractere é letra.
                deslocamento = 65 if i.isupper() else 97  # Aqui ele vai verificar se o caractere é maiúsculo ou minúsculo de acordo com a tabela ASCII.
                resultado += chr((ord(i) + chave - deslocamento) % 26 + deslocamento)  # Aqui ele fará o deslocamento dos caracteres de acordo com a tabela ASCII.

            elif i.isnumeric():  # Aqui vai fazer a verificação se é um número o caractere.
                deslocamentonum = 48  # Aqui vai ser o início do deslocamento de acordo com o primeiro número da tabela ASCII.
                resultado += chr((ord(i) + chave - deslocamentonum) % 10 + deslocamentonum)  # Aqui ele vai alterar os números de acordo com a tabela ASCII.

            else:  # Se nenhum dos requisitos for atendido, vai adicionar o caractere normalmente.
                resultado += i

        return resultado  # Retorna o resultado.

    def descriptografar(self, texto): 
        return self.criptografar(texto, -self.chave)  # Ele vai inverter os valores; por exemplo, se for 3, vai virar -3. Isso vai fazer o processo inverso.

# Uso da Cifra de César
cifra = CifraCesar(3)  # Escolhe o número da criptografia que vai ser usada, fazendo a substituição dos caracteres.
texto_original = "Seguranca111@"  # Aqui vamos escolher um texto que vai ser criptografado.
texto_criptografado = cifra.criptografar(texto_original)
print(f"Texto criptografado: {texto_criptografado}")

# Descriptografar o texto
texto_descriptografado = cifra.descriptografar(texto_criptografado)
print(texto_descriptografado)

#transforma apenas a primeira letra de uma string em em maiuscula
nome="isabella"
print(nome.capitalize(),"\n") 

#tranforma todas as letras em minuscula
nome="ISABELLA"
print(nome.casefold(),"\n") 

#conta o numero de vezes que um caractere especifico aparece na string
nome="isabellacarolina@gmail.com"
print(nome.count('l'),"\n")

#retorna true (verdadeiro) ou false (falso) para um teste se a string termina com uma string especifica
nome="isabellacarolina@gmail.com"
print(nome.endswith('gmail.com'),"\n")

#encontra a posição do termo procurado, lembre-se começa do zero
nome="isabellacarolina@gmail.com"
print(nome.find('@'),"\n")

#verifica se o texto é todo feito com letras
nome="isabella"
print(nome.isalpha(),"\n")

#substitui um caractere escolhido por outro.
nome="isabella"
print(nome.replace('a','e'),"\n")

#separa texto string baseado em algum caractere indicado.
nome="isabella @ vinicius"
print(nome.split('@'),"\n")

#colocar todas as letras iniciais em maiusculas
nome="Isabella Carolina de Souza"
print(nome.title(),"\n")

#retira os caracteres indesejados, como por exemplo espaços que não agregam valor
nome=" Isabella Carolina de Souza"
print(nome.strip(),"\n")

#retorna true ou false para um teste de uma string se inicia com um texto especifico
nome=" Isabella 2009"
print(nome.startswith("isa"),"\n")
print(nome.startswith("Isa"),"\n")
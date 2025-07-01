
print("Apolo Leonardi Bastos ; RA: 1051392421009")
print("Reinaldo Gomes de Sousa ; RA: 1051392421007")
print()


#primeiro declaramos os Arrays para amarzenas os candidatos e eleitores
candidatos = []
eleitores = []


#Declaramos a classe pessoa com atributos presentes em qualquer pessoa idependente de ser candidato ou eleitor
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def mostrar(self): # <-- Aqui implementamos o polimorfismo
        print(f"Nome: {self.nome}; CPF: {self.cpf}")
    
            
        
    

#Na classe candidato foi adicionado os atributos cod_candidato (para que o eleitor possa escolher de forma mais facil um candididato para votar) e qntVotos (a quantidade de votos que cada candidato recebeu)

class Candidato(Pessoa):
    def __init__(self, nome, cpf, cod_candidato, qntVotos):
        super().__init__(nome, cpf)
        self._cod_candidato = cod_candidato
        self.qntVotos = qntVotos
        qntVotos = 0
        
    def mostrar(self):
        print(f"Nome: {self.nome}; CPF: {self.cpf}; Código: {self._cod_candidato}; Votos: {self.qntVotos}")


#Declaramos uma função para que o usuário possa cadastrar candidatos de acordo com a necessidade, com restrições para que não tenham candidatos com o mesmo CPF e codigo

def cadastrarCandidato():
    try:
        nome = input("Insira o nome do candidato: ")
        cpf = input("Insira o CPF do candidato (Apenas 11 números): ")
        if not cpf.isdigit() or len(cpf) != 11:
            print()
            print("--ERRO--")
            print("CPF inválido! Deve conter exatamente 11 números.")
            print()
            return False
        
        
        for candidato in candidatos:
            if candidato.cpf == cpf:
                print()
                print("CPF já cadastrado...")
                print()
                return
            
        cod_candidato = input("Insira o codigo de votação do candidato (5 números): ")
        if not cod_candidato.isdigit() or len(cod_candidato) != 5:
            print()
            print("--ERRO--")
            print("Código inválido, deve conter apenas 5 números!")
            print()
            return False
        
        
        for candidato in candidatos:
            if candidato.cod_candidato == cod_candidato:
                print()
                print("--ERRO--")
                print("Esse códido já está em uso!")
                print()
                return
        
        novo = Candidato(nome, cpf , cod_candidato, 0)
        candidatos.append(novo)
        print()
        print("Candidato cadastrado com sucesso!")
        print()
        
    except Exception as e:
        print("--ERRO--")
        print("Erro ao cadastrar candidato!")


#Aqui declaramos a classe eleitor que herda o nome e cpf da classe primária "Pessoa"
class Eleitor(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
    
    def mostrar(self):
        print(f"Nome: {self.nome}; CPF: {self.cpf} (eleitor)") 

#Aqui declaramos a função para cadastrar o eleitor, que do mesmo jeito que a função cadastrarCandidato, possúi restrições, nesse caso para que não tenha como cadastrar um eleitor caso não tenham candidatos, evitando erros na hora da votação e restrições para que eleitores não tenham o mesmo cpf e que o mesmo eleitor não vote mais de uma vez

def cadastrarEleitor():
    try:
        
        
        if len(candidatos) == 0:
            print()
            print("--ERRO--")
            print("Nenhum candidato cadastrado...")
            print()
            return False
            
        nome = input("Insira seu nome: ")
        cpf = input("Insira seu cpf (Apenas 11 números): ")
        
        if not cpf.isdigit() or len(cpf) != 11:
            print()
            print("--ERRO--")
            print("CPF inválido! Deve conter exatamente 11 números.")
            print()
            return False
       
        for eleitor in eleitores:
            if eleitor.cpf == cpf:
                print()
                print("--ERRO--")
                print("Esse CPF já votou! ")
                print()
                return False

        novoEleitor = Eleitor(nome, cpf)
        eleitores.append(novoEleitor)
        return True
        
    except Exception as e:
        print("Erro ao iniciar votação!")
        return False


#Essa função exibe todos os candidatos cadastrados com seus nomes e códigos e imprime uma frase caso não tenham candidatos cadastrados
def mostrarCandidatos():
    if len(candidatos) == 0:
            print()
            print("--ERRO--")
            print("Nenhum candidato cadastrado...")
            print()
    else:
        print()
        print("Candidatos cadastrados: ")
        for i, candidato in enumerate(candidatos, start=1):
            print()
            print(f"{i}° Candidato; Nome = {candidato.nome}; Codigo: {candidato._cod_candidato}")
            print("-")



#Essa função exibe os resultados das votações mostrando o nome dos candidatos e a quantidade de votos
def mostrarResultados():
    if len(candidatos) == 0:
        print()
        print("--ERRO--")
        print("Nenhum candidato cadastrado...")
        print()
    else:
        print()
        print("Resultados das votações: ")
        
        for i, candidato in enumerate(candidatos):
            print()
            print(f"Nome: {candidato.nome}; Quandidade de votos: {candidato.qntVotos}")

#Criamos essa função para permitir que o usuário vote, com restrições para garantir que não tenham votos fantasmas e explique ao usuário o motivo do erro
def votar():
    
    if len(candidatos) == 0:
        print("Nenhum candidato cadastrado...")
        return
        
    try:
        escolha = input("Insira o codigo do candidato que você deseja votar: ")
        
        for candidato in candidatos:
            if candidato._cod_candidato == escolha:
                candidato.qntVotos += 1
                print()
                print(f"Voto registrado para o candidato: {candidato.nome}!")
                print()
                return True
        print()
        print("--ERRO--")
        print("Código invalido!")
        print()
    except Exception as e:
        print("Erro ao votar...")


#Aqui com um loop While criamos o que seria o Menu, onde o usuário terá a opção de votar( Aqui ja deixei embutido o cadastro do eleitor, pois ele só precisa se cadastrar para votar, uma forma também de poupar espaço na hora de garantir que o candidato só receberá um voto por eleitor e que não terá votos fantasmas), Cadastrar candidato, ver os resultados e fechar o programa
while True:
    print("Insira 1 para votar,")
    print("Insira 2 para cadastrar candidato,")
    print("Insira 3 para ver os resultados,")
    print("Insira 4 para mostrar todos os cadastros,")
    print("Insira 5 para sair.")
    opcao = int(input("Insira a opção desejada: "))
    
    if opcao == 1:
        if cadastrarEleitor():
            mostrarCandidatos()
            votar()
            
        
        
    elif opcao == 2:
        cadastrarCandidato()
        
        
    elif opcao == 3: 
        mostrarResultados()
    
    
    elif opcao == 4:
        print("Candidatos:")
        for c in candidatos:
            c.mostrar() 
        print()
        print("Eleitores:")
        for e in eleitores:
            e.mostrar()
        print()
    
    elif opcao == 5:
        print()
        print("Encerrando...")
        print()
        break
    
    
    else:
        print()
        print("Insira uma opção válida...")
        print()
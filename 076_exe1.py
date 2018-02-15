"""
Crie um database de sites permitindo que o usuário
acesse esse database recupere a descriçao de cada site
e tambem coloque novos sites. Tenha certeza que as entradas do
usuário para sites sejam válidas, www.nomedosite.com.br, www.python.org
"""
import struct
import dbm

class ErroIni(Exception):
	def __str__(self):
	    return "Inicie o site com www!\n"

class Minusculo(Exception):
	def __str__(self):
	    return "Todas as palavras devem ser minúsculas!\n"

class SoLetras(Exception):
	def __str__(self):
	    return "O nome do site só pode ser composto por letras!\n"

class Com(Exception):
    def __str__(self):
        return "Deve existir .com após o nome do site!\n"

class Br(Exception):
    def __str__(self):
        return "Deve existir .br após o .com!\n"

class VerificaSite(object):
    def __init__(self, site):
        self.site = site

    def novo_site(self, site):
        self.site = site

    def checa_site(self):
        try:
            self.site_quebra = self.site.split(".")
            for palavra in self.site_quebra:
                if palavra.lower() != palavra:
                    raise Minusculo

            for letra in self.site_quebra[1]:
                if not letra.isalpha():
                    raise SoLetras

            if self.site_quebra[0] != 'www':
                raise ErroIni
            elif self.site_quebra[2] != 'com':
                raise Com
            elif self.site_quebra[3] != 'br':
                raise Br

            print("O site digitado é válido!\n")

            return True

        except ErroIni:
            print(ErroIni())
        except Minusculo:
            print(Minusculo())
        except SoLetras:
            print(SoLetras())
        except Com:
            print(Com())
        except Br:
            print(Br())

class Menu(object):
    def __init__(self):
        self.seleciona_menu()

    def seleciona_menu(self):
        self.escolha = int(input("1) Quer adicionar um novo site ao database?\n2) Quer verificar " \
                             "um site no database?\n3) Quer sair? \nAdicionar - 1 / Verificar - 2" \
                                  " / Sair - 3\n"))
        return self.escolha

class DataBase(object):

    def __init__(self, escolha):
        self.escolha = escolha

        if self.escolha == 1:
            self.adiciona_database()

        elif self.escolha == 2:
            self.verifica_database()

    def adiciona_database(self):
        self.site = input("Digite o site: ")
        verifica = VerificaSite(self.site)
        while  not verifica.checa_site():
            self.site = input("Digite o site: ")
            verifica.novo_site(self.site)

        self.descricao = input("Digite a descrição do site: ")
        db = dbm.open("sites.db", "c")
        db[self.descricao] = self.site
        db.close()

    def verifica_database(self):
        db = dbm.open("sites.db", "r")
        descricao = input("Digite o site que deseja saber o endereço: ")
        if len(db) != 0:
            if descricao in db:
                print(db[descricao].decode())
            else:
                print("Esse site não está cadastrado!\n")
        else:
            print("O arquivo está vazio!\n")
        db.close()

if __name__ == "__main__":
    menu = Menu()
    while menu.escolha != 3:
        data_base = DataBase(menu.escolha)
        menu.seleciona_menu()
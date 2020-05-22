class Client:
    def __init__(self, name, age):
        self.__nomeCliente = name
        self.__idadeCliente = age
        self.__enderecos = []
    def insereEndereco(self, street, city, state, cep):
        address = Address(street, city, state, cep)
        self.__enderecos.append(address)
    def listaEndereco(self):
        count = 1
        for i in self.__enderecos:
            print(
                "Endereço %d: %s, %s-%s. CEP: %s"
                %(count, i.getStreet(), i.getCity(), i.getState(), i.getCep())
            )
            count += 1
            
class Address:
    def __init__(self, street, city, state, cep):
        self.__rua = street
        self.__cidade = city
        self.__estado = state
        self.__cep = cep
    def getStreet(self):
        return self.__rua
    def getCity(self):
        return self.__cidade
    def getState(self):
        return self.__estado
    def getCep(self):
        return self.__cep

client1 = Client("Bruno", 22)
client1.insereEndereco("Rua X", "SRS", "MG", "11111-000")
client1.listaEndereco()
client1.insereEndereco("Rua Y", "SRS", "MG", "11111-000")
client1.listaEndereco()

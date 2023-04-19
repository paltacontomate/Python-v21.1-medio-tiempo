class Mascota:

    # Implementa __init__( name , type , tricks ):
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def Dormir(self):
        self.energy += 50
        return self


    def Comer(self):
        self.energy += 5
        self.health += 10
        return self


    def Jugar(self):
        self.health += 5
        self.energy -= 2
        return self

    def noise(self):
        print(self.noise)

#clase del ninja

class Ninja:
    def __init__(self, first_name, last_name , treats, Mascota_Comida, Mascota):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.Mascota_Comida = Mascota_Comida
        self.Mascota = Mascota

    def Pasear(self):
        self.Mascota.Jugar()
        return self


    def Alimentar(self):

        if len(self.Mascota_Comida) > 0:
            Comida = self.Mascota_Comida.pop()
            print(f"Alimentar al {self.Mascota.name} {Comida}!")
            self.Mascota.Comer()
        else:
            print("¡Oh, no! ¡Necesitas más comida para tus mascotas!")
        return self


    def Bañarse(self):
        self.Mascota.noise()

Comidas = ['Snausage','Bacon',"Trash Bag"]
Mascota_Comida = ['Pizza, Trash bag','Burger, Bacon']

Onix = Mascota("Onix","Horse",['Onix'],"Hey Hey")

Snow = Ninja("Snow","Dion",Comidas,Mascota_Comida, Onix)

Snow.Alimentar();
Snow.Alimentar();
Snow.Alimentar();
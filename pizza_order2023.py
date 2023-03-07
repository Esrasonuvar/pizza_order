import csv
import datetime

class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Classic Pizza"
        self.cost = 10.0


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 12.0


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turkish Pizza"
        self.cost = 15.0


class PizzaDecorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + super().get_description()


class Olive(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Olive"
        self.cost = 2.0


class Mushroom(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mushroom"
        self.cost = 2.5


class GoatCheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Goat Cheese"
        self.cost = 3.0


class Meat(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Meat"
        self.cost = 4.0


class Onion(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Onion"
        self.cost = 1.5


class Corn(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Corn"
        self.cost = 2.0


with open('menu.txt', 'r') as file:
    menu = file.read()
    print(menu)
1
def main():
     
    pizza_choice = int(input("Select a pizza base: "))
    sauce_choice = int(input("Select a sauce: "))

    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkishPizza()
    else:
        pizza = Pizza()

    if sauce_choice == 11:
        pizza = Olive(pizza)
    elif sauce_choice == 12:
        pizza = Mushroom(pizza)
    elif sauce_choice == 13:
        pizza = GoatCheese(pizza)
    elif sauce_choice == 14:
        pizza = Meat(pizza)
    elif sauce_choice == 15:
        pizza = Onion(pizza)
    elif sauce_choice == 16:
        pizza = Corn(pizza)

def get_cost(self):
    return self.component.get_cost() + Pizza.get_cost(self)

def get_description(self):
    return self.component.get_description() + ' ' + Pizza.get_description(self)
def get_cost(self):
    return self.component.get_cost() + 1.5

def get_pizza(pizza_choice):
    # pizza_choice değişkeni ile ilgili işlemler yapılır
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkishPizza()
    else:
        pizza = Pizza()
    return pizza

    pizza = get_pizza(int(pizza_choice))
def get_sauce(sauce_choice):
    if sauce_choice == 11:
        sauce = Olive(Pizza())
    elif sauce_choice == 12:
        sauce = Mushroom(Pizza())
    elif sauce_choice == 13:
        sauce = GoatCheese(Pizza())
    elif sauce_choice == 14:
        sauce = Meat(Pizza())
    elif sauce_choice == 15:
        sauce = Onion(Pizza())
    elif sauce_choice == 16:
        sauce = Corn(Pizza())
    else:
        sauce = sauce(Pizza())
    return sauce
def main():
# Menüyü yazdır
    #print("Menü:")
    with open("Menu.txt", "r") as f:
        menu = f.read()
        print(menu)
    # Pizza ve sos seçimi
pizza_choice = input("Lütfen bir pizza seçin (1-4): ")
while pizza_choice not in ["1", "2", "3", "4"]:
    pizza_choice = input("Lütfen geçerli bir pizza seçin (1-4): ")

sauce_choice = input("Lütfen bir sos seçin (11-16): ")
while sauce_choice not in ["11", "12", "13", "14", "15", "16"]:
    sauce_choice = input("Lütfen geçerli bir sos seçin (11-16): ")



# Pizza ve sos nesnelerini oluştur
pizza = get_pizza(int(pizza_choice))
sauce = get_sauce(int(sauce_choice))

# Toplam fiyatı hesapla
total_cost = pizza.get_cost() + sauce.get_cost()

# Kullanıcı bilgileri
name = input("İsminiz: ")
  
while True:
    try: 
        id_number = int(input("TC Kimlik Numaranız: "))
        if len(str(id_number))!= 11:
             print("Lütfen 11 hane olarak giriş yapın!")
        else:
            break
      
    except:
        print("Lütfen sayı giriniz!")

while True:
    try: 
        credit_card_number = int(input("Kredi Kartı Numaranız: "))
        if len(str(credit_card_number))!= 16:
             print("Lütfen 16 hane olarak giriş yapın!")
        else:
            break
    except:
        print("Lütfen sayılardan oluşan bir kart numarası giriniz!")        

while True:
    try: 
        credit_card_pin = int(input("Kredi Kartı Şifreniz: "))
        if len(str(credit_card_pin))!= 4:
             print("Lütfen 4 hane olarak giriş yapın!")
        else:
            break
    except:
        print("Lütfen sayılardan oluşan bir şifre giriniz!") 


# Sipariş zamanı
#order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Sipariş veritabanına kaydet
# add_order(name, id_number, credit_card_number, credit_card_pin, pizza.get_description() + " " + sauce.get_description(), total_cost)

 
file_name = "Orders_Database.csv"

# Dosyayı aç
with open(file_name, mode="a", newline="") as file:

    # Dosyayı yazma nesnesine bağla
    writer = csv.writer(file)

    # Dosya boşsa, başlık satırını yazdır
    if file.tell() == 0:
        writer.writerow(["Name", "User ID", "Credit dard number", "Credit Card Pin", "Order ", "Sauce", "total cost", "Order Time"])
    # Kullanıcı bilgileri, sipariş bilgileri ve ödeme bilgilerini dosyaya yazdır

        writer.writerow([name, id_number,credit_card_number, credit_card_pin, pizza.get_description() + " " + sauce.get_description(), total_cost, order_time]) 

# Dosyayı kapat
    file.close()

print("Siparişiniz alınmıştır. Teşekkür ederiz!")
if name == 'main':
    main()
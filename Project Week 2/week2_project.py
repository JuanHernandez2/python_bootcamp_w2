import datetime


def save_contacts(contacts):
    
    saving_file = open("Contacts.txt", "w")
    for i in range(0 , len(contacts)):
        saving_file.write(str(i)+"\n")
        saving_file.write(contacts[i].name +"\n")
        saving_file.write(contacts[i].lastname +"\n")
        saving_file.write(str(contacts[i].age)+"\n")
        saving_file.write(str(contacts[i].phone_number)+"\n")
        saving_file.write(contacts[i].email+ "\n")
        saving_file.write(str(contacts[i].date_created) + "\n")
    saving_file.close()
    
class Contact:

    def __init__(self, name, lastname, age, phone_number, email):
            now = datetime.datetime.now()
            self.name = name
            self.lastname = lastname
            self.age = age
            self.phone_number = phone_number
            self.email = email
            self.date_created = now


c = [ ]
name = input("Nombre contacto: ")
lastname = input("Apellido del contacto: ")
age = int(input("Edad del contacto: "))
phone_number = int(input("Ingrese el numero de contacto: "))
email = input("Email del contacto: ")
contacto = Contact(name, lastname, age, phone_number, email)
c.append(contacto)
save_contacts(c)



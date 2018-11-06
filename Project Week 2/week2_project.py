import datetime

class Contact:

    def __init__(self, name, lastname, age, phone_number, email):
            now = datetime.datetime.now()
            self.name = name
            self.lastname = lastname
            self.age = age
            self.phone_number = phone_number
            self.email = email
            self.date_created = now

def create_contact(contacts, c):
        """This function create a new contact with the parameter information and then is
           added to the contact list"""
        contacts.append(c)

def show_sorted_contacts(contacts):
        contacts.sort(key = lambda x: x.microsecond)
        return contacts
        
def save_contacts(contacts):
    """This function save each contact of the parameter list in a file.txt"""
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

def update_contact(contacts, name):
        """This function update a contact with the given name as a parameter"""
        for c in contacts:
                if name == c.name:
                        c.name = input("New name?")
                        c.lastname = input("New lastname?")
                        c.age = input("New age?")
                        c.phone_number = input("New phone number?")
                        c.email = input("New email?")


    



if __name__ == '__main__':
    option = 0
    c = Contact(" ", " ", " ", " ", " ")
    contacts = [ ]
    option_dictionary = {
            "1" : create_contact(contacts,c),
            "2" : show_sorted_contacts(contacts),
            "3" : save_contacts(contacts),
            "4" : update_contact(name),
            "5" : hide_contact(name)
    }  
    while option != 6 :
            print("Choose one number...")
            print("1. Create contact")
            print("2. Show contacts sorted by creation date")
            print("3. Save contacts")
            print("4. Update contact")
            print("5. Hide contact")
            print("6. Exit")
            option = int(input())
            if option == 1:
                    name = input("Contact name")
                    lastname = input("Contact lastname?")
                    age = input("Contact age?")
                    phone_number = input("Contact phone number ?")
                    email = input("Contact email?")
                    c = Contact(name, lastname, age, phone_number, email)
                    option_dictionary[str(option)]
                

            



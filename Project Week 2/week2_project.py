import datetime

class Contact:

    def __init__(self, id, name, lastname, age, phone_number, email):
            now = datetime.datetime.now()
            self.id = id
            self.name = name
            self.lastname = lastname
            self.age = age
            self.phone_number = phone_number
            self.email = email
            self.date_created = now
    
    def __repr_(self):
            return "Name: %s\n Lastname: %s\n Age: %s\n Phone number: %s\n Email: %s\n " % (self.name, self.lastname, self.age, self.phone_number, self.email)

    @classmethod
    def default_contact(cls):
            c = cls(" "," "," ", " ", " "," ")
            return c

class Phone_number():
        
       def __init__(self, *numbers):
            self.contact_numbers = [ ]
            for n in numbers:
                self.contact_numbers.append(n)

       def __str__(self):
               return str(self.contact_numbers)


def create_contact(contacts, c):
        """This function create a new contact with the parameter information and then is
           added to the contact list"""
        contacts.append(c)

def show_sorted_contacts(contacts):
        "This function returns the contact list sorted by the date of creation sorting by microsecond"
        contacts.sort(key = lambda x: x.date_created.microsecond)
        return contacts
        
def save_contacts(contacts):
    """This function save each contact of the parameter list in a file.txt"""
    saving_file = open("Contacts.txt", "w")
    for i in range(0 , len(contacts)):
        saving_file.write(str(i)+"\n")
        saving_file.write(str(contacts[i].id) + "\n")
        saving_file.write(contacts[i].name +"\n")
        saving_file.write(contacts[i].lastname +"\n")
        saving_file.write(str(contacts[i].age)+"\n")
        saving_file.write(str(contacts[i].phone_number)+"\n")
        saving_file.write(contacts[i].email+ "\n")
        saving_file.write(str(contacts[i].date_created) + "\n")
    saving_file.close()

def update_contact(c):
        """This function update a contact with the given name as a parameter"""
        c.name = input("New name?")
        c.lastname = input("New lastname?")
        c.age = input("New age?")
        numbers = [ ]
        flag = "yes"
        while flag == "yes":
                numbers.append(input("Enter a phone number"))
                flag = input("Enter no if you are ready to continue")      
        c.phone_number = Phone_number(numbers)
        c.email = input("New email?")

def generator_hide_contacts(contacts):
        
    id_to_hide = input("Enter contact id to hide ")
    for i in contacts:
        if i.id is not id_to_hide:
            yield i.id
            yield i.name
            yield i.lastname
            yield i.phone_number
            yield i.age
            yield i.email

def hide_contact(contacts):
    g = generator_hide_contacts(contacts)
    while True:
        try:
            print(next(g))
        except StopIteration:
            break

    



if __name__ == '__main__':
    option = 0
    c = Contact.default_contact()
    contacts = [ ]
    
    while option != 6 :
            print("Choose one number...")
            print("1. Create contact")
            print("2. Show contacts sorted by creation date")
            print("3. Save contacts")
            print("4. Update contact")
            print("5. Hide contact")
            print("6. Exit")
            option = int(input())
            option_dictionary = {
                   "1" : create_contact,
                   "2" : show_sorted_contacts,
                   "3" : save_contacts,
                   "4" : update_contact,
                   "5" : hide_contact
                } 
            if option == 1:
                    id = input("Contact id? ")
                    name = input("Contact name? ")
                    lastname = input("Contact lastname? ")
                    age = input("Contact age? ")
                    numbers = [ ]
                    flag = "yes"
                    while flag == "yes":
                         numbers.append(input("Enter a phone number: "))
                         flag = input("Enter no if you are ready to continue or yes to enter another numbers: ")      
                    contact_numbers = Phone_number(numbers)
                    email = input("Contact email? ")
                    c = Contact(id, name, lastname, age, contact_numbers, email)
                    option_dictionary[str(option)](contacts,c)
            elif option == 2:
                    sorted_contacts = option_dictionary[str(option)](contacts)
                    i=0
                    for s in sorted_contacts:
                            print("-------------------"+ str(i) +"---------------")
                            print("Id: " + s.id)
                            print("Name: " + s.name)
                            print("Lastname: " + s.lastname)
                            print("Age: " + s.age)
                            print("Phone number: " + str(s.phone_number))
                            print("Email: " + s.email)
                            print("Creation date: " + str(s.date_created))
                            print("-------------------------------------------\n")
                            i += 1
                    
            elif option == 3:
                    option_dictionary[str(option)](contacts)
            elif option == 4:
                    id = input("Enter contact id to update")
                    contact_to_update = [x for x in contacts if x.id == id]
                    option_dictionary[str(option)](contact_to_update[0])
            elif option == 5: 
                    option_dictionary[str(option)](contacts)
        

                 


            



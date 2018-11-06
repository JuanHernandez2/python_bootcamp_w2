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
            """Class method for creating an empty Contact in a fast way"""
            c = cls(" "," "," ", " ", " "," ") #empty Contact
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
        contacts.sort(key = lambda x: x.date_created.microsecond) #sorting by microsecond
        return contacts
        
def save_contacts(contacts):
    """This function save each contact of the parameter list in a file.txt"""
    saving_file = open("Contacts.txt", "w") #creates a file in write mode
    for i in range(0 , len(contacts)):
        saving_file.write(str(i)+"\n") #contact counter
        saving_file.write(str(contacts[i].id) + "\n") #contact id
        saving_file.write(contacts[i].name +"\n") #contact name
        saving_file.write(contacts[i].lastname +"\n") #contact lastname
        saving_file.write(str(contacts[i].age)+"\n") #contact age
        saving_file.write(str(contacts[i].phone_number)+"\n") #contact phone numbers
        saving_file.write(contacts[i].email+ "\n") #contact email
        saving_file.write(str(contacts[i].date_created) + "\n") #date of creation
    saving_file.close()

def update_contact(c):
        """This function update a contact with the given name as a parameter"""
        c.name = input("New name?")
        c.lastname = input("New lastname?")
        c.age = input("New age?")
        numbers = [ ]
        flag = "yes"
        while flag == "yes": #when the user enters no the loop breaks
                numbers.append(input("Enter a phone number"))
                flag = input("Enter no if you are ready to continue")      
        c.phone_number = Phone_number(numbers)
        c.email = input("New email?")

def generator_hide_contacts(contacts):
    """This generator prints all the contacts except the one that the user wants to hide"""
    id_to_hide = input("Enter contact id to hide ")
    for i in contacts:
        if i.id is not id_to_hide: #if the contact id is different from the one to hide
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
            print(next(g)) #call the generator
        except StopIteration:
            break

    



if __name__ == '__main__':
    option = 0
    c = Contact.default_contact()
    contacts = [ ]
    
    while option != 6 : # when the option is 6 the loops breaks and the module finishes
            print("Choose one number...")
            print("1. Create contact")
            print("2. Show contacts sorted by creation date")
            print("3. Save contacts")
            print("4. Update contact")
            print("5. Hide contact")
            print("6. Exit")
            option = int(input())
            option_dictionary = {  # a dictionary with functions names
                   "1" : create_contact,
                   "2" : show_sorted_contacts,
                   "3" : save_contacts,
                   "4" : update_contact,
                   "5" : hide_contact
                } 
            if option == 1: #create contact
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
                    option_dictionary[str(option)](contacts,c) #calls the function with its parameters
            elif option == 2: #show contacts sorted by creation date
                    sorted_contacts = option_dictionary[str(option)](contacts) #calls the function with its parameters
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
                    
            elif option == 3: #save contacts
                    option_dictionary[str(option)](contacts)#calls the function with its parameters
            elif option == 4: #update contacts
                    id = input("Enter contact id to update")
                    contact_to_update = [x for x in contacts if x.id == id]
                    option_dictionary[str(option)](contact_to_update[0])#calls the function with its parameters
            elif option == 5: #hide contact
                    option_dictionary[str(option)](contacts)#calls the function with its parameters
        

                 


            



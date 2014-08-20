import sys
import os

def create_phonebook(phonebook_name):
    filename = '%s.txt' % phonebook_name
    if os.path.exists(filename):
        raise Exception("That Phonebook already exists!")
    with open(filename, 'w') as f:
        pass    

def add_entry(name, number, phonebook_name):
    if not os.path.exists('%s.txt' % phonebook_name):
        raise Exception("That Phonebook does not exist!")
    with open('%s.txt' % phonebook_name, 'r') as f:
        for line in f: 
            entry_name, entry_number = line.strip().split('\t')
            if entry_name == name:
                raise Exception('That Entry Already Exists! Please use the Update function!')
        
    with open('%s.txt' % phonebook_name, 'a') as f:
        f.write('%s\t%s' % (name, number))
        f.write('\n')
        pass    

def remove_entry(name, phonebook_name):
    name_list = []
    number_list = []
    if not os.path.exists('%s.txt' % phonebook_name):
        raise Exception("That Phonebook does not exist!")
    with open('%s.txt' % phonebook_name, 'r') as f:
        for line in f: 
            entry_name, entry_number = line.strip().split('\t')
            if entry_name != name:
                name_list.append(entry_name)
                number_list.append(entry_number)
                
    with open('%s.txt' % phonebook_name, 'w') as f:
        pass
    for z in range(len(name_list)):
        add_entry(name_list[z], number_list[z], phonebook_name)
        pass

def lookup_entry(name, phonebook_name):
    if not os.path.exists('%s.txt' % phonebook_name):
        raise Exception("That Phonebook does not exist!")
    with open('%s.txt' % phonebook_name, 'r') as f:
        for line in f: 
            entry_name, entry_number = line.strip().split('\t')
            if entry_name == name:
                print entry_name, entry_number
        pass    

def update_entry(name, number, phonebook_name):
    
    name_list = []
    number_list = []
    if not os.path.exists('%s.txt' % phonebook_name):
        raise Exception("That Phonebook does not exist!")
    with open('%s.txt' % phonebook_name, 'r') as f:
        for line in f: 
            entry_name, entry_number = line.strip().split('\t')
            if entry_name != name:
                name_list.append(entry_name)
                number_list.append(entry_number)
                
    with open('%s.txt' % phonebook_name, 'w') as f:
        pass
    for z in range(len(name_list)):
        add_entry(name_list[z], number_list[z], phonebook_name)
    with open('%s.txt' % phonebook_name, 'a') as f:
        f.write('%s\t%s' % (name, number))
        f.write('\n')
        pass        

def reverse_lookup_entry(number, phonebook_name):
    if not os.path.exists('%s.txt' % phonebook_name):
        raise Exception("That Phonebook does not exist!")
    with open('%s.txt' % phonebook_name, 'r') as f:
        for line in f: 
            entry_name, entry_number = line.strip().split('\t')
            if entry_number == number:
                print entry_name, entry_number
        pass   

if __name__ == "__main__":
    arguments = sys.argv[:]
    script = arguments.pop(0)
    if not arguments:
        raise Exception ('Command required')
        
    command = arguments.pop(0)

    if command == "create":
        if not arguments:
            raise Exception ('Phonebook Name required')
            
        phonebook_name = arguments.pop(0)
        create_phonebook(phonebook_name)

    elif command == "add":
        if len(arguments) != 3:
            raise Exception ("Name, Number, Phonebook Name Required.")
            
        name, number, phonebook_name = arguments
        add_entry(name, number, phonebook_name)

    elif command == "update":
        if len(arguments) != 3:
            raise Exception ("Name, Number, Phonebook Name Required.")
            
        name, number, phonebook_name = arguments
        update_entry(name, number, phonebook_name)

    elif command == "remove":
        if len(arguments) != 2:
            raise Exception ("Name, Phonebook Name Required.")
            
        name, phonebook_name = arguments
        remove_entry(name, phonebook_name)

    elif command == "lookup":
        if len(arguments) != 2:
            raise Exception ("Name, Phonebook Name Required.")
            
        name, phonebook_name = arguments
        lookup_entry(name, phonebook_name)

    elif command == "reverse-lookup":
        if len(arguments) != 2:
            raise Exception ("Number, Phonebook Name Required.")
            
        number, phonebook_name = arguments
        reverse_lookup_entry(number, phonebook_name)

    else:
        raise Exception ("Invalid Command.")

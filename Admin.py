
#importing the doctor class from the doctor file 
from Doctor import Doctor 

#list created to work with the logins 


created_admins = []
created_password = []
class Admin :
    def __init__(self, username, password, address):
        self.username = username 
        self.password = password 
        self.address = address
        created_admins.append(self)
    #the view method 
    def view(self, a_list):
         """
        print a list
        Args:
            a_list (list): a list of printables
        """
         for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')


    def login(self):

         """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
         print("-----Login-----")
        #Get the details of the admin

         username = input('Enter the username: ') #username to be inputed 
         password = input('Enter the password: ') #password to be inputed by user 

         for admin in created_admins:
                if (username == admin.username and password == admin.password):
                    print("Login successful")
                    return True
                    break

         else:
                return False
                print("Invalid username or password")

    
    #find_index method 
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
    
    
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
       

        first_name = input("Enter the doctor's first name: ")
        surname = input("Enter the doctor's surname: ")
        speciality = input("Enter the doctor's speciality: ")

        return (first_name, surname, speciality)
        
    def doctor_management(self, doctors):
         """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

         print("-----Doctor Management-----")

        # menu
         print('Choose the operation:')
         print(' 1 - Register')
         print(' 2 - View')
         print(' 3 - Update')
         print(' 4 - Delete')

        #variable op declared to get operartion input
         op = input("Enter the operation : ")
         # register
         if op == '1':
                print("-----Register-----")

                # get the doctor details
                print('Enter the doctor\'s details:')
               
                first_name = input("Enter doctors first name : ")
                surname = input("Enter doctors surname : ")
                speciality = str(input("Enter doctor's speciality "))

                # check if the name is already registered
                name_exists = False
                for doctor in doctors:
                    if (first_name == doctor.get_first_name() and surname == doctor.get_surname()):
                        print('Name already exists.')
                        break
                        
                         
                        #save time and end the loop

                else :                    
                        name_exists = True
                        # while name_exists:
                        
                        new_doc = Doctor(first_name, surname, speciality)
                                
                            #add the doctor ...
                        doctors.append(new_doc)
                                # ... to the list of doctors
                        print('Doctor registered.')

          #view 
         elif op == "2" : 
                print("-----List of Doctors-----")
           
        
                print('ID     |               Fullname             |    speciality')
                for doctor in doctors :
                         print('{:<6} | {:<34} | {:<15}'.format((doctors.index(doctor) + 1), str(doctor.full_name()), str(doctor.get_speciality())))




          # Update
         elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: ')) # make the user input lowercase
            
             

             #for updating te firstname 
            if (op == 1):
                    new_first_name = str(input("Enter the new firstname :  ")).lower()
                    for doctor in doctors :
                        if (doctors.index(doctor) == index ):
                            doctor.set_first_name(new_first_name)
                            break
                    print("Update successful")

            #for updating the surname 
            elif (op == 2):
                    new_surname = str(input("Enter the new S–urname :  ")).lower()
                    for doctor in doctors :
                        if (doctors.index(doctor) == index ):
                            doctor.set_surname(new_surname)
                            break
                    print("Update successful")

            #for updating speciality 
            elif (op == 3):
                    new_speciality = str(input("Enter the new Speciality :  ")).lower()
                    for doctor in doctors :
                        if (doctors.index(doctor) == index ):
                            doctor.set_speciality(new_speciality)
                            break
                    print("Update successful")

        # Delete
         elif op == '4':
              print("-----Delete Doctor-----")
              print('ID |          Full Name           |  Speciality')
              self.view(doctors)
  
              doctor_index = input('Enter the ID of the doctor to be deleted: ')
             
              for doctor in doctors : 
                    if(doctors.index(doctor) == doctor_index):
                        doctors.pop(doctor)
                        print("Doctor deleted succesffuly ")
                        break
              else : 
                    print("Wrong index inputted ")

              print('The id entered is incorrect')

             # if the id is not in the list of patients
         else:
               print('Invalid operation choosen. Check your inpuuted id')
        
    def management_report(self, patients, doctors):
            #getting number of doctors 
            doctor_numbers = 0
            for doctor in doctors:
                    doctor_numbers += 1
            
            #getting number of patient 
            patient_number = 0

            
            #   sample_illnesses = ['malaria', 'fever']
            malaria = 0
            fever = 0

            for patient in patients :
                if patient.print_symptoms ==  "Malaria":
                    malaria =+ 1
                elif patient.print_symptoms == "fever":
                    fever =+ 1
            
            print("---------Management report -------------- ")
            print("Number of doctors : " + str(doctor_numbers))
            print("-----List of Doctors and Patients ---------")

            #this loops print the doctors name and the amount of patients he/she has 
            for doctor in doctors :
                print(doctor.full_name() + " - " + str(len(doctor.get_patient())))

            #this loops prints the amount of appountments per month per doctor 
            print("--------List of Doctors and appointments per month------------")
            #using datetime library 
            import datetime
            for doctor in doctors :
                 print( str(datetime.date.today()) + " " + doctor.full_name() + " - " + str(len(doctor.get_patient())))
            
            #this prints number of patients per illness 
            print("-------List of illness and respective number of patients -----")
            for patient in patients : 
                if patient.print_symptoms().lower() == "malaria":
                    malaria += 1 
                elif patient.print_symptoms().lower() == "fever":
                    fever +=  1
                else : 
                    print("Not found in illness List " + patient.print_symptoms)
            print("Malaria : " + str(malaria))
            print("Fever : " + str(fever))
            
            
    def group_patients(self, patients):

        #dictionary holding patients with same sunrname(the same family)
        family_groups = {}

        for patient in patients :
            surname = patient.get_surname()

            if surname not in family_groups:
                family_groups[surname] = []

            family_groups[surname].append(patient.get_full_name())
        
        print("This are patients from same family")
        print(family_groups)

             
    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print("ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ")
        for index, patient in enumerate(patients):
            print("{:<2} | {:<28} | {:<27} | {:<4} | {:<12} | {:<7}".format(index+1, patient.get_full_name(), patient.get_doctor(), patient.age, patient.mobile, patient.address))

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")
        self.view_patient(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Selection-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #getting date so as to deduce doctors appointment within certain times 
                year = int(input("Enter the year : "))
                month = int(input("Enter the month(1-12) : "))
                day = int(input("Enter the day(1-31): "))
                for patient in patients :
                    for doctor in doctors: 
                        if patients.index(patient) == patient_index:
                            if doctors.index(doctor) == doctor_index: 
                                import datetime 

                                ##linking the patient with the doctor 
                                patient.link(doctor.full_name())
                                doctor.add_patient(patient, datetime.date(year, month, day))


                                break

                print('The patient is now assign to the doctor.')

                

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, patients, discharge_patients):
            """
            Allow the admin to discharge a patient when treatment is done
            Args:
                patients (list<Patients>): the list of all the active patients
                discharge_patients (list<Patients>): the list of all the non-active patients
            """
            discharge = True
            while discharge : 
                self.view_patient(patients)
                print("-----Discharge Patient-----")
                patient_index = int(input('Please enter the patient ID :   '))-1
                choice = input("Do you want to discharge a patient (y/n) :   ").lower()
                if choice == "y": 
                    
                        for patient in patients: 
                            if patients.index(patient) == int(patient_index):
                                discharge_patients.append(patient)
                                patients.remove(patient)
                                self.view_patient(patients)
                                print("Patient has been discharged")
                                break
                else :
                    discharge = False 

    def view_discharge(self, discharged_patients):
            """
            Prints the list of all discharged patients
            Args:
                discharge_patients (list<Patients>): the list of all the non-active patients
            """

            print("-----Discharged Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            for patient in discharged_patients:
                print("{:<2} | {:<28} | {:<27} | {:<4} | {:<12} | {:<7}".format(discharged_patients.index(patient)+1, patient.get_full_name(), patient.get_doctor(), patient.age, patient.mobile, patient.address))



    def view_doctor_numbers(self, doctors):
        numbers = 0
        for doctor in doctors:
            numbers += 1
        
        return numbers
        
    def update_details(self):
            """
            Allows the user to update and change username, password and address
            """

            print('Choose the field to be updated:')
            print(' 1 Username')
            print(' 2 Password')
            print(' 3 Address')
            op = int(input('Input: '))

            if op == 1: 
                username = input("Enter the new username : ")
                self.username = username

            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                password_confirm = input('Enter the new password again: ')
                if password == password_confirm : 
                    self.__password = password
                else : 
                    print("passwords dont match")

            elif op == 3:
                new_address = input("Enter the new address : ")
                self.address = new_address

            else:
                print("Invalid choice.")
        



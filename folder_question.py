# make a class ame folder operations and perform operations
# first take folder path as input if path found enter in system otherwise access denied
# if folder path is accurate then perform operations
#  IMPORTING OS
import os


# MAKING A CLASS
class Folder_operations:
    def __init__(self):
        self.folder_path=""           # MAKE ATTRIBUT FOLDER PATH
 
    
    # THIS MEHTOD IS FOR TAKING FOLDER PATH INPUT
    def get_folder_path(self):
        print("Welcome, Please Enter Folder Path To Perform Operations.")
        print()
        while True:
            # now changing our attribute to users input
            self.folder_path=input("Enter Folder Path (enter 0 to go back):").strip()
            if self.folder_path=="0":   # if he want to go back
                return 
            

            else:
                # checking if folder path is right or not
                if os.path.isdir(self.folder_path):
                    print("Folder Path is correct Now You can access system...")
                    print()
                    # Returning folder path if accurate
                    return self.folder_path

                # Printing error message if not accurate
                else:
                    print()
                    print("Invalid Folder Path.Please Give Correct Folder path.")
                    print()



    # THIS MEHTOD MAKE TO CHECK EXISTENCE OF FILE
    def check_file_existence(self):
        while True:
            try:
                # taking file name input with extension
                file_name=input("Enter File Name with Extension like (abc.txt,xyz.pdf) [enetr 0 to back]:").strip()
                if file_name=="0":   # if want to go back
                    return
                # making file path with concatecation of folder path
                file_name=os.path.join(self.folder_path,file_name)
                # checking existence of file
                if os.path.exists(file_name):
                    print(f"{file_name} is found in that folder.")
                    print()
                    return
                # If file not found 
                else:
                    print("This File Not Found In Folder.")
            except FileNotFoundError:
                print()
                print("The File Not Exist In That Folder.")
                print()
        
    #THIS MEHTOD TO RENAME A FILE
    def rename_file(self):
        while True:
             # fisrt taking file name input that he wat to renme
             file_name=input("Enter File Name with Extension like (abc.txt,xyz.pdf) to rename [enetr 0 to back]:").strip()
             if file_name=="0":
                    return   # if want to go back
             #  making file path with concatecation of folder path
             file_name=os.path.join(self.folder_path,file_name)
             # Check that this file exist or not
             if os.path.exists(file_name):
                 print("Now Enter New name of file you want to rename.")
                 print()
                 # If file found take new file name input
                 new_name=input("Enter File Name with Extension like (abc.txt,xyz.pdf) [enetr 0 to back]:")
                 if new_name=="0":
                     return
                # rename a file in that folder
                 new_name=os.path.join(self.folder_path,new_name)
                 os.rename(file_name,new_name)
                 print(f"New Name Of That File {new_name} Is set Succesffuly.")
                 print()
                 return     
            # If file not found in folder
             else:
                 print()
                 print("Inavlid File name. No File found With that name in folder")
                 print()
            
    # THIS MEHTOD TO MAKE FILE IN FOLDER
    def make_file(self):
        while True:
        # take  filename input
         name_file=input("Enter File Name with Extension like (abc.txt,xyz.pdf) [enetr 0 to back]:").strip()
         if name_file=="0":
            return
        # checking that input must contain something
         if len(name_file)>=1:
             # making file path with concatecation of folder path
            new=os.path.join(self.folder_path,name_file)
            # make  a file
            with open(new,"w") as file:
                pass
            print(f"{name_file} is succesfully made in that folder.")
            print()
            return
        # if input contains nothing
         else:
             print()
             print("Please Enter Something To make File:")
             print()
    
# THIS MWHTOD TO DELETE ANY FILE IN FOLDER
    def delete_file(self):
        while True:
            # take filename input
            name_file=input("Enter File Name with Extension like (abc.txt,xyz.pdf) to delete [enetr 0 to back]:").strip()
            if name_file=="0":
                return
             # making file path with concatecation of folder path
            new=os.path.join(self.folder_path,name_file)
            # Checking existence of file
            if os.path.exists(new):
                # deleting the file if found
                os.remove(new)
                print(f"File {new} has deleted succesfuly.")
                print()
                return
            # If file not found.
            else:
                print(f"Invalid File Name {name_file} No File Found With That Name.")

    # TO PROVIDE CHOICES OF SYSTEM PROVIDE WHEN FOLDER PATH FOUND   
    def give_choice(self):
        print()
        print("\t\tWelcome To This Area.")
        print("\t1.To Check if specific file exist in folder or not.")
        print("\t2.To Rename the file.")
        print("\t3.To Make The file in the folder.")
        print("\t4.To Delete The file From the folder.")
        print("\t5.To Exit:exit from Here.")
        print()

    # Make  a main execution 
    def main_execution(self):
               # First taking folder path input so call this mehtod
               # check if return something then execute
                value=self.get_folder_path()
                if value:               
                    # calling respective mehtod on choices
                    while True:
                        self.give_choice()
                        choice=input("Enter Your Prefereed Option:").strip()
                        if choice=="1":
                            self.check_file_existence()
                        elif choice=="2":
                            self.rename_file()
                        elif choice=="3":
                            self.make_file()
                        elif choice=="4":
                            self.delete_file()
                        elif choice=="5":
                            break           # If he want to end
                        else:                    
                            print("Invalid Choice.")
                else:
                    print("Okay Good Bye!")
# making instance of class
object=Folder_operations()
object.main_execution()
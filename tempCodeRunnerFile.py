import os
import pandas as pd


def dataframe(x): 
    complete_file = os.listdir(x)
    
    for file in complete_file:
        complete_file_path = os.path.join(x, file)
        complete_file_excel = pd.read_csv(complete_file_path)
    df = pd.DataFrame(complete_file_excel)
    return df
    

def compare(x, y,z):
    isnew = 'NO'
    short_updated_file = os.path.join(z,"Atty_Email_Date.csv")
    ID = []
    TkprIndex = []   
    Initials = []   
    FullName =[]
    FirstName = []
    LastName = []
    User = []
    Email = []
    Password = []
    Client = []
    Status = []

### ID	Tkpr Index	Initials	FullName	First Name	Last Name	User	Email	Password	Client	Status

    for index1, Big in x.iterrows():
        for index1, short in y.iterrows():
            if Big['ID'] == short['ID'] and Big['tkprStatus'] != short['Status']:
                ## Creating Variables to append value
                VID = short['ID']
                VTkprIndex = short['Tkpr Index']
                VInitials = short['Initials']  
                VFullName =short['FullName']
                VFirstName = short['FirstName']
                VLastName = short['Last Name']
                VUser = short['User']
                VEmail = short['Email']
                VPassword = short['Password']
                VClient = short['Client']
                VStatus = Big['Status'] 
                ###############################################
                ID.append(VID)
                TkprIndex.append(VTkprIndex)  
                Initials.append(VInitials)  
                FullName.append(VFullName)
                FirstName.append(VFirstName)
                LastName.append(VLastName)
                User.append(VUser)
                Email.append(VEmail)
                Password.append(VPassword) 
                Client.append(VClient)
                Status.append(VStatus)               
                isnew = 'NO'
                break
            
            elif Big['ID'] == short['ID'] and Big['tkprStatus'] == short['Status']:
                VID = short['ID']
                VTkprIndex = short['Tkpr Index']
                VInitials = short['Initials']  
                VFullName =short['FullName']
                VFirstName = short['First Name']
                VLastName = short['Last Name']
                VUser = short['User']
                VEmail = short['Email']
                VPassword = short['Password']
                VClient = short['Client']
                VStatus = short['Status'] 
                ###############################################
                ID.append(VID)
                TkprIndex.append(VTkprIndex)  
                Initials.append(VInitials)  
                FullName.append(VFullName)
                FirstName.append(VFirstName)
                LastName.append(VLastName)
                User.append(VUser)
                Email.append(VEmail)
                Password.append(VPassword) 
                Client.append(VClient)
                Status.append(VStatus)               
                isnew = 'NO'
                break
            else:
                isnew = 'YES'
                continue
        if isnew == 'YES':
            #################
            VID = Big['ID']
            VTkprIndex = Big['TkprIndex']
            VInitials = Big['BillInitial']  
            VFullName =''
            VFirstName = ''
            VLastName = ''
            VUser = ''
            VEmail = ''
            VPassword = 'manning12'
            VClient = 'MK'
            VStatus = Big['tkprStatus'] 
            #################
            ID.append(VID)
            TkprIndex.append(VTkprIndex)
            Initials.append(VInitials)
            FullName.append(VFullName)
            Status.append(VStatus)
            Password.append(VPassword)
            Client.append(VClient)
            FirstName.append(VFullName)
            LastName.append(VLastName)
            User.append(VUser)
            Email.append(VEmail)
    shortdf = pd.DataFrame({'ID':ID, 'Tkpr Index':TkprIndex, 'Initials': Initials, 'FullName': FullName, 'FirstName':FirstName, 'LastName': LastName, 'User':User, 'Email':Email, 'Password': Password, 'Client': Client,'Status': Status })
    shortdf.to_csv(short_updated_file)

def main():
    
    current_path = os.path.dirname(os.path.abspath(__file__))
    complete_atty_fBiger = os.path.join(current_path,"Complete_list")
    knack_list_fBiger = os.path.join(current_path,"Knack_List")
    Updatd_FBiger = os.path.join(current_path, "Updated_List")
    



    compare(dataframe(complete_atty_fBiger), dataframe(knack_list_fBiger),Updatd_FBiger)
    
    


if __name__ == "__main__":
    main()


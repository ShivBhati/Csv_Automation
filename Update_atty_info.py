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
    new_updated_file = os.path.join(z,"Atty_Email_Date.csv")
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


    for index1, old in x.iterrows():
        for index1, new in y.iterrows():
            if old['ID'] == new['ID']:
                if old['tkprStatus'] != new['Status']:
                    ## Creating Variables to append value
                    VID = new['ID']
                    VTkprIndex = new['TkprIndex']
                    VInitials = new['Initials']  
                    VFullName =new['FullName']
                    VFirstName = new['FirstName']
                    VLastName = new['LastName']
                    VUser = new['User']
                    VEmail = new['Email']
                    VPassword = new['Password']
                    VClient = new['Client']
                    VStatus = old['Status'] 
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
                    continue
            else:
                isnew = 'YES'
                continue
        if isnew == 'YES':
            #################
            VID = old['ID']
            VTkprIndex = old['TkprIndex']
            VInitials = old['BillInitial']  
            VFullName =''
            VFirstName = ''
            VLastName = ''
            VUser = ''
            VEmail = ''
            VPassword = 'manning12'
            VClient = 'MK'
            VStatus = old['tkprStatus'] 
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
    newdf = pd.DataFrame({'ID':ID, 'Tkpr Index':TkprIndex, 'Initials': Initials, 'FullName': FullName, 'FirstName':FirstName, 'LastName': LastName, 'User':User, 'Email':Email, 'Password': Password, 'Client': Client,'Status': Status })
    newdf.to_csv(new_updated_file)

def main():
    
    current_path = os.path.dirname(os.path.abspath(__file__))
    complete_atty_folder = os.path.join(current_path,"Complete_list")
    knack_list_folder = os.path.join(current_path,"Knack_List")
    Updatd_Folder = os.path.join(current_path, "Updated_List")
    



    compare(dataframe(complete_atty_folder), dataframe(knack_list_folder),Updatd_Folder)
    
    


if __name__ == "__main__":
    main()


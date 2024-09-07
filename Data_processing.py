import numpy as np
usr_file = "ml-1m/users.dat"

def get_usr_info(path):
    # change the gender to number type
    def gender2num(gender):
        return 1 if gender == 'F' else 0
    
    # open and read file
    with open(usr_file,"r") as f:
        data = f.readlines()


    # Converts user data of string type to numeric type 
    usr_info = {}

    max_usr_id = 0

    for item in data:
        # Remove irrelevant parts of each line
        item = item.strip().split("::")
        usr_id = item[0]
        # Convert string data to numbers and store in a dictionary
        usr_info[usr_id] = {'usr_id': int(usr_id),
                            'gender': gender2num(item[1]),
                            'age': int(item[2]),
                            'job': int(item[3])}
        max_usr_id = max(max_usr_id, int(usr_id))

    return usr_info,max_usr_id

usr_info, max_usr_id = get_usr_info(usr_file)
print("the number of users:", len(usr_info))
print("the max ID:", max_usr_id)
print("the information of the first user：", usr_info['1'])

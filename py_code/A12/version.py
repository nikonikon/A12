import mongodb_module
from global_defination import *
def create_version(version_number,comment):
    mongodb_module.create_version(version_number,comment)

def get_all_version():
    dataset = mongodb_module.inspect_data_in_db('VersionTable')
    for data in dataset:
        if DEBUG:
            print(data)



if __name__ == '__main__':
    create_version('V1.0','Initial version') #Create version V1.0,Comment "Initial version"
    get_all_version() #Return a dataset , use 'for structure' to go over it. Turn on DEBUG in global_defination.py to enable print function

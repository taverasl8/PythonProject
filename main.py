"""
Project :
File sorter

Reasoning: This would be useful for

Synopsis:
    This program allows for the sorting and organizing of files in a particular directory
    This program will take a user input of a directory and based on that
    it will organize the files in the inputed directory based on a cofiguration file.
    In the configuration file it specifies folder names and what file extensions bellongs in them.
        in any case that the configuration file cannot be accessed or anything of that nature a default configuration will be
        implemented in the source code itself

    sample config.json
    {
    "folders":
    {
        "folder_name":["file_extension"],
    }
    }


    actual configuration:
    {
    "folders":
    {
        "Audio":[".mp3",".wav"],
    }
    }   
    in the actual configuration the folders that would be created would be named "Audio" and it will contain
    files that end with ".mp3" or ".wav"


    based on the configuration file folders are either created if they are not there.
    After which the progaram will access each file and read their file extension and the program will move each file based on extenstion
    to specified folders.
    

Based on the configuration file create forlder for specific file extensiions

STEPS

-input(str): File Directory
    Check if the file directory actualy exist
    Fail: end and say no such directory

-Check for files in the directory:
    if empty then END


-loadConfiguration:
    based on a specified directory there is a configuration as a json file
    using python the config.json will be translated as a dictionary.
    This configuration will, specify the folder name and which files goes in

    sample configuration:
    {


    "folders":
    {
        "Audio":[".mp3",".wav"],
        "Video":[".mp4"],
        "Images":[".png",".jpg",".jpeg"]
    }

    }   

    
-Folders: check to see if the folders are already there.
    if not: create
    else: no changes


-Moving files:
    based on the configuration




"""


"""
What else we need
-Creating the folders if needed(has to be done first)
-Listing all the files
-moving the files to the correct folder
"""

import os, argparse, platform, json

# By default the config file is in the same folder as the script
DEFAULT_CONFIG_LOCATION = f"./sorter_config.json"


def json_to_dict(json_path):
    '''
    Function turns a json into a dictionary
    
    Parameters:
    json_path(str)


    '''
    

    with open(f"{json_path}","r") as conFile:
        config = json.load(conFile)

    return config


def get_config(path_config = None):
    """
    Function that reads the configuration and organizes the files based on configuration
    if configuration can not be located then a default config will be chosen.
    """

    # Initially try to load the configuration

    try:
        # if a path_config is provided then, use configuration
        # if anything is off or error comes up a default configuration is used
        if path_config is not None:
            print(f'configuration provided')
        
        config = json_to_dict(path_config)

        return config
    

    except:

        """DEFAULT CONFIGURATION"""
        print(f"no configuration given using default configuration")
    
        default_config = {
        # Insert here commonly used file formats
        "Audio":[".mp3",".wav"],
        "Video":[".mp4"],
        "Images":[".png",".jpg",".jpeg"],
        "Oher":["*"] #NOTE: This might change
        }

        
        return default_config


    return 



def folder_creation(configuration):
    
    """
    Based on the configuration create the folders needed

    Parameters:
    configuration(dict): dictionary with 
    """

    return


def get_files(folder_path):
    """
    This Function takes in a directory and returns the files in the directory if any

    """


    return



def main():
    
    """STEP 1 User Input"""
    # This is for command line agruements
    args = argparse.ArgumentParser(description=f"Program takes a directory path and organizes the files into folders")
    args.add_argument("fileDir", type=str, help="directory path")
    # args.add_argument("itter", type=int, help="number of times repeated")

    cli_arg = args.parse_args()
    folderDir = cli_arg.fileDir
    
    #---Corrects the path based on OS---
    os_name = platform.system()

    if os_name == "Windows":
        folderDir = folderDir.replace("/", "\\")  
    elif os_name in ("Linux", "Darwin"):  
        folderDir = folderDir.replace("\\", "/")  


    #---Test to see if the directory is real---
    if os.path.exists(folderDir):
        print("Directory Exist")
    else:
        # Case here where the file directory is not real or can not be found exit the program
        print("Directory is not real")
        return
    

    """STEP 2 Load Configuration"""
    #  DEFAULT_CONFIG_LOCATION 
    config = get_config(DEFAULT_CONFIG_LOCATION)
    print(config)


    """STEP 3 Foler Creation"""
    # based on the config{} check to see if folders are created if they are not create them
    
    import os
    def folder_creation(configuration, folder_path):
        """
        Create folders based on the configuration if they do not already exist.
        
        Parameters:
        configuration(dict): Configuration specifying folder names and file extensions.
        folder_path(str): Path of the directory where folders will be created.
        """
        for folder_name in configuration.keys():
            folder_directory = os.path.join(folder_path, folder_name)
            # Check if folder exsist, if not create it
            if not os.path.exists(folder_directory):
                os.makedirs(folder_directionary)
                print(f"Create folder: {folder_name} at {folder_directory}")
            else:
                print(f"Folder {folder_name} already exists at {folder_directory}")

    folder_creation(config['folders'], folderDir)

    
    """STEP 4 List out all the files"""
    


    """STEP 5 Moving Files to Correct Folder"""



    """STEP 6 Encryption"""
    # we shall see what happens here


    return



# os.mkdir("/test/w3school") 

main()

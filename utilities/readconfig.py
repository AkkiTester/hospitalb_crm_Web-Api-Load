import configparser
import os

# directory components
directory = 'Configurations'
filename = 'config.ini'

# Get the current working directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a platform-independent file path relative to the current working directory
file_path = os.path.join(current_directory, directory,filename)


config = configparser.RawConfigParser()
config.read(rf'{file_path}')

"""
Getting Common Information from config.ini
"""
class Readconfig:
    @staticmethod
    def geturl():
        url = config.get('common_info', 'Login-page')
        return url

    @staticmethod
    def getid():
        username = config.get('common_info', 'ID')
        return username

    @staticmethod
    def getfpassword():
        password = config.get('common_info', 'Password')
        return password

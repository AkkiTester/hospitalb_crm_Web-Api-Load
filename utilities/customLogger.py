import logging
import os
import inspect

# directory components
directory = 'Log'
filename = 'automation.log'

# Get the current working directory
current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a platform-independent file path relative to the current working directory
file_path = os.path.join(current_directory, directory, filename)

print(file_path)


# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=rf'{file_path}',
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger





class LogGen:
    @staticmethod
    def loggen():
        log_name = inspect.stack()[1][3]  # runtime -getting filepath -class -method
        logger = logging.getLogger(log_name)  # gen logs
        logfile = logging.FileHandler(file_path)  # log file
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")  # log format
        logfile.setFormatter(log_format)  # setting format to the logs
        logger.addHandler(logfile)  # adding log everytime to same file
        logger.setLevel(logging.INFO)  # set log level
        return logger

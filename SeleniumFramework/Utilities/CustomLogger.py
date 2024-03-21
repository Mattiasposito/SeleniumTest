import logging
import inspect



def customLogger():
    #1 this is used to get the class / method name from where this customlogger method is called
    logName = inspect.stack()[1][3]

    #2 create a log object and pass the logname in it
    logger = logging.getLogger(logName)

    #3 Set the log level
    logger.setLevel(logging.DEBUG)

    #4 Create the file handler to save the logs in the file
    filehandler = logging.FileHandler("../Reports/FileLog.log", mode='a')

    #5 set the loglevel for fileHandler
    filehandler.setLevel(logging.DEBUG)

    #6 Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')

    #7 set the Formatter to FileHandler
    filehandler.setFormatter(formatter)

    #8 Add file Handler to logging
    logger.addHandler(filehandler)

    #9 Finally return the logging object

    return logger

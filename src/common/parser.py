import sys
import logging

class Parser:
    """ This class works as a common purpose parser and includes helper methods 
    for other classes that need parsing """
    
    def __init__(self, debug):
        logging.getLogger().setLevel(logging.DEBUG)
        
    def parseBetween(self, data, start, stop):
        """ receives data-string which will be searched,
        start and stop strings to search for. Everything between 
        these tags will be returned as a result string."""
        
        logging.debug("parsing between: %s : %s", start, stop)
        lowdata = data.lower()
        datalength = len(data)
        startreading = lowdata.find(start.lower()) + len(start)
        finishreading = lowdata.find(stop.lower(), startreading, datalength)
        result = ""

        logging.debug("datalength: %s", datalength)
        logging.debug("startreading: %s", startreading)
        logging.debug("finishreading: %s", finishreading)  
        
        if startreading != (len(start)-1):
            logging.debug("sisalla")
            if finishreading > 0:
                result = data[startreading:finishreading]
        
        logging.debug("parsed result: %s", result)
        
            
        return result
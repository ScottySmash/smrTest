import serial
import time
import string


testMAC = "E9C938A0C8E6"


def scanAll():
    
    """ Use A Context Manager To Open A Serial Connection And Send The
        Command To <SCAN ALL> Available Devices:
            Parameters: None
            Return Value: List of Test Results
    """

    # TODO: Move text string used incalls to a struct
    cmdScanAll = b'SCAN ALL'

    # TODO: Make serial settings variable 
    with serial.Serial(port="COM18", baudrate=115200, timeout=3) as ser:
        ser.write(cmdScanAll)
        time.sleep(15)
        outp = ser.read(1000000).decode("utf-8").split("\r\n")

    #print(f'cutting[0] {outp[0]}') #SCAN ALLOK
    #print(f'cutting[-1] {outp[-1]}') #
    #print(f'cutting[-2] {outp[-2]}') #STATUS: READY

    """
    if len(outp) > 3:
        return outp[1:-2]
    else:
        return None
    """

    # Guard Clause
    if len(outp) < 4 : return None

    # Remove Status Lines and Return List
    return outp[1:-2]
    

def getLairdDongleData(cmdString):

    outp = None
    
    # TODO: Make serial settings variable 
    with serial.Serial(port="COM18", baudrate=115200, timeout=3) as ser:
        ser.write(cmdString)
        time.sleep(15)
        outp = ser.read(1000000).decode("utf-8").split("\r\n")

    # Guard Clause - Three blank lines are stripped off, len must be > 3
    if len(outp) < 4 : return None

    # Remove status lines and return list
    return outp[1:-2]


def capture_laird_dongle_raw_data(cmdString):
    
    """ Open serial port and send command string to dongle
    """
    if isinstance(cmdString, str):
        cmdString = cmdString.encode("utf-8")
    
    # TODO: Make serial settings variable 
    with serial.Serial(port="COM18", baudrate=115200, timeout=3) as ser:
        # print(cmdString)
        ser.write(cmdString)
        time.sleep(15)
        outp = ser.read(1000000).decode("utf-8").split("\r\n")
        # outp = ser.read(1000000)
 
    return outp[1:-2]

cap = capture_laird_dongle_raw_data


def scan(cmdType, *args, **kwargs):
    """ General Scan Method
    """
    
    cmdTypes = {
        "ALL" : b'SCAN ALL',
        "TYPE" : b'SCAN TYPE=',
        "MAC" : b'SCAN MAC=',
        "STOP" : b'SCAN STOP',
    }

    cmdStr = cmdTypes[cmdType.upper()]
    resultList = getLairdDongleData(cmdStr)

    return resultList


def run_test(serials, cslist):
    for serial in serials:
        for cs in cslist:
            if serial in cs:
                print(serial, " -> ", cs)


def get_data(test):
    with open("c:\cs\cs102"+test+".txt", "r") as f:
        d = f.read().split("\n")
        return d


def get_102s():
    list = getLairdDongleData(b"SCAN TYPE=CS102")
    return list



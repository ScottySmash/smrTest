from datetime import timezone
import datetime

from pymongo import MongoClient as DB

import laird_dongle as COM

 
def get_utc_time():
    now = datetime.datetime.now
    return now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')


def cs101_test():
    results = COM.cap("SCAN TYPE=CS101")

    #get a time snapshot
    test_time = get_utc_time()
    
    print(f"Test finished capturing {len(results)} results at UTC {test_time}.")

    # TODO: could this be a decorator instead?
    return map(test_dict, results)
    
       


def test_dict(tr):
    
    # TODO: this with re.split()
    
    # Guard Clause
    if "CS101:" not in tr: return None

    test_results = {}
    test_list = tr.strip("CS101:").replace("=", ":").split(",")

    

    return test_results

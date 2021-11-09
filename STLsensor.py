class Sensor:
    
    """ Sensor(MAC str, Model str):
            CS101 - Temperature and Humidity Sensor
            CS102 - Door Sensor
            CS103 - Ranging Sensor
    """
    
    TESTLIST = {
        "CS101" : ["temp", "humi"],
        "CS102" : ["door"],
        "CS103" : ["warp", "dist"]
    }

 
    def __init__(self, MAC: str, model: str):

        self._id = MAC
        self.type = model
        self.status = "untested",
        self.test_results = []

        self.tests = ["rssi", "vbat", "payload"]
        self.tests.extend(Sensor.TESTLIST[self.type])


    def print_sensor_data(self) -> None:
        print(f"MAC: {self._id}, Test Result: {self.status}")
        print(f"Test list -> {self.tests}")
        for test in self.test_results:
            print(test)


    def print_testlist(self) -> None:
        print(self.tests)


    def get_data_dictionary(self) -> {}:
        pass

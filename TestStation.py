class TestStation:
    """
    """

    def __init__(self, cs_model: str):
        self.TestStationType = cs_model.upper()
        
        stationSetup(self.TestStationType)


    def stationSetup():
        pass

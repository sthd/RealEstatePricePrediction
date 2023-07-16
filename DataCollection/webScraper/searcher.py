

class Searcher:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.wait = None
        self.refresh = 0
        self.search_function = None
        self.searcher = None

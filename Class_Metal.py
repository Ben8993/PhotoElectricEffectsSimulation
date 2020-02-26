class Metal():
    def __init__(self, metal):
        self.workfunction_dictionary = {'sodium': 2.28, 'copper': 4.7, 'calcium': 2.9, 'zinc': 4.3, 'platinum': 6.35}
        self.workfunction = self.workfunction_dictionary[metal.lower()] * 1.6e-19
        # use dictionary to find workfunction for metal

    def get_workfunction(self):
        return self.workfunction
class Light():
    def __init__(self, wavelength):
        self.wavelength = wavelength * 1.0e-9
        self.light_energy = 0  # calculate
        self.planck_constant = 6.63e-34
        self.light_speed_constant = 3.0e8

    def calculate_energy(self):
        self.light_energy = (self.planck_constant * self.light_speed_constant) / self.wavelength
        return self.light_energy
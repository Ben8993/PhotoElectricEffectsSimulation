from tkinter import *
from tkinter import messagebox
import Class_Electron as e
import Class_Light as l
import Class_Metal as m


class Photoelectric_Effect_Simulation(Tk):
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='white smoke')
        self.master.title('Photoelectric effect simulation')
        self.master.option_add('*Font', 'Georgia 12')
        self.master.option_add('*Label.Font', 'helvetica 20 bold')
        self.master.option_add('*Background', 'white smoke')
        self.master.geometry('800x500+100+100')
        self.electron_list = []

        main_frame = Frame(self.master)
        main_frame.grid()
        ''''' FRAMES'''
        animation_frame = Frame(main_frame, bg="green")
        animation_frame.grid(row=1, column=0, rowspan=4, columnspan=6, sticky=W + E + N + S)
        wavelength_input_frame = Frame(main_frame)
        wavelength_input_frame.grid(row=1, column=7, rowspan=2, columnspan=3, sticky=W + E + N + S)
        metal_input_frame = Frame(main_frame)
        metal_input_frame.grid(row=3, column=7, rowspan=2, columnspan=3, sticky=W + E + N + S)
        ''''' LABEL START '''
        # Label - Title
        lbl_title = Label(main_frame)
        lbl_title.config(text='Photoelectric Effect Simulation')
        # Label - Metal
        lbl_metal = Label(metal_input_frame)
        lbl_metal.config(text='Metal')
        ''''' LABEL END '''
        ''''' INPUTS START '''
        # Slider - Wavelength
        self.wavelength_input = Scale(wavelength_input_frame, from_=100, to=850, orient=HORIZONTAL,
                                      label='Wavelength (nm)',
                                      length=195)
        self.wavelength_input.grid(row=2, column=0, sticky='w')
        # Dropdown Menu - Metal
        self.metal_input = StringVar(metal_input_frame)
        self.metal_input.set('Sodium')  # Default Value
        dropdown = OptionMenu(metal_input_frame, self.metal_input, 'Sodium', 'Copper', 'Calcium', 'Zinc', 'Platinum')
        dropdown.grid(row=2, column=0, sticky='w')
        ''''' INPUTS END '''
        ''''' CANVAS '''
        self.canvas = Canvas(animation_frame, width=600, height=400)
        self.canvas.grid(row=2, column=0)
        self.canvas.create_rectangle(0, 0, 10, 350, fill="grey")
        ''''' CANVAS '''
        ''''' BUTTON START '''
        # Button - Play
        btn_play = Button(main_frame)
        btn_play.config(text='PLAY', command=self.play)
        ''''' BUTTON END '''
        ''''' GRID START '''
        lbl_title.grid(row=0, column=0, sticky='w')
        btn_play.grid(row=0, column=1, sticky='w')
        lbl_metal.grid(row=0, column=0, sticky='w')
        ''''' GRID END '''

    def play(self):
        for ball in self.electron_list:
            ball.destroy_ball()
        self.electron_list = []
        user_metal = m.Metal(self.metal_input.get())
        user_wavelength = l.Light(self.wavelength_input.get())
        light_energy = user_wavelength.calculate_energy()
        workfunction = user_metal.get_workfunction()
        if user_wavelength.calculate_energy() > user_metal.get_workfunction():
            for i in range(0, 10):
                elec = e.Electron(self.canvas, light_energy, workfunction)
                self.electron_list.append(elec)
            for each in self.electron_list:
                each.calculate_velocity()
                each.move_ball()
        else:
            messagebox.showerror("Threshold Frequency not met",
                                 "The light wavelength you have chosen doesnt meet the threshold frequency of the metal, so no electrons can be emitted.")


def main():
    root = Tk()
    pes_app = Photoelectric_Effect_Simulation(root)
    root.mainloop()


if __name__ == '__main__':
    main()

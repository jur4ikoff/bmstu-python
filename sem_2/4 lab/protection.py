from processing_protection import validate, make_array_unique, find_max
from tkinter import *
import warnings

warnings.filterwarnings('ignore')

WIDTH, HEIGHT = 680, 780


class Application:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.points = []
        self.circles = []
        self.window_width, self.window_height = window_width, window_height
        self.init_UI()
        self.open_window_in_center()
        self.add_canvas()
        self.settings_interface()

    def init_UI(self):
        self.window.title("Поиск ближайших кругов")
        self.window.geometry(f'{self.window_width}x{self.window_height}')

    def open_window_in_center(self):
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
        self.window.wm_geometry("+%d+%d" % (x - (self.window_width // 2), y - (self.window_height // 2)))

    def add_canvas(self):
        self.c = Canvas(width=(self.window_width - 80), height=(self.window_height - 180), bg='white')
        self.c.pack()

    def settings_interface(self):
        self.frame = Frame(self.window, padx=20, pady=20)
        self.frame.pack(expand=True)

        self.point_header = Label(self.frame, text="Добавление точки")
        self.point_header.grid(row=3, column=1)

        self.point_annotation = Label(self.frame, text="(x1 y1)")
        self.point_annotation.grid(row=4, column=0)

        self.circle_header = Label(self.frame, text="Добавление круга", )
        self.circle_header.grid(row=3, column=4)

        self.circle_annotation = Label(self.frame, text="(x1 y1 r)")

        self.circle_annotation.grid(row=4, column=3)

        self.point_input = Entry(self.frame)
        self.point_input.grid(row=4, column=1)

        self.circle_input = Entry(self.frame)
        self.circle_input.grid(row=4, column=4)

        self.btn1 = Button(self.frame, text='Добавить точку', command=self.add_point)
        self.btn1.grid(row=5, column=1)

        self.btn2 = Button(self.frame, text='Добавить круг', command=self.add_circle)
        self.btn2.grid(row=5, column=4)

        self.result = Button(self.frame, text='Найти прямую', command=self.calculate)
        self.result.grid(row=6, column=2)

    def add_point(self):
        point = self.point_input.get()
        point, res = validate(point, self.window_width, self.window_height, mode=0)
        if point != -1:
            self.points.append(point)
            self.create_point(point)

    def add_circle(self):
        circle = self.circle_input.get()
        circle, res = validate(circle, self.window_width, self.window_height, mode=1)
        if circle != -1:
            self.circles.append(circle)
            self.draw_circle(circle, "blue", width=2)

    def create_point(self, point):
        x1, y1 = (point[0] - 2), (point[1] - 2)
        x2, y2 = (point[0] + 2), (point[1] + 2)
        self.c.create_oval(x1, y1, x2, y2, fill="green")

    def draw_circle(self, center, color, width):
        self.c.create_oval(center[0] - center[2], center[1] - center[2],
                           center[0] + center[2], center[1] + center[2], outline=color, outlinestipple=width)

    def calculate(self):
        self.circles = make_array_unique(self.circles)
        self.points = make_array_unique(self.points)[:1]
        min_circle = find_max(self.circles, self.points)
        self.draw_circle(min_circle, "red", 2)


if __name__ == "__main__":
    window = Tk()
    app = Application(window, WIDTH, HEIGHT)
    window.mainloop()

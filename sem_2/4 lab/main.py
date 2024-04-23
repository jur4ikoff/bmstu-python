from processing import validate, make_array_unique, find_max_line
from tkinter import *
import warnings
import time

warnings.filterwarnings('ignore')

WIDTH, HEIGHT = 680, 780


class Application:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.points = []
        self.lines = []
        self.window_width, self.window_height = window_width, window_height
        self.init_UI()
        self.open_window_in_center()
        self.add_canvas()
        self.settings_interface()
        self.c.bind("<B1-Motion>", self.paint)

    def init_UI(self):
        self.window.title("Поиск параллельных")
        self.window.geometry(f'{self.window_width}x{self.window_height}')

    def open_window_in_center(self):
        x = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2
        y = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
        self.window.wm_geometry("+%d+%d" % (x - (self.window_width // 2), y - (self.window_height // 2)))

    def add_canvas(self):
        self.c = Canvas(width=(self.window_width - 80), height=(self.window_height - 180), bg='white')
        self.c.pack()

    def settings_interface(self):
        self.frame = Frame(
            self.window,
            padx=20,
            pady=20
        )
        self.frame.pack(expand=True)

        self.status_label = Label(self.frame, text="Статус")
        self.status_label.grid(row=2, column=2)

        self.point_header = Label(
            self.frame,
            text="Добавление точки"
        )
        self.point_header.grid(row=3, column=1)

        self.point_annotation = Label(
            self.frame,
            text="(x1 y1)"
        )
        self.point_annotation.grid(row=4, column=0)

        self.line_header = Label(
            self.frame,
            text="Добавление прямой",
        )
        self.line_header.grid(row=3, column=4)

        self.line_annotation = Label(
            self.frame,
            text="(x1 y1 x2 y2)"
        )

        self.line_annotation.grid(row=4, column=3)

        self.point_input = Entry(
            self.frame,
        )
        self.point_input.grid(row=4, column=1)

        self.line_input = Entry(
            self.frame,
        )
        self.line_input.grid(row=4, column=4)

        self.btn1 = Button(self.frame, text='Добавить точку', command=self.add_point)
        self.btn1.grid(row=5, column=1)

        self.btn2 = Button(self.frame, text='Добавить прямую', command=self.add_line)
        self.btn2.grid(row=5, column=4)

        self.result = Button(self.frame, text='Найти прямую', command=self.calculate)
        self.result.grid(row=6, column=2)

    def add_point(self):
        point = self.point_input.get()
        point, res = validate(point, self.window_width, self.window_height, mode=0)
        if res != 0:
            self.change_status(3)
        else:
            self.change_status(2)
        if point != -1:
            self.points.append(point)
            self.create_point(point)

    def add_line(self):
        line = self.line_input.get()
        line, res = validate(line, self.window_width, self.window_height, mode=1)
        if res != 0:
            self.change_status(3)
        else:
            self.change_status(2)
        if line != -1:
            self.lines.append(line)
            self.create_line(line, "blue", widht=2)

    def create_point(self, point):
        x1, y1 = (point[0] - 2), (point[1] - 2)
        x2, y2 = (point[0] + 2), (point[1] + 2)
        self.c.create_oval(x1, y1, x2, y2, fill="green")

    def create_line(self, line, color, widht):
        self.c.create_line(line[0], line[1], line[2], line[3], fill=color, width=widht)

    def calculate(self):
        self.points = make_array_unique(self.points)
        self.lines = make_array_unique(self.lines)
        res, x1, y1, x2, y2 = find_max_line(self.points, self.lines)
        answer = [x1, y1, x2, y2]
        if res:
            self.change_status(0)
        else:
            self.change_status(1)
            return
        print(answer)
        self.create_line(answer, color="red", widht=3)

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.c.create_oval(x1, y1, x2, y2, fill="green")
        self.points.append([event.x, event.y])
        time.sleep(0.004)

    def change_status(self, res):
        match res:
            case 0:
                self.status_label['text'] = 'Успешный поиск'
            case 1:
                self.status_label['text'] = 'Нет такой прямой'
            case 2:
                self.status_label['text'] = 'Успешное добавление'
            case 3:
                self.status_label['text'] = 'Произошла ошибка'


if __name__ == "__main__":
    window = Tk()
    app = Application(window, WIDTH, HEIGHT)
    window.mainloop()

import tkinter as tk


class App:

    def __init__(self, parent):
        """Constructor"""
        frame = tk.Frame(parent)
        frame.pack()

        btn22 = tk.Button(
            frame,
            text="22",
            command=lambda: self.print_num(22)
        )
        btn22.pack(side=tk.LEFT)

        btn44 = tk.Button(
            frame,
            text="44",
            command=lambda: self.print_num(44)
        )
        btn44.pack(side=tk.LEFT)

        quit_btn = tk.Button(frame, text="QUIT", fg="red", command=frame.quit)
        quit_btn.pack(side=tk.LEFT)

    def print_num(self, num):
        print("You're press button: %s" % num)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# import math
#
#
# def sq_root(x):
#     """Find the square root"""
#     return math.sqrt(x)
#
#
# square_rt = lambda x: math.sqrt(x)
# print(sq_root(49))
# print(square_rt(64))

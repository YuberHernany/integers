from manim import *


class MyNumberLine(Scene):
    def construct(self):
        nl = NumberLine(
            x_range=[-6,6],
            length=12,
            stroke_width=10
        ).add_numbers().set_color(RED)
        self.add(nl)
        self.wait(1)

if __name__ == "__main__":
    pass 
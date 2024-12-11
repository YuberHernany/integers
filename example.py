import numpy as np
from manim import *
from sprits import *
config.background_color = YELLOW

def one_step_on(scene: Scene, mob: Mobject, number_line: NumberLine, direction: np.ndarray):
    """number_line: NumberLine, mob: Mobject, direction: str with options 'left', 'right'
       scene: Scene """
    unit_length = number_line.get_unit_size()
    if direction == 'left':
        scene.play(mob.animate.shift(unit_length * LEFT), run_time=0.3)
    elif direction == 'right':
        scene.play(mob.animate.shift(unit_length * RIGHT), run_time=0.3)
        

class Adding(Scene):
    def construct(self):

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{utfsym}")
        integers = [-2, 5, -3, 2, -4]
        question = MathTex(*["-", "2", "+", "5", "-", "3", "+", "2", "-", "4"],
                           color=BLACK,
                           substrings_to_isolate=["-","+"],
                           font_size=120, 
                           stroke_width=5)
        question.set_color_by_tex("+", GRAY)
        question.set_color_by_tex("-", ORANGE)
        question.to_edge(UP)        

        self.play(Write(question))

        numb_line = NumberLine(
            x_range=[-6,6],
            length=12,
            stroke_width=20,
            font_size=64,
            tick_size=0.2
        ).add_numbers().set_color(RED)

        hand_right = Tex(
            r"\usym{261E}",
            tex_template=myTemplate,
            color=GRAY, 
            font_size=80,
            stroke_width=4
        ).next_to(numb_line, UP, buff=0.3).align_to(numb_line, RIGHT)

        plus_sign = MathTex("+", 
                            font_size=120, 
                            color=GRAY,
                            stroke_width=5).next_to(hand_right, UP)
        hand_left = Tex(
            r"\usym{261C}",
            tex_template=myTemplate,
            color=ORANGE,
            font_size=80,
            stroke_width=4
        ).next_to(numb_line, UL, buff=0.3).align_to(numb_line, LEFT)
        minus_sign = MathTex("-", 
                            font_size=120, 
                            color=ORANGE,
                            stroke_width=5).next_to(hand_left, UP)
        hand_down = Tex(
            r"\usym{261F}",
            tex_template=myTemplate,
            color=BLACK, 
            font_size=164,
            stroke_width=4
        ).next_to(numb_line.n2p(-2 + 0.1), UP, buff=0.3)
        hand_up = Tex(
            r"\usym{261D}",
            tex_template=myTemplate,
            color=BLACK, 
            font_size=100,
        ).next_to(numb_line.n2p(-2+0.1), UP, buff=0.3)

        ################################################################
        self.add_sound("assets/sounds/enteros.wav",gain=3)
        # self.wait(0.01)
        self.wait(7)
        self.play(Write(question))
        self.play(Create(numb_line))
        self.play(Create(hand_right), Create(plus_sign))
        self.play(Create(hand_left), Create(minus_sign))
        # self.play(Create(hand_up))
        rec1 = SurroundingRectangle(question[0:2], color=ORANGE)
        rec2 = SurroundingRectangle(question[2:4], color=GRAY)
        rec3 = SurroundingRectangle(question[4:6], color=ORANGE)
        rec4 = SurroundingRectangle(question[6:8], color=GRAY)
        rec5 = SurroundingRectangle(question[8:10], color=ORANGE)
        recs = [rec1,rec2, rec3, rec4, rec5]
        self.play(Create(recs[0]))
        self.play(Create(hand_down))
        self.wait(2)
        for integer, r in zip(integers[1:], recs[1:]):
            for k in range(1, abs(integer)+1):
                if integer > 0:
                    one_step_on(self, hand_down, numb_line, 'right')
                    self.play(FadeIn(r), run_time=0.01)
                    self.add_sound("assets/sounds/count.wav",gain=2)
                    self.play(FadeOut(r), run_time=0.01)
                    self.wait(0.01)
                elif integer < 0:
                    one_step_on(self, hand_down, numb_line, 'left')
                    self.play(FadeIn(r), run_time=0.01)
                    self.add_sound("assets/sounds/finish.wav",gain=2)
                    self.play(FadeOut(r), run_time=0.01)
                    self.wait(0.01)
                self.wait(0.4)
        self.wait(2)

from manim import *

class ExampleCode(Scene):
    def construct(self):
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(FadeIn(rendered_code.background_mobject))
        self.wait(1)
        self.play(FadeIn(rendered_code.line_numbers))
        self.wait(2)
        self.add_sound("assets/sounds/typing.mp3",gain=4)
        self.wait(0.1)
        for line in rendered_code.code[:2]:
            if len(line) != 0:
                self.play(AddTextLetterByLetter(line), time_per_char=0.01)
        self.play(AddTextLetterByLetter(rendered_code.code[2:]))
        self.wait(2)
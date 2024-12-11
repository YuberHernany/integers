from manim import *

config.background_color = YELLOW

head = Circle(fill_opacity=1).set_color(PURPLE)
E1 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2)
E2 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2).next_to(E1, RIGHT, buff=0.2)

noise_arr_right = np.array([[0,1,0], [0,0,0], [2, 1/2, 0]])
noise_arr_left = np.array([[0,1,0], [0,0,0], [-2, 1/2, 0]])
noise_arr_center = np.array([[-1/2,1,0], [1/2,1,0], [0,0,0]])
noise_right = Polygon(*noise_arr_right, fill_opacity=1.0).set_color(BLACK).scale(0.5)
noise_left = Polygon(*noise_arr_left, fill_opacity=1).set_color(BLACK).scale(0.5)
noise_center = Polygon(*noise_arr_center, fill_opacity=1).set_color(BLACK).scale(0.5)


def sprits_watch(direction):
    """direction must be 'left' or 'right', 'center' """
    if direction == 'left':
        E1 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2)
        E2 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2).next_to(E1, RIGHT, buff=0.2)
        e1 = E1.next_to(Dot(np.array([-0.5, 0.6, 0])), ORIGIN).copy()
        e2 = E2.next_to(e1, RIGHT, buff=0.2).copy()
        noise_left.next_to(Dot(np.array([-0.9, 0.0, 0])), ORIGIN)
        return VGroup(*[head, e1, e2, noise_left])
    elif direction == 'right':
        E1 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2)
        E2 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2).next_to(E1, RIGHT, buff=0.2)
        e1 = E1.next_to(Dot(np.array([0.5, 0.6, 0])), ORIGIN).copy()
        e2 = E2.next_to(e1, RIGHT, buff=0.2).copy()
        noise_right.next_to(Dot(np.array([0.9, 0.0, 0])), ORIGIN)
        return VGroup(*[head, e1, e2, noise_right])
    elif direction == 'center':
        E1 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2)
        E2 = Circle(fill_opacity=1).set_color(BLACK).scale(0.2).next_to(E1, RIGHT, buff=0.2)
        e1 = E1.next_to(Dot(np.array([-0.2, 0.6, 0])), ORIGIN).copy()
        e2 = E2.next_to(e1, RIGHT, buff=0.2).copy()
        noise_center.next_to(Dot(np.array([0.0, 0.0, 0])), ORIGIN)
        return VGroup(*[head, e1, e2, noise_center])


class CreatingSprits(Scene):
    def construct(self):
        sprit_left = sprits_watch('left')
        sprit = sprit_left.copy()
        sprit_center = sprits_watch('center')
        sprit_right = sprits_watch('right')
        self.add(sprit)
        self.play(Transform(sprit, sprit_left))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_center))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_right))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_left))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_center))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_right))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_left))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_center))
        self.wait(0.1)
        self.play(Transform(sprit, sprit_right))
        self.wait(0.1)

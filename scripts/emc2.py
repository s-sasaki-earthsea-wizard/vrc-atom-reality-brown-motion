"""
E=mc^2を表示するシンプルなアニメーション
"""

from manim import *


class EMC2(Scene):
    """E=mc^2の式を表示するシーン"""

    def construct(self):
        # E=mc^2の数式を作成
        equation = MathTex("E", "=", "m", "c^2")
        equation.scale(3)

        # アニメーション: 式を書くように表示
        self.play(Write(equation), run_time=2)
        self.wait(2)

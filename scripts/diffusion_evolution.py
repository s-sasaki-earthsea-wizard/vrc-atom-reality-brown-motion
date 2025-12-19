"""
拡散方程式の時間発展アニメーション
初期条件: δ(x) → 時間とともにガウス分布が広がる
「1つの粒子がどこにいる確率」として解釈
"""

from manim import *
import numpy as np


class DiffusionEvolution(Scene):
    """拡散方程式の時間発展: δ(x)からガウス分布へ"""

    def construct(self):
        # 拡散係数
        D = 0.5

        # 座標軸の設定
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 2.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        )

        # 軸ラベル
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label(r"\rho", edge=UP, direction=UP)

        # タイトル
        title = Text("拡散方程式の時間発展", font_size=32)
        title.to_edge(UP)

        # 拡散方程式
        eq_label = Text("拡散方程式:", font_size=20)
        diff_eq = MathTex(r"\frac{\partial \rho}{\partial t} = D \frac{\partial^2 \rho}{\partial x^2}")
        diff_eq.scale(0.7)
        eq_group = VGroup(eq_label, diff_eq).arrange(DOWN, buff=0.1)
        eq_group.to_corner(UR)

        # 解の式
        sol_label = Text("解:", font_size=20)
        solution_eq = MathTex(
            r"\rho(x,t) = \frac{1}{\sqrt{4\pi D t}} e^{-\frac{x^2}{4Dt}}"
        )
        solution_eq.scale(0.6)
        sol_group = VGroup(sol_label, solution_eq).arrange(DOWN, buff=0.1)
        sol_group.next_to(eq_group, DOWN, buff=0.3)

        # 座標軸と式を表示
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Write(eq_group))
        self.play(Write(sol_group))
        self.wait(0.5)

        # ガウス分布の関数（拡散方程式の解）
        def gaussian(x, t):
            if t <= 0.01:
                t = 0.01  # t≈0ではδ関数に近い形
            return (1 / np.sqrt(4 * np.pi * D * t)) * np.exp(-x**2 / (4 * D * t))

        # 初期状態（t≈0、鋭いピーク = δ関数の近似）
        t_initial = 0.02
        initial_graph = axes.plot(
            lambda x: gaussian(x, t_initial),
            x_range=[-5, 5],
            color=YELLOW
        )

        # 時間表示
        time_label = MathTex("t = 0")
        time_label.to_corner(UL)

        # 初期条件の説明
        init_text = Text("初期条件: δ(x)", font_size=24, color=YELLOW)
        init_text.next_to(axes, DOWN)

        self.play(Create(initial_graph), Write(time_label), Write(init_text))
        self.wait(1)

        # 確率解釈の説明
        prob_text = Text("= 粒子が位置xにいる確率密度", font_size=20, color=GREEN)
        prob_text.next_to(init_text, DOWN, buff=0.2)
        self.play(Write(prob_text))
        self.wait(0.5)

        self.play(FadeOut(init_text), FadeOut(prob_text))

        # 時間発展のアニメーション（0〜1を0.01刻み）
        time_values = [i * 0.01 for i in range(1, 101)]  # 0.01, 0.02, ..., 1.0

        current_graph = initial_graph
        for t in time_values:
            new_graph = axes.plot(
                lambda x, t=t: gaussian(x, t),
                x_range=[-5, 5],
                color=YELLOW
            )
            new_time_label = MathTex(f"t = {t:.2f}")
            new_time_label.to_corner(UL)

            self.play(
                Transform(current_graph, new_graph),
                Transform(time_label, new_time_label),
                run_time=0.05
            )

        self.wait(0.5)

        # 最終説明
        final_text = Text(
            "時間とともに分布が広がる → 粒子の存在確率が拡散",
            font_size=24
        )
        final_text.to_edge(DOWN)
        self.play(Write(final_text))

        self.wait(2)

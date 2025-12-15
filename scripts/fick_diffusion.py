"""
フィックの法則のアニメーション
「粒子は濃度の高い方から低い方へ拡散する」を視覚化
J = -D dρ/dx
"""

from manim import *
import numpy as np


class FickDiffusion(Scene):
    """フィックの法則: 濃度勾配と粒子の流れを表示"""

    def construct(self):
        # 座標軸の設定
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.2],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        )

        # 軸ラベル
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label(r"\rho", edge=UP, direction=UP)

        # フィックの法則の式を表示
        fick_label = Text("粒子の流れ", font_size=24)
        fick_math = MathTex(r"J = -D \frac{d\rho}{dx}")
        fick_math.scale(0.8)
        fick_eq = VGroup(fick_label, fick_math).arrange(DOWN, buff=0.2)
        fick_eq.to_corner(UR)

        # 座標軸を表示
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Write(fick_eq))
        self.wait(0.5)

        # 濃度分布（左側が高濃度、右側が低濃度）
        def concentration(x):
            return 0.9 / (1 + np.exp(x))  # シグモイド関数で滑らかな勾配

        # 濃度分布のグラフ
        conc_graph = axes.plot(
            concentration,
            x_range=[-4, 4],
            color=YELLOW
        )
        conc_label = Text("濃度 ρ(x)", font_size=24)
        conc_label.next_to(conc_graph, UP + LEFT)
        conc_label.set_color(YELLOW)

        self.play(Create(conc_graph), Write(conc_label))
        self.wait(0.5)

        # 「高濃度」「低濃度」のラベル
        high_label = Text("高濃度", font_size=28, color=RED)
        low_label = Text("低濃度", font_size=28, color=BLUE)
        high_label.move_to(axes.c2p(-3, 1.0))
        low_label.move_to(axes.c2p(3, 1.0))

        self.play(Write(high_label), Write(low_label))
        self.wait(0.5)

        # 粒子の流れを矢印で表示
        arrows = VGroup()
        arrow_positions = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]

        for x_pos in arrow_positions:
            # 濃度勾配を計算（数値微分）
            dx = 0.1
            gradient = (concentration(x_pos + dx) - concentration(x_pos - dx)) / (2 * dx)

            # 流束 J = -D * dρ/dx（勾配が負なので流れは正の方向）
            flux = -gradient * 2  # スケール調整

            # 矢印の長さと方向
            y_pos = concentration(x_pos)
            arrow = Arrow(
                start=axes.c2p(x_pos - flux * 0.3, y_pos - 0.15),
                end=axes.c2p(x_pos + flux * 0.3, y_pos - 0.15),
                color=GREEN,
                buff=0,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.3
            )
            arrows.add(arrow)

        flow_label = Text("粒子の流れ", font_size=24, color=GREEN)
        flow_label.to_corner(DL)

        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            Write(flow_label),
            run_time=1.5
        )
        self.wait(1)

        # 説明テキスト
        explanation = Text(
            "濃度の高い方から低い方へ粒子が流れる",
            font_size=28
        )
        explanation.to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(2)

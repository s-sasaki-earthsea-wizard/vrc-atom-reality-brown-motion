"""
変位の二乗平均の具体計算アニメーション
アインシュタインの1905年の計算を再現
"""

from manim import *


class MSDCalculation(Scene):
    """変位の二乗平均の具体的な計算を表示"""

    def construct(self):
        # タイトル
        title = Text("変位の二乗平均の計算", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 核心の式
        main_eq = MathTex(r"\langle (\Delta x)^2 \rangle = 2Dt")
        main_eq.scale(1.3)
        main_eq.move_to(UP * 2)

        box = SurroundingRectangle(main_eq, color=YELLOW, buff=0.2)

        self.play(Write(main_eq), Create(box))
        self.wait(1)

        # 式を上に移動
        self.play(
            main_eq.animate.scale(0.7).move_to(UP * 2.5),
            box.animate.scale(0.7).move_to(UP * 2.5),
            title.animate.scale(0.7).to_corner(UL),
        )

        # 計算条件
        conditions_title = Text("アインシュタインの計算条件（1905年）", font_size=24)
        conditions_title.move_to(UP * 1.5)

        self.play(Write(conditions_title))
        self.wait(0.3)

        # 条件を1つずつ表示
        cond1_label = Text("粒子の直径:", font_size=20)
        cond1_value = MathTex(r"2r = 1 \, \mu m")
        cond1 = VGroup(cond1_label, cond1_value).arrange(RIGHT, buff=0.2)
        cond1.move_to(UP * 0.8 + LEFT * 2)

        cond2_label = Text("温度:", font_size=20)
        cond2_value = MathTex(r"T = 17°C = 290 \, K")
        cond2 = VGroup(cond2_label, cond2_value).arrange(RIGHT, buff=0.2)
        cond2.move_to(UP * 0.3 + LEFT * 2)

        cond3_label = Text("水の粘性係数:", font_size=20)
        cond3_value = MathTex(r"\eta = 1.35 \times 10^{-2} \, \text{g/(cm} \cdot \text{s)}")
        cond3_value.scale(0.8)
        cond3 = VGroup(cond3_label, cond3_value).arrange(RIGHT, buff=0.2)
        cond3.move_to(DOWN * 0.2 + LEFT * 1.5)

        self.play(Write(cond1))
        self.wait(0.3)
        self.play(Write(cond2))
        self.wait(0.3)
        self.play(Write(cond3))
        self.wait(0.5)

        # アインシュタイン-ストークスの式
        es_label = Text("アインシュタイン-ストークスの式:", font_size=20)
        es_label.move_to(DOWN * 0.9 + LEFT * 2)

        es_eq = MathTex(r"D = \frac{k_B T}{6 \pi \eta r}")
        es_eq.next_to(es_label, RIGHT, buff=0.2)

        self.play(Write(es_label), Write(es_eq))
        self.wait(0.5)

        # Dの計算結果
        d_result = MathTex(r"D \simeq 3.15 \times 10^{-6} \, \text{cm}^2/\text{s}")
        d_result.move_to(DOWN * 1.6)
        d_result.set_color(GREEN)

        self.play(Write(d_result))
        self.wait(1)

        # 画面をクリアして次のステップへ
        self.play(
            FadeOut(conditions_title),
            FadeOut(cond1), FadeOut(cond2), FadeOut(cond3),
            FadeOut(es_label), FadeOut(es_eq),
            d_result.animate.move_to(UP * 1),
        )

        # t = 30秒での計算
        t_label = Text("t = 30 秒のとき", font_size=24)
        t_label.move_to(UP * 0.3)

        self.play(Write(t_label))
        self.wait(0.3)

        # 計算式
        calc_eq = MathTex(
            r"\sqrt{\langle (\Delta x)^2 \rangle}",
            r"=",
            r"\sqrt{2Dt}"
        )
        calc_eq.move_to(DOWN * 0.3)

        self.play(Write(calc_eq))
        self.wait(0.5)

        # 数値代入
        substitution = MathTex(
            r"= \sqrt{2 \times 3.15 \times 10^{-6} \times 30}"
        )
        substitution.scale(0.9)
        substitution.next_to(calc_eq, DOWN, buff=0.3)

        self.play(Write(substitution))
        self.wait(0.5)

        # 結果
        result = MathTex(r"\simeq 4.3 \, \mu m")
        result.scale(1.2)
        result.next_to(substitution, DOWN, buff=0.3)
        result.set_color(YELLOW)

        result_box = SurroundingRectangle(result, color=YELLOW, buff=0.15)

        self.play(Write(result), Create(result_box))
        self.wait(0.5)

        # 結論
        conclusion = Text(
            "→ これは顕微鏡で観測できる大きさ！",
            font_size=28,
            color=GREEN
        )
        conclusion.to_edge(DOWN)

        self.play(Write(conclusion))
        self.wait(2)

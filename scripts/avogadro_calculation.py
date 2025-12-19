"""
アインシュタイン-ストークスの式からボルツマン定数・アボガドロ数を求める
計算過程のアニメーション
"""

from manim import *


class AvogadroCalculation(Scene):
    """アインシュタイン-ストークス式からアボガドロ数を導出"""

    def construct(self):
        # === Part 1: アインシュタイン-ストークスの式 ===
        title = Text("アボガドロ数の決定", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # アインシュタイン-ストークスの式
        subtitle1 = Text("アインシュタイン-ストークスの式", font_size=24, color=YELLOW)
        subtitle1.next_to(title, DOWN, buff=0.4)

        es_eq = MathTex(r"D = \frac{k_B T}{6\pi \eta r}")
        es_eq.scale(1.3)
        es_eq.next_to(subtitle1, DOWN, buff=0.5)

        self.play(Write(subtitle1))
        self.play(Write(es_eq))
        self.wait(1)

        # === Part 2: k_B について解く ===
        step1_text = Text("ボルツマン定数について解くと...", font_size=24)
        step1_text.next_to(es_eq, DOWN, buff=0.6)

        self.play(Write(step1_text))
        self.wait(0.5)

        # 変形過程
        kb_eq = MathTex(r"k_B = \frac{6\pi \eta r D}{T}")
        kb_eq.scale(1.3)
        kb_eq.next_to(step1_text, DOWN, buff=0.4)

        self.play(TransformFromCopy(es_eq, kb_eq))
        self.wait(1)

        # 画面をクリアして次のパートへ
        self.play(
            FadeOut(subtitle1),
            FadeOut(es_eq),
            FadeOut(step1_text),
            kb_eq.animate.move_to(UP * 1.5).scale(0.9),
        )

        # 枠で強調
        kb_box = SurroundingRectangle(kb_eq, color=YELLOW, buff=0.15)
        self.play(Create(kb_box))
        self.wait(0.5)

        # === Part 3: 実験からk_Bが求まる ===
        exp_text = Text("実験データを代入すると、ボルツマン定数が求まる", font_size=24)
        exp_text.next_to(kb_box, DOWN, buff=0.6)

        self.play(Write(exp_text))
        self.wait(1)

        # === Part 4: 気体定数との関係 ===
        self.play(
            FadeOut(exp_text),
            VGroup(kb_eq, kb_box).animate.move_to(UP * 2.2).scale(0.8),
        )

        # 気体定数との関係式
        relation_title = Text("気体定数との関係", font_size=28, color=BLUE)
        relation_title.move_to(UP * 0.8)

        relation_eq = MathTex(r"k_B = \frac{R}{N_A}")
        relation_eq.scale(1.3)
        relation_eq.next_to(relation_title, DOWN, buff=0.4)

        # 各変数の説明
        legend = VGroup(
            VGroup(MathTex("k_B"), Text(" : ボルツマン定数", font_size=18)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex("R"), Text(" : 気体定数（8.314 J/(mol·K)）", font_size=18)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex("N_A"), Text(" : アボガドロ数", font_size=18)).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legend.scale(0.9)
        legend.to_corner(DL, buff=0.5)

        self.play(Write(relation_title))
        self.play(Write(relation_eq))
        self.play(Write(legend))
        self.wait(1)

        # 変形してN_Aについて解く
        transform_text = Text("アボガドロ数について解くと...", font_size=24)
        transform_text.next_to(relation_eq, DOWN, buff=0.5)

        self.play(Write(transform_text))
        self.wait(0.5)

        na_eq = MathTex(r"N_A = \frac{R}{k_B}")
        na_eq.scale(1.3)
        na_eq.next_to(transform_text, DOWN, buff=0.4)

        na_box = SurroundingRectangle(na_eq, color=GREEN, buff=0.15)

        self.play(TransformFromCopy(relation_eq, na_eq))
        self.play(Create(na_box))
        self.wait(1)

        # === Part 5: ペランの実験結果 ===
        self.play(
            FadeOut(relation_title),
            FadeOut(relation_eq),
            FadeOut(transform_text),
            FadeOut(kb_eq),
            FadeOut(kb_box),
            FadeOut(legend),
            VGroup(na_eq, na_box).animate.move_to(UP * 1.5),
        )

        # ペランの測定したボルツマン定数
        perrin_title = Text("ペランの実験結果（1908年）", font_size=28, color=YELLOW)
        perrin_title.next_to(na_box, DOWN, buff=0.6)

        perrin_kb = MathTex(r"k_B \approx 1.28 \times 10^{-23} \text{ J/K}")
        perrin_kb.next_to(perrin_title, DOWN, buff=0.3)

        self.play(Write(perrin_title))
        self.play(Write(perrin_kb))
        self.wait(1)

        # === Part 6: アボガドロ数の計算結果 ===
        # 結果を直接表示
        na_result = MathTex(
            r"N_A \approx 6.5 \times 10^{23} \text{ mol}^{-1}"
        )
        na_result.scale(1.4)
        na_result.set_color(GREEN)
        na_result.next_to(perrin_kb, DOWN, buff=0.6)

        result_box = SurroundingRectangle(na_result, color=GREEN, buff=0.2)

        self.play(Write(na_result))
        self.play(Create(result_box))
        self.wait(1)

        # === Part 7: 現代の値との比較 ===
        self.play(
            FadeOut(na_eq),
            FadeOut(na_box),
            FadeOut(perrin_title),
            FadeOut(perrin_kb),
            VGroup(na_result, result_box).animate.move_to(UP * 0.5),
        )

        # 現代の値
        modern_text = Text("現代の値", font_size=24, color=BLUE)
        modern_na = MathTex(r"N_A = 6.022 \times 10^{23} \text{ mol}^{-1}")
        modern_na.set_color(BLUE)

        modern_group = VGroup(modern_text, modern_na).arrange(DOWN, buff=0.2)
        modern_group.next_to(result_box, DOWN, buff=0.6)

        self.play(Write(modern_group))
        self.wait(1)

        # 最終メッセージ
        final_message = Text(
            "ブラウン運動の観測から分子の数が決定できた！",
            font_size=28,
            color=WHITE
        )
        final_message.to_edge(DOWN, buff=0.5)

        self.play(Write(final_message))
        self.wait(2)

        # フェードアウト
        self.play(*[FadeOut(mob) for mob in self.mobjects])

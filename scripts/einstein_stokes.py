"""
アインシュタイン-ストークスの式の導出アニメーション
フィックの法則とストークスの法則を結びつける
"""

from manim import *


class EinsteinStokes(Scene):
    """フィックの法則とストークスの法則からアインシュタイン-ストークス式を導出"""

    def construct(self):
        # タイトル
        title = Text("アインシュタイン-ストークスの式", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # --- フィックの法則 ---
        fick_title = Text("フィックの法則", font_size=28, color=YELLOW)
        fick_title.move_to(LEFT * 3 + UP * 2)

        fick_eq = MathTex(r"J = -D \frac{d\rho}{dx}")
        fick_eq.next_to(fick_title, DOWN, buff=0.3)

        fick_desc = Text("拡散による粒子の流れ", font_size=20)
        fick_desc.next_to(fick_eq, DOWN, buff=0.2)

        self.play(Write(fick_title))
        self.play(Write(fick_eq))
        self.play(Write(fick_desc))
        self.wait(0.5)

        # --- ストークスの法則 ---
        stokes_title = Text("ストークスの法則", font_size=28, color=BLUE)
        stokes_title.move_to(RIGHT * 3 + UP * 2)

        stokes_eq = MathTex(r"F_{\text{drag}} = -6\pi \eta r v")
        stokes_eq.next_to(stokes_title, DOWN, buff=0.3)

        stokes_desc = Text("粘性抵抗力", font_size=20)
        stokes_desc.next_to(stokes_eq, DOWN, buff=0.2)

        self.play(Write(stokes_title))
        self.play(Write(stokes_eq))
        self.play(Write(stokes_desc))
        self.wait(1)

        # --- 結びつける ---
        # 上の式をフェードアウトして中央に移動
        self.play(
            FadeOut(fick_desc),
            FadeOut(stokes_desc),
            fick_title.animate.move_to(LEFT * 3 + UP * 2.5).scale(0.8),
            fick_eq.animate.move_to(LEFT * 3 + UP * 1.8).scale(0.8),
            stokes_title.animate.move_to(RIGHT * 3 + UP * 2.5).scale(0.8),
            stokes_eq.animate.move_to(RIGHT * 3 + UP * 1.8).scale(0.8),
        )

        # 外力と粘性抵抗の釣り合い
        balance_text = Text("外力 F と粘性抵抗が釣り合うとき", font_size=24)
        balance_text.move_to(UP * 0.5)

        balance_eq = MathTex(r"F = 6\pi \eta r v")
        balance_eq.next_to(balance_text, DOWN, buff=0.3)

        self.play(Write(balance_text))
        self.play(Write(balance_eq))
        self.wait(0.5)

        # 速度を求める
        velocity_eq = MathTex(r"v = \frac{F}{6\pi \eta r}")
        velocity_eq.next_to(balance_eq, DOWN, buff=0.3)

        self.play(TransformFromCopy(balance_eq, velocity_eq))
        self.wait(0.5)

        # 外力による流れ
        self.play(
            FadeOut(balance_text),
            balance_eq.animate.move_to(UP * 0.8).scale(0.8),
            velocity_eq.animate.move_to(UP * 0.2).scale(0.8),
        )

        flow_text = Text("外力による粒子の流れ = 拡散による流れ", font_size=24)
        flow_text.move_to(DOWN * 0.5)

        flow_eq = MathTex(
            r"\frac{\rho F}{6\pi \eta r}",
            r"=",
            r"D \frac{d\rho}{dx}"
        )
        flow_eq.next_to(flow_text, DOWN, buff=0.3)

        self.play(Write(flow_text))
        self.play(Write(flow_eq))
        self.wait(1)

        # --- 熱力学との結びつき ---
        self.play(
            FadeOut(fick_title), FadeOut(fick_eq),
            FadeOut(stokes_title), FadeOut(stokes_eq),
            FadeOut(balance_eq), FadeOut(velocity_eq),
            FadeOut(flow_text), FadeOut(flow_eq),
        )

        # アインシュタイン-ストークスの式
        es_eq = MathTex(r"D = \frac{k_B T}{6\pi \eta r}")
        es_eq.scale(1.5)
        es_eq.move_to(ORIGIN)

        box = SurroundingRectangle(es_eq, color=YELLOW, buff=0.3)

        self.play(Write(es_eq), run_time=2)
        self.play(Create(box))
        self.wait(0.5)

        # 各変数の説明（MathTexとTextを組み合わせ）
        def make_legend_item(symbol, desc):
            sym = MathTex(symbol)
            txt = Text(f" : {desc}", font_size=20)
            return VGroup(sym, txt).arrange(RIGHT, buff=0.1)

        legend = VGroup(
            make_legend_item("D", "拡散係数"),
            make_legend_item("k_B", "ボルツマン定数"),
            make_legend_item("T", "温度"),
            make_legend_item(r"\eta", "粘性係数"),
            make_legend_item("r", "粒子半径"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legend.scale(0.8)
        legend.to_corner(DR)

        self.play(
            title.animate.scale(0.8).to_corner(UL),
        )
        self.play(Write(legend))
        self.wait(0.5)

        # 意義の説明
        significance = Text(
            "マクロな拡散 D とミクロな粒子 r を結びつける！",
            font_size=28,
            color=GREEN
        )
        significance.to_edge(DOWN)

        self.play(Write(significance))
        self.wait(2)

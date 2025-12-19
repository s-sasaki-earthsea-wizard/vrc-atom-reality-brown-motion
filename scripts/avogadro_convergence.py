"""
様々な現象から得られたアボガドロ数の一致
異なる実験方法が同じ値に収束することを示すアニメーション
"""

from manim import *


class AvogadroConvergence(Scene):
    """様々な方法で得られたアボガドロ数が一致"""

    def construct(self):
        # タイトル
        title = Text("様々な方法で得られたアボガドロ数", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 測定方法と値のリスト
        measurements = [
            ("ブラウン運動（ペラン, 1908年）", r"6.5 \times 10^{23}", YELLOW),
            ("黒体放射（プランク, 1900年）", r"6.18 \times 10^{23}", BLUE),
            ("原子核崩壊（1908年）", r"6.09 \times 10^{23}", GREEN),
            ("油滴実験（ミリカン, 1911年）", r"6.06 \times 10^{23}", ORANGE),
            ("X線回折（1913年）", r"6.06 \times 10^{23}", PURPLE),
        ]

        # リスト項目を作成
        items = VGroup()
        for method, value, color in measurements:
            # 方法名
            method_text = Text(method, font_size=22)
            # 値
            value_tex = MathTex(r"N_A \approx " + value, font_size=28)
            value_tex.set_color(color)
            # 横に並べる
            row = VGroup(method_text, value_tex).arrange(RIGHT, buff=0.5)
            items.add(row)

        items.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        items.next_to(title, DOWN, buff=0.8)

        # 1つずつ表示
        for item in items:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)

        self.wait(1)

        # 強調: すべて同じ桁
        highlight_box = SurroundingRectangle(items, color=WHITE, buff=0.3)
        self.play(Create(highlight_box))
        self.wait(0.5)

        # メッセージ
        message1 = Text("全く異なる現象から", font_size=28)
        message2 = Text("同じ値が得られた", font_size=28, color=YELLOW)
        message_group = VGroup(message1, message2).arrange(DOWN, buff=0.2)
        message_group.to_edge(DOWN, buff=1.2)

        self.play(Write(message_group))
        self.wait(1)

        # 結論
        conclusion = Text("→ これは偶然ではありえない！", font_size=32, color=RED)
        conclusion.next_to(message_group, DOWN, buff=0.4)

        self.play(Write(conclusion))
        self.wait(2)

        # フェードアウト
        self.play(*[FadeOut(mob) for mob in self.mobjects])

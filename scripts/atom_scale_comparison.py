"""
原子スケール比較アニメーション
テニスボール（6.6cm）を46,000倍に拡大すると約2.1kmになる
→ 東京スカイツリー（634m）約3.3個分の高さ
"""

from manim import *


class AtomScaleComparison(Scene):
    """テニスボール拡大によるスケール感の可視化"""

    def construct(self):
        # === Part 1: テニスボールの紹介 ===
        title = Text("原子を「見える」ようにするスケール", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # テニスボールを表示
        tennis_ball = Circle(radius=1.2, color=YELLOW_C, fill_opacity=0.8)
        tennis_ball.set_fill(YELLOW_C, opacity=0.8)
        tennis_ball.set_stroke(YELLOW_D, width=3)

        # テニスボールの模様（曲線）
        seam1 = Arc(radius=1.0, start_angle=PI/4, angle=PI/2, color=WHITE)
        seam2 = Arc(radius=1.0, start_angle=-3*PI/4, angle=PI/2, color=WHITE)
        tennis_ball_group = VGroup(tennis_ball, seam1, seam2)
        tennis_ball_group.move_to(ORIGIN)

        # サイズラベル
        size_label = Text("テニスボール", font_size=28)
        size_label.next_to(tennis_ball_group, DOWN, buff=0.3)
        size_value = MathTex(r"\phi = 6.6 \text{ cm}", font_size=32)
        size_value.next_to(size_label, DOWN, buff=0.2)

        self.play(
            FadeIn(tennis_ball_group, scale=0.5),
            Write(size_label),
            Write(size_value)
        )
        self.wait(1)

        # === Part 2: 拡大率の説明 ===
        # 説明テキスト
        explanation = Text(
            "原子（0.1-0.3nm）がマイクロメートルの世界で見える",
            font_size=24
        )
        explanation.next_to(title, DOWN, buff=0.3)
        self.play(Write(explanation))
        self.wait(0.5)

        # 拡大率
        magnification = MathTex(r"\times 46,000", font_size=64, color=RED)
        magnification.next_to(tennis_ball_group, RIGHT, buff=1)

        self.play(Write(magnification))
        self.wait(0.5)

        # === Part 3: 拡大後のサイズ ===
        # 計算式
        calc = MathTex(
            r"6.6 \text{ cm} \times 46,000 = 3,036 \text{ m} \approx 3 \text{ km}",
            font_size=28
        )
        calc.to_edge(DOWN, buff=1.5)
        self.play(Write(calc))
        self.wait(1)

        # 画面をクリア
        self.play(
            FadeOut(tennis_ball_group),
            FadeOut(size_label),
            FadeOut(size_value),
            FadeOut(magnification),
            FadeOut(calc),
            FadeOut(explanation)
        )

        # === Part 4: スカイツリーを縦に積み上げて比較 ===
        comparison_title = Text("どれくらい大きい？", font_size=32)
        comparison_title.next_to(title, DOWN, buff=0.3)
        self.play(Write(comparison_title))

        # スカイツリーを描画（シンプルな形状）
        def create_skytree(height=0.6, color=BLUE):
            """スカイツリーのシンプルな形状"""
            # メインタワー（細長い台形）
            tower = Polygon(
                [-0.08, 0, 0],
                [0.08, 0, 0],
                [0.04, height * 0.7, 0],
                [-0.04, height * 0.7, 0],
                color=color,
                fill_opacity=0.8
            )
            # アンテナ部分
            antenna = Line(
                [0, height * 0.7, 0],
                [0, height, 0],
                color=color,
                stroke_width=2
            )
            # 展望台（下）
            obs1 = Rectangle(width=0.2, height=0.03, color=color, fill_opacity=0.8)
            obs1.move_to([0, height * 0.45, 0])
            # 展望台（上）
            obs2 = Rectangle(width=0.15, height=0.025, color=color, fill_opacity=0.8)
            obs2.move_to([0, height * 0.58, 0])

            return VGroup(tower, antenna, obs1, obs2)

        # スカイツリーを縦に5個積み上げる
        skytree_unit_height = 0.6  # 1個あたりの画面上の高さ
        skytrees = VGroup()

        for i in range(5):
            st = create_skytree(height=skytree_unit_height, color=BLUE_C)
            # 下から順に積み上げ
            st.move_to([0, i * skytree_unit_height + skytree_unit_height / 2, 0])
            skytrees.add(st)

        # 全体を画面左側に配置
        skytrees.move_to(LEFT * 4.5 + DOWN * 0.3)

        # スカイツリー1個分のラベル
        st_label = Text("634m", font_size=16, color=BLUE_C)
        st_label.next_to(skytrees[0], LEFT, buff=0.15)

        # 5個分の高さを示すブラケット
        brace = Brace(skytrees, RIGHT, color=WHITE)
        brace_label = Text("5個 = 3,170m", font_size=18)
        brace_label.next_to(brace, RIGHT, buff=0.1)

        # スカイツリーを1個ずつ積み上げるアニメーション
        self.play(FadeIn(skytrees[0], shift=UP * 0.3), Write(st_label))
        for i in range(1, 5):
            self.play(FadeIn(skytrees[i], shift=UP * 0.3), run_time=0.4)

        self.play(GrowFromCenter(brace), Write(brace_label))
        self.wait(0.5)

        # === Part 5: 巨大テニスボールとの比較 ===
        # 巨大テニスボール（直径がスカイツリー4.7個分 ≈ 5個弱）
        ball_diameter = skytree_unit_height * 4.7  # 4.7個分
        giant_ball = Circle(radius=ball_diameter / 2, color=YELLOW_C, fill_opacity=0.6)
        giant_ball.set_stroke(YELLOW_D, width=4)

        # ボールを右側に配置（中心がスカイツリーの高さの中央くらい）
        giant_ball.move_to(RIGHT * 1.5 + DOWN * 0.3)

        # ボールのラベル
        ball_label = Text("拡大したテニスボール", font_size=20, color=YELLOW)
        ball_label.next_to(giant_ball, UP, buff=0.2)

        # 直径を示す線
        diameter_line = Line(
            giant_ball.get_left(),
            giant_ball.get_right(),
            color=RED,
            stroke_width=3
        )
        diameter_value = Text("直径 3km", font_size=20, color=RED)
        diameter_value.next_to(diameter_line, DOWN, buff=0.1)

        self.play(
            FadeIn(giant_ball, scale=0.5),
            Write(ball_label)
        )
        self.wait(0.3)
        self.play(Create(diameter_line), Write(diameter_value))
        self.wait(0.5)

        # 比較説明テキスト
        compare_text = Text("≈ スカイツリー 4.7個分の直径！", font_size=24, color=WHITE)
        compare_text.to_edge(DOWN, buff=1.2)
        self.play(Write(compare_text))
        self.wait(1)

        # === Part 6: 最終メッセージ ===
        self.play(FadeOut(compare_text))

        final_message = Text(
            "これほどの拡大で、初めて原子の存在が見えた",
            font_size=28,
            color=WHITE
        )
        final_message.to_edge(DOWN, buff=0.5)

        self.play(Write(final_message))
        self.wait(2)

        # フェードアウト
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class AtomScaleComparisonSimple(Scene):
    """シンプル版：テニスボールとスカイツリーの比較"""

    def construct(self):
        # タイトル
        title = Text("スケール比較", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))

        # 左側：元のテニスボール
        tennis_small = Circle(radius=0.3, color=YELLOW_C, fill_opacity=0.8)
        tennis_small.move_to(LEFT * 4)
        label_small = Text("6.6 cm", font_size=20)
        label_small.next_to(tennis_small, DOWN)

        # 右側：拡大後を示すスカイツリー群
        def create_mini_skytree(h=1.5):
            tower = Polygon(
                [-0.1, 0, 0], [0.1, 0, 0],
                [0.05, h, 0], [-0.05, h, 0],
                color=BLUE_C, fill_opacity=0.7
            )
            return tower

        skytrees = VGroup(*[create_mini_skytree() for _ in range(4)])
        skytrees.arrange(RIGHT, buff=0.3)
        skytrees.move_to(RIGHT * 2)

        # 矢印と倍率
        arrow = Arrow(LEFT * 2.5, RIGHT * 0, color=RED, buff=0.3)
        mult_text = MathTex(r"\times 46,000", color=RED, font_size=28)
        mult_text.next_to(arrow, UP)

        self.play(FadeIn(tennis_small), Write(label_small))
        self.wait(0.5)
        self.play(GrowArrow(arrow), Write(mult_text))
        self.wait(0.5)
        self.play(
            LaggedStart(*[FadeIn(st, shift=UP) for st in skytrees], lag_ratio=0.2)
        )

        # スカイツリーラベル
        st_text = Text("≈ スカイツリー4.7個分", font_size=24, color=BLUE_C)
        st_text.next_to(skytrees, DOWN)
        result = MathTex(r"= 3 \text{ km}", font_size=32)
        result.next_to(st_text, DOWN)

        self.play(Write(st_text), Write(result))
        self.wait(2)

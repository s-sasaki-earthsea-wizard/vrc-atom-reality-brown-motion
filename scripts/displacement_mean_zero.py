"""
ブラウン運動の変位: 平均が0になることの視覚化
複数の粒子の軌跡を同時に描画し、平均が0に近づくことを示す
"""

from manim import *
import numpy as np


class DisplacementMeanZero(Scene):
    """ブラウン運動の変位が平均0になることを示す"""

    def construct(self):
        # 乱数シード
        np.random.seed(1218)

        # パラメータ
        n_particles = 15  # 粒子数
        n_steps = 100     # ステップ数

        # 座標軸
        axes = Axes(
            x_range=[0, n_steps, 20],
            y_range=[-20, 20, 5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        )

        # 軸ラベル
        x_label = Text("時間 t", font_size=20)
        x_label.next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"\Delta x")
        y_label.next_to(axes.y_axis, UP)

        # ゼロライン（基準線）
        zero_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(n_steps, 0),
            color=GRAY,
            dash_length=0.1
        )

        # タイトル
        title = Text("ブラウン運動の変位", font_size=32)
        title.to_edge(UP)

        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(zero_line))
        self.wait(0.3)

        # 複数粒子のランダムウォークを生成
        all_positions = []
        colors = [YELLOW, BLUE, RED, GREEN, ORANGE, PINK, PURPLE, TEAL, MAROON, GOLD,
                  LIGHT_BROWN, LIGHT_GRAY, DARK_BLUE, LIGHT_PINK, PURE_GREEN]

        for _ in range(n_particles):
            steps = np.random.choice([-1, 1], size=n_steps)
            positions = np.cumsum(steps)
            positions = np.insert(positions, 0, 0)
            all_positions.append(positions)

        all_positions = np.array(all_positions)

        # 各粒子の軌跡を初期化
        paths = []
        for i in range(n_particles):
            path = VMobject()
            path.set_points_as_corners([axes.c2p(0, 0), axes.c2p(0, 0)])
            path.set_color(colors[i % len(colors)])
            path.set_stroke(width=2, opacity=0.7)
            paths.append(path)
            self.add(path)

        # 時間発展のアニメーション
        step_interval = 2  # 2ステップごとに更新
        for t in range(step_interval, n_steps + 1, step_interval):
            new_paths = []
            for i in range(n_particles):
                path_points = [axes.c2p(s, all_positions[i][s])
                              for s in range(0, t + 1, step_interval)]
                new_path = VMobject()
                new_path.set_points_as_corners(path_points)
                new_path.set_color(colors[i % len(colors)])
                new_path.set_stroke(width=2, opacity=0.7)
                new_paths.append(new_path)

            self.play(
                *[Transform(paths[i], new_paths[i]) for i in range(n_particles)],
                run_time=0.05
            )

        self.wait(0.5)

        # 平均を計算
        mean_positions = np.mean(all_positions, axis=0)

        # 平均の軌跡を太く描画
        mean_path_points = [axes.c2p(t, mean_positions[t])
                           for t in range(0, n_steps + 1, step_interval)]
        mean_path = VMobject()
        mean_path.set_points_as_corners(mean_path_points)
        mean_path.set_color(WHITE)
        mean_path.set_stroke(width=5)

        mean_label = Text("平均", font_size=24, color=WHITE)
        mean_label.move_to(axes.c2p(80, 15))

        self.play(Create(mean_path), Write(mean_label), run_time=1.5)
        self.wait(0.5)

        # 説明テキスト
        explanation = Text(
            "個々はバラバラ、でも平均すると0に近づく！",
            font_size=24
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        # 平均の式
        mean_eq = MathTex(r"\langle \Delta x \rangle = 0")
        mean_eq.scale(1.2)
        mean_eq.next_to(explanation, UP, buff=0.3)
        mean_eq.set_color(GREEN)

        self.play(Write(mean_eq))
        self.wait(2)

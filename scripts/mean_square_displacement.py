"""
変位の二乗平均が時間に比例することを示すアニメーション
複数の粒子の軌跡を同時に描画し、最後に平均を表示
"""

from manim import *
import numpy as np


class MeanSquareDisplacement(Scene):
    """変位の二乗平均が時間に比例することを視覚化"""

    def construct(self):
        # 乱数シード
        np.random.seed(1219)

        # パラメータ
        n_particles = 25  # 粒子数
        n_steps = 300     # ステップ数

        # 座標軸
        axes = Axes(
            x_range=[0, n_steps, 50],
            y_range=[0, 400, 100],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        )

        # 軸ラベル
        x_label = Text("時間 t", font_size=20)
        x_label.next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"(\Delta x)^2")
        y_label.next_to(axes.y_axis, UP)

        # タイトル
        title = Text("変位の二乗", font_size=32)
        title.to_edge(UP)

        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.3)

        # 複数粒子のランダムウォークを生成
        all_displacement_squared = []
        colors = [YELLOW, BLUE, RED, GREEN, ORANGE, PINK, PURPLE, TEAL, MAROON, GOLD]

        for _ in range(n_particles):
            steps = np.random.choice([-1, 1], size=n_steps)
            positions = np.cumsum(steps)
            positions = np.insert(positions, 0, 0)
            displacement_squared = positions ** 2
            all_displacement_squared.append(displacement_squared)

        all_displacement_squared = np.array(all_displacement_squared)

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
        step_interval = 3  # 3ステップごとに更新
        for t in range(step_interval, n_steps + 1, step_interval):
            new_paths = []
            for i in range(n_particles):
                path_points = [axes.c2p(s, all_displacement_squared[i][s])
                              for s in range(0, t + 1, step_interval)]
                new_path = VMobject()
                new_path.set_points_as_corners(path_points)
                new_path.set_color(colors[i % len(colors)])
                new_path.set_stroke(width=2, opacity=0.7)
                new_paths.append(new_path)

            self.play(
                *[Transform(paths[i], new_paths[i]) for i in range(n_particles)],
                run_time=0.03
            )

        self.wait(0.5)

        # 平均を計算
        mean_displacement_squared = np.mean(all_displacement_squared, axis=0)

        # 平均の軌跡を太く描画
        mean_path_points = [axes.c2p(t, mean_displacement_squared[t])
                           for t in range(0, n_steps + 1, step_interval)]
        mean_path = VMobject()
        mean_path.set_points_as_corners(mean_path_points)
        mean_path.set_color(WHITE)
        mean_path.set_stroke(width=5)

        mean_label = Text("平均", font_size=24, color=WHITE)
        mean_label.move_to(axes.c2p(250, 350))

        self.play(Create(mean_path), Write(mean_label), run_time=1.5)
        self.wait(0.5)

        # 理論線（時間に比例）
        theory_line = axes.plot(
            lambda t: t,  # ⟨(Δx)²⟩ ∝ t
            x_range=[0, n_steps],
            color=GREEN
        )
        theory_line.set_stroke(width=3, opacity=0.8)

        theory_label = MathTex(r"\langle (\Delta x)^2 \rangle = 2Dt", color=GREEN)
        theory_label.scale(0.9)
        theory_label.move_to(axes.c2p(200, 100))

        self.play(Create(theory_line), Write(theory_label))
        self.wait(0.5)

        # 説明
        explanation = Text(
            "個々はバラバラ、でも平均すると時間に比例！",
            font_size=24
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(2)

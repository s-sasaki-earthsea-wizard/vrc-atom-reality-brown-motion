"""
2Dブラウン運動のアニメーション
平面上でランダムウォークする粒子とその軌跡を描画
粒子はt=0で原点からスタート
"""

from manim import *
import numpy as np


class BrownianMotion2D(Scene):
    """平面上のブラウン運動をシミュレーション"""

    def construct(self):
        # 乱数シード
        np.random.seed(42)

        # パラメータ
        n_steps = 500  # ステップ数
        step_size = 0.16  # 1ステップあたりの移動量

        # 座標軸
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=7,
            axis_config={"include_tip": True, "color": GREY},
        )

        # 軸ラベル
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis, UP)

        # タイトル
        title = Text("ブラウン運動の軌跡", font_size=32)
        title.to_edge(UP)

        # 原点マーカー
        origin_dot = Dot(axes.c2p(0, 0), color=GREEN, radius=0.08)
        origin_label = Text("t=0", font_size=18, color=GREEN)
        origin_label.next_to(origin_dot, DOWN, buff=0.1)

        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(origin_dot), Write(origin_label))
        self.wait(0.3)

        # 2Dランダムウォークを生成
        angles = np.random.uniform(0, 2 * np.pi, n_steps)
        dx = step_size * np.cos(angles)
        dy = step_size * np.sin(angles)

        # 累積和で位置を計算（原点からスタート）
        x_positions = np.cumsum(dx)
        y_positions = np.cumsum(dy)
        x_positions = np.insert(x_positions, 0, 0)
        y_positions = np.insert(y_positions, 0, 0)

        # 軌跡のパスを事前に完全に生成
        path_points = [axes.c2p(x_positions[i], y_positions[i])
                      for i in range(len(x_positions))]
        full_path = VMobject()
        full_path.set_points_as_corners(path_points)
        full_path.set_color(BLUE)
        full_path.set_stroke(width=2, opacity=0.8)

        # 粒子（現在位置を表すドット）
        particle = Dot(axes.c2p(0, 0), color=YELLOW, radius=0.12)
        particle.set_z_index(10)

        # 粒子を軌跡に沿って動かすためのupdater
        def update_particle(mob, alpha):
            idx = int(alpha * (len(x_positions) - 1))
            mob.move_to(axes.c2p(x_positions[idx], y_positions[idx]))

        self.add(particle)

        # 軌跡を描画しながら粒子を動かす
        self.play(
            Create(full_path, rate_func=linear),
            UpdateFromAlphaFunc(particle, update_particle, rate_func=linear),
            run_time=3
        )

        self.wait(0.5)

        # 終点マーカー
        end_dot = Dot(
            axes.c2p(x_positions[-1], y_positions[-1]),
            color=RED,
            radius=0.08
        )
        end_label = Text("t=T", font_size=18, color=RED)
        end_label.next_to(end_dot, UP, buff=0.1)

        self.play(Create(end_dot), Write(end_label))
        self.wait(0.5)

        # 説明テキスト
        explanation = Text(
            "個々の粒子の動きは不規則で予測不可能",
            font_size=24
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(2)


class BrownianMotionMultiple(Scene):
    """複数粒子のブラウン運動を同時に表示"""

    def construct(self):
        # 乱数シード
        np.random.seed(1234)

        # パラメータ
        n_particles = 5  # 粒子数
        n_steps = 400  # ステップ数
        step_size = 0.16  # 1ステップあたりの移動量

        # 座標軸
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=7,
            axis_config={"include_tip": True, "color": GREY},
        )

        # 軸ラベル
        x_label = MathTex("x").next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y").next_to(axes.y_axis, UP)

        # タイトル
        title = Text("ブラウン運動する粒子たち", font_size=32)
        title.to_edge(UP)

        # 原点マーカー
        origin_dot = Dot(axes.c2p(0, 0), color=WHITE, radius=0.1)
        origin_label = Text("原点 (t=0)", font_size=18, color=WHITE)
        origin_label.next_to(origin_dot, DOWN, buff=0.15)

        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(origin_dot), Write(origin_label))
        self.wait(0.3)

        # 色のリスト
        colors = [YELLOW, BLUE, RED, GREEN, ORANGE]

        # 各粒子のランダムウォークを生成
        all_x = []
        all_y = []
        for _ in range(n_particles):
            angles = np.random.uniform(0, 2 * np.pi, n_steps)
            dx = step_size * np.cos(angles)
            dy = step_size * np.sin(angles)
            x_pos = np.cumsum(dx)
            y_pos = np.cumsum(dy)
            x_pos = np.insert(x_pos, 0, 0)
            y_pos = np.insert(y_pos, 0, 0)
            all_x.append(x_pos)
            all_y.append(y_pos)

        # 各粒子のパスを事前に生成
        full_paths = []
        particles = []
        for i in range(n_particles):
            # パスを完全に生成
            path_points = [axes.c2p(all_x[i][j], all_y[i][j])
                          for j in range(len(all_x[i]))]
            full_path = VMobject()
            full_path.set_points_as_corners(path_points)
            full_path.set_color(colors[i])
            full_path.set_stroke(width=2, opacity=0.7)
            full_paths.append(full_path)

            # 粒子
            particle = Dot(axes.c2p(0, 0), color=colors[i], radius=0.1)
            particle.set_z_index(10)
            particles.append(particle)
            self.add(particle)

        # 粒子のupdater関数を生成
        def make_updater(x_pos, y_pos):
            def update_particle(mob, alpha):
                idx = int(alpha * (len(x_pos) - 1))
                mob.move_to(axes.c2p(x_pos[idx], y_pos[idx]))
            return update_particle

        # 全ての軌跡と粒子を同時にアニメーション
        animations = []
        for i in range(n_particles):
            animations.append(Create(full_paths[i], rate_func=linear))
            animations.append(
                UpdateFromAlphaFunc(
                    particles[i],
                    make_updater(all_x[i], all_y[i]),
                    rate_func=linear
                )
            )

        self.play(*animations, run_time=3)

        self.wait(0.5)

        # 説明
        explanation = Text(
            "全ての粒子が原点から出発しても、バラバラの方向に広がる",
            font_size=22
        )
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        self.wait(2)

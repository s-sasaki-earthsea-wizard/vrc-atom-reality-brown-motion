"""
ストークスの法則のアニメーション
水中を落下するボールが終端速度に達する様子を表示
重力と粘性抵抗力が釣り合い、等速直線運動になる
"""

from manim import *
import numpy as np


class StokesLaw(Scene):
    """ストークスの法則: 粘性流体中の落下運動"""

    def construct(self):
        # 背景を水色に設定
        self.camera.background_color = "#1a5276"

        # パラメータ設定
        g = 9.8          # 重力加速度
        m = 1.0          # 質量
        gamma = 2.0      # 抵抗係数 (6πηr)
        tau = m / gamma  # 時定数
        v_terminal = m * g / gamma  # 終端速度

        # 速度の時間発展: v(t) = v_terminal * (1 - e^(-t/τ))
        def velocity(t):
            return v_terminal * (1 - np.exp(-t / tau))

        # 位置の時間発展: y(t) = v_terminal * (t - τ(1 - e^(-t/τ)))
        def position(t):
            return v_terminal * (t - tau * (1 - np.exp(-t / tau)))

        # 水面より上（空気）を黒で塗る
        air_region = Rectangle(
            width=14.2,
            height=1.5,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        air_region.move_to(UP * 3.75)

        # 水面を表示
        water_surface = Line(LEFT * 7.1, RIGHT * 7.1, color=WHITE, stroke_width=2)
        water_surface.move_to(UP * 3)
        water_label = Text("水面", font_size=24)
        water_label.next_to(water_surface, DOWN + RIGHT)

        # ストークスの法則の式（中央寄り）
        stokes_eq = MathTex(r"F_{\text{drag}} = -6\pi \eta r v")
        stokes_eq.scale(0.7)
        stokes_eq.move_to(RIGHT * 3 + UP * 2)
        stokes_eq.set_color(WHITE)

        # 力のバランス説明
        force_eq = MathTex(r"mg = 6\pi \eta r v_{\text{terminal}}")
        force_eq.scale(0.6)
        force_eq.next_to(stokes_eq, DOWN)
        force_eq.set_color(YELLOW)

        self.add(air_region)  # 背景として追加
        self.play(Create(water_surface), Write(water_label))
        self.play(Write(stokes_eq))
        self.wait(0.5)

        # ボールの初期位置（中央寄り）
        ball = Circle(radius=0.3, color=RED, fill_opacity=1)
        x_pos = 0  # 中央
        y_start = 2.5
        ball.move_to(UP * y_start + RIGHT * x_pos)

        # 力の矢印
        gravity_arrow = Arrow(
            ball.get_center(),
            ball.get_center() + DOWN * 1.2,
            color=YELLOW,
            buff=0.3
        )
        drag_arrow = Arrow(
            ball.get_center(),
            ball.get_center() + UP * 0.1,
            color=GREEN,
            buff=0.3
        )

        self.play(Create(ball))
        self.wait(0.3)

        # シミュレーション
        total_time = 4.0
        dt = 0.1  # 単位時間（細かくする）
        num_steps = int(total_time / dt)

        # 位置の履歴を保持するドット
        trail_dots = VGroup()

        # 速度表示（中央上部）
        velocity_text = Text(f"v = 0.00", font_size=24)
        velocity_text.move_to(LEFT * 3 + UP * 2)

        self.play(Write(velocity_text), run_time=0.3)

        for i in range(num_steps):
            t_next = (i + 1) * dt

            # 現在の速度
            v = velocity(t_next)
            v_normalized = v / v_terminal  # 正規化（0〜1）

            # 現在の位置（スケール調整）
            y_offset = position(t_next) * 0.6
            new_y = y_start - y_offset

            # 画面外に出たら終了
            if new_y < -3.5:
                break

            # ボールを移動
            new_pos = np.array([x_pos, new_y, 0])

            # 軌跡のドットを追加（単位時間ごとの位置）
            trail_dot = Dot(ball.get_center(), color=WHITE, radius=0.06)
            trail_dot.set_opacity(0.7)
            trail_dots.add(trail_dot)

            # 力の矢印を更新
            new_gravity = Arrow(
                new_pos,
                new_pos + DOWN * 1.0,
                color=YELLOW,
                buff=0.3
            )
            new_drag = Arrow(
                new_pos,
                new_pos + UP * (1.0 * v_normalized),
                color=GREEN,
                buff=0.3
            )

            # 速度テキスト更新
            new_velocity_text = Text(
                f"v = {v:.2f}",
                font_size=24
            )
            new_velocity_text.move_to(LEFT * 3 + UP * 2)

            # 連続的にアニメーション（一時停止なし）
            self.play(
                ball.animate.move_to(new_pos),
                Transform(gravity_arrow, new_gravity),
                Transform(drag_arrow, new_drag),
                Transform(velocity_text, new_velocity_text),
                FadeIn(trail_dot),
                run_time=0.08
            )

        # 終端速度に達したことを表示
        self.play(Write(force_eq))

        terminal_text = Text(
            "重力と粘性抵抗が釣り合い → 等速直線運動",
            font_size=24
        )
        terminal_text.to_edge(DOWN)
        self.play(Write(terminal_text))

        # ドットの間隔が等間隔になっていることを強調
        interval_note = Text(
            "ドットの間隔: 最初は狭い → 徐々に一定に",
            font_size=20,
            color=YELLOW
        )
        interval_note.next_to(terminal_text, UP)
        self.play(Write(interval_note))

        self.wait(2)

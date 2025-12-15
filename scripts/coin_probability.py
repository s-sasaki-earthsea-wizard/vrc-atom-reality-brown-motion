"""
コイン投げの確率収束アニメーション
試行回数が増えるにつれて表・裏の確率が50%に収束する様子を表示
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 日本語フォント設定（環境に応じて変更）
plt.rcParams['font.family'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'sans-serif']

# 乱数シード固定（再現性のため）
np.random.seed(42)

# パラメータ
max_flips = 10000  # 最大試行回数
frames = 2000      # アニメーションのフレーム数

# コイン投げの結果を事前に生成（0: 裏, 1: 表）
flips = np.random.randint(0, 2, max_flips)

# 各フレームでの試行回数を計算（対数的に増加させてスムーズに）
flip_counts = np.unique(np.logspace(0, np.log10(max_flips), frames).astype(int))
flip_counts = np.clip(flip_counts, 1, max_flips)

# グラフの設定
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(0, 1)
ax.set_xticks([0, 1])
ax.set_xticklabels(['表', '裏'])
ax.set_ylabel('確率')
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.7, label='理論値 (50%)')

# バーの初期化
bars = ax.bar([0, 1], [0, 0], color=['red', 'blue'], width=0.6)
title = ax.set_title('試行回数: 0')
ax.legend(loc='upper right')


def update(frame):
    """アニメーションの各フレームを更新"""
    n = flip_counts[frame]

    # 現在までの結果を集計
    heads = np.sum(flips[:n])  # 表の回数
    tails = n - heads          # 裏の回数

    # 確率を計算
    p_heads = heads / n
    p_tails = tails / n

    # バーの高さを更新
    bars[0].set_height(p_heads)
    bars[1].set_height(p_tails)

    # タイトルを更新
    title.set_text(f'試行回数: {n}')

    return bars, title


# アニメーション作成
ani = animation.FuncAnimation(
    fig, update, frames=len(flip_counts),
    interval=50, blit=False, repeat=False
)

# 保存または表示
if __name__ == '__main__':
    # mp4として保存する場合
    ani.save('coin_probability.mp4', writer='ffmpeg', fps=30, dpi=150)

    # 画面に表示
    plt.tight_layout()
    plt.show()

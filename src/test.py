# Library
import numpy as np
import matplotlib.pyplot as plt
import collections
import random

# params
dataLength = 10  # １つのデータの配列の点数
frame = 25  # プロットするフレーム数
sleepTime = 1  # １フレーム表示する時間[s]

# history = collections.deque(maxlen=dataLength)

# plot
if __name__== "__main__":
    # try:
    for i in range(frame): # フレーム回数分グラフを更新
        data = np.random.rand() # プロットするデータを作成
        # history.append(data)
        # x = list(range(i-len(history), i))
        plt.cla() # プロットした点を消してグラフを初期化
        plt.plot(data,data, marker="o", color="r", markersize=2) # データをプロット
        plt.draw() # グラフを画面に表示開始
        plt.pause(sleepTime) # SleepTime時間だけ表示を継続
        print(random.randrange(10, 20, 3))
    # except KeyboardInterrupt:
        # plt.close()
# plt.close()
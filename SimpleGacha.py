# シンプルなガチャ機能の実装
# https://qiita.com/saib-ryo/items/dffb3ab05762cdc26da0

# random.choices(population, weights=None, *, cum_weights=None, k=1)
# population から重複ありで選んだ要素からなる大きさ k のリストを返します。population が空の場合 IndexError を送出します。

import random

# 抽選対象のアイテムIDと重みのdictionary
item_dic = { \
    "SSR":1, \
    "SR":10, \
    "R":100, \
}


items = tuple(item_dic.keys())
weights = item_dic.values()

# ガチャ回数
times = 10

print(random.choices(items, weights=weights, k=times))

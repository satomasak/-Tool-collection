#データの日付の最大値最小値を取得し期間を設定する
max_day = selldf[['取引年月日']].values.max()
min_day = selldf[['取引年月日']].values.min()
#データの期間を作成
days = min_day+'～'+max_day

import datetime
#エクセルから読み込んだ日付をdate型に変換
min_dt = datetime.datetime.strptime(min_day, '%Y.%m.%d')
max_dt = datetime.datetime.strptime(max_day, '%Y.%m.%d')

str(max_dt.year)+'年'+str(max_dt.month)+'月'

#max_dt.yearは数値扱いなので計算可能　期間の計算
count_year = max_dt.year - min_dt.year
count_month = 12 - min_dt.month +1
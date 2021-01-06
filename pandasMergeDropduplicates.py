import pandas as pd

#得意先コードで連結
mergdf = pd.merge(chaindf,proddf,on="得意先ｺｰﾄﾞ")
#いらない列を削除　デフォルトのaxis=0は行
mergdf = mergdf.drop(['得意先ｺｰﾄﾞ','得意先名_x','得意先名_y'], axis=1)
#2列の条件で重複するデータを削除
mergdf = mergdf.drop_duplicates(subset=['チェーンコード','商品ｺｰﾄﾞ'])
#列の並び替え
mergdf = mergdf.reindex(columns=['チェーンコード','チェーン名','取引区分','商品ｺｰﾄﾞ','商品名'])

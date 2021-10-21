#人口割合の時間変化をプロット (n 戦略間のダイナミクス)
#出力形式pdfバージョン(データ数が多く実行時間・ファイルの処理が比較的遅いので注意)

#data
state = ARG1 #状態数
file = ARG2 #入力ファイル名
set datafile separator ","

#get column
stats file every ::0:0:1:0
rowlength = STATS_columns

#output
set terminal pdfcairo size 10, 6  #出力のキャンバスサイズ指定
file_name = sprintf("dynamics_%s.pdf", ARG2[8:21])
set output file_name

# x axis 
set xrange[0:] 
set xlabel "time"
set xlabel font "Arial,24"  #x軸ラベルのフォントの種類とサイズ指定

# y axis
set yrange[0:1]
set ylabel "abundance"
set ylabel font "Arial,24"  #y軸ラベルのフォントの種類とサイズ指定

#color 
call "color.gp" 1 2 state #ARG1＝0(固定パレット)/1(色相環使用), ARG2＝見出しの列数, ARG3=状態数(2 or 3)

#graph setting
set size 1,1  #図の比率
set size ratio 0.7  #図の倍率
set key outside
set key font "Arial,15"  #凡例のフォントの種類とサイズ指定 
set tics font "Arial,15"  #目盛りのフォントの種類とサイズ指定
unset colorbox
#unset key

#plot (戦略ごとに色を変える、凡例は戦略名)
plot for [i=3:rowlength] file using 1:i with lines linewidth 5 \
    linecolor palette frac color_decision(i) \
    title columnheader(i)

unset output




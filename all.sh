sed 1d < cutaruki_0.csv > _cutaruki_0_wo_title.csv
sed 1d < cutaruki_1.csv > _cutaruki_1_wo_tilte.csv

python3 accel2svm.py _cutaruki_0_wo_title.csv _cutaruki_1_wo_tilte.csv _data.unsorted.txt



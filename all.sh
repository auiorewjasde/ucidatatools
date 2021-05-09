sed 1d < cutaruki_0.csv > _cutaruki_0_wo_title.csv
sed 1d < cutaruki_1.csv > _cutaruki_1_wo_title.csv

python3 accel2svm.py _cutaruki_0_wo_title.csv 0 _data0.unsorted.txt _data0.sorted.txt
python3 accel2svm.py _cutaruki_1_wo_title.csv 1 _data1.unsorted.txt _data1.sorted.txt



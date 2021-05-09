sed 1d < cutaruki_0.csv > _cutaruki_0_wo_title.csv
sed 1d < cutaruki_1.csv > _cutaruki_1_wo_title.csv

python3 accel2svm.py _cutaruki_0_wo_title.csv 0 _data0.unsorted.txt _data0.sorted.txt
python3 accel2svm.py _cutaruki_1_wo_title.csv 1 _data1.unsorted.txt _data1.sorted.txt




python3 accel2knn.py _cutaruki_0_wo_title.csv 0 _data0.knn.unsorted.txt _data0.knn.sorted.txt
python3 accel2knn.py _cutaruki_1_wo_title.csv 1 _data1.knn.unsorted.txt _data1.knn.sorted.txt


#cat _data0.knn.sorted.txt _data1.knn.sorted.txt > _dataX.knn.sorted.txt
#sed 1d < _dataX.knn.sorted.txt > _dataX.knn.sorted.trai.txt
#head -1 _dataX.knn.sorted.txt > _dataX.knn.sorted.test.txt
#python3 k-nn.py 10 6144 _dataX.knn.sorted.trai.txt _dataX.knn.sorted.test.txt


all : __.txt
__.txt : _s_y_x.all.txt
	rm -f __*s*a*.txt
	python3 separate_by_subj_and_acti.py _s_y_x.all.txt
	touch __.txt | rm -f __.txt
_s_y_x.all.txt : test_subject_test.txt test_X_test.txt test_y_train.txt train_subject_test.txt train_X_test.txt train_y_train.txt
	paste train_subject_test.txt train_y_train.txt train_X_test.txt >_s_y_x.all.txt
	paste test_subject_test.txt test_y_train.txt test_X_test.txt >> _s_y_x.all.txt

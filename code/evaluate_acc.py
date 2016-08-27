# Evalute the accuracy

import numpy as np
from load_datas import *
import pdb


# ground truth label path
GT_label_path = '../../labels/'

# prediction label path
pred_label_path = '../../labels/'

#load_train_labels(label_path,'obj',setting_index=0)
GT  =load_test_labels(GT_label_path, 'obj',setting_index=0)
pred=load_test_labels(pred_label_path, 'obj',setting_index=0)


GT_seq=np.zeros((0))
pred_seq=np.zeros((0))

for i in xrange(len(GT)):
    GT_seq=np.append(GT_seq, GT[i])
    pred_seq  =np.append(pred_seq, pred[i])

correct = np.count_nonzero(GT_seq==pred_seq)
total = len(GT_seq)
print "testing acc. = %.2f%%, %d/%d" %(correct/float(total)*100, correct, total)

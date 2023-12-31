from sklearn.metrics import confusion_matrix
import numpy as np


def MCC(y_test, pred_labels):
    confusion = confusion_matrix(y_test, pred_labels)
    # MCM返回的每一个二分类混淆矩阵中，TN在[0, 0] ，FN在[1, 0], TP在[1, 1], FP在[1, 0]
    tn, fn, tp, fp = confusion[0, 0], confusion[1, 0], confusion[1, 1], confusion[1, 0]
#     tn, fp, fn, tp = confusion_matrix(y_test, pred_labels).ravel()
    MCC_score = (tp*tn-fp*fn)/(((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**0.5)

    return MCC_score


def main():
    y_test = np.zeros(100)
    y_test[10:20] = 1
    y_test[50:60] = 1
    pred_labels = np.zeros(100)
    pred_labels[15:17] = 1
    pred_labels[55:62] = 1
    # pred_labels[51:55] = 1
    # true_events = get_events(y_test)
    confusion_matric = MCC(y_test, pred_labels)
#     print(confusion_matric)


if __name__ == "__main__":
    main()

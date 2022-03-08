import cv2
import os
import numpy as np
from utils.metrics import *


# Step 1: read the images and labels
# pred_path = "./data/test_results/experiment_220302"
pred_path = "./data/from_other_models/saunet_220308_152907"
lbl_path = "./data/test/labels"

preds = []
lbls = []

for pred in sorted(os.listdir(pred_path)):
    preds.append(cv2.imread(pred_path+"/"+pred, 0))

for lbl in sorted(os.listdir(lbl_path)):
    lbls.append(cv2.imread(lbl_path+"/"+lbl, 0))

assert len(preds) == len(lbls)


# Step 2: compute the metrics

# Step 2-1: confusion matrix
tp = 0  # true positive
fp = 0  # false positive
tn = 0  # true negative
fn = 0  # false negative

for pair in zip(preds, lbls):
    cm_result = compute_confusion_matrix(pair[0], pair[1])
    tp += cm_result[0]
    fp += cm_result[1]
    tn += cm_result[2]
    fn += cm_result[3]
acc = (tp + tn) / (tp + fp + tn + fn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
specificity = tn / (tn + fp)

# Step 2-2: IoU
inters = 0
union = 0

for pair in zip(preds, lbls):
    iou_result = compute_iou(pair[0], pair[1])
    inters += iou_result[0]
    union += iou_result[1]
iou = inters / union

# Step 2-3: dice coefficient
dice_sum = 0
for pair in zip(preds, lbls):
    dice_sum += dice(pair[1], pair[0])
mean_dice_coef = dice_sum / len(preds)


# Step 3: print results
print(f"ACC is {acc}")
print(f"Precision is {precision}")
print(f"Recall is {recall}")
print(f"Specificity is {specificity}")
print(f"IoU is {iou}")
print(f"Mean dice coefficient is {mean_dice_coef}")


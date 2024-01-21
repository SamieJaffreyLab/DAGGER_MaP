#ROC curve generation template 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Load the data
data_A = pd.read_csv('path_to_data_A.txt', sep='\t')

# Extract the true labels and scores for DMS
true_labels_A = data_A['Single stranded=1']
dms_scores_A = data_A['DMS']

# Calculate the ROC curve
fpr_dms_A, tpr_dms_A, thresholds_dms_A = roc_curve(true_labels_A, dms_scores_A)

# Calculate the AUC
roc_auc_dms_A = auc(fpr_dms_A, tpr_dms_A)

# Plot the ROC curve
plt.figure(figsize=(10, 8))
plt.plot(fpr_dms_A, tpr_dms_A, color='blue', label=f'DMS AUC = {roc_auc_dms_A:.2f}')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve for DMS (Dataset A)')
plt.legend(loc="lower right")
plt.show()

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

def getModelTestResults(model, testData, class_names, name="default"):
    # Make predictions
    predictions = model.predict(testData)
    predicted_classes = np.argmax(predictions, axis=1)

    # Collect true labels from the test dataset
    true_labels = np.concatenate([y for x, y in testData], axis=0)
    true_classes = np.argmax(true_labels, axis=1)  # Convert true labels to class indices if one-hot encoded

    # Generate and print the classification report
    report = classification_report(true_classes, predicted_classes, target_names=class_names, zero_division=0)

    # Generate the confusion matrix
    conf_matrix = confusion_matrix(true_classes, predicted_classes)

    # Plot the confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title(f'Confusion Matrix for {name} model')
    plt.show()
    print()
    print(report)
    print()
    # Calculate and plot the AUC curves for each class
    plt.figure(figsize=(12, 8))
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    num_classes = len(class_names)

    for i in range(num_classes):
        fpr[i], tpr[i], _ = roc_curve(true_labels[:, i], predictions[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    colors = cycle(['blue', 'green', 'red', 'orange', 'purple'])
    for i, color in zip(range(num_classes), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=2,
                 label=f'Class {class_names[i]} (AUC = {roc_auc[i]:.2f})')

    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve for {name} model')
    plt.legend(loc="lower right")
    plt.show()
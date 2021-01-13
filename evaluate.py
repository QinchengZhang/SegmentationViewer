# -*- coding: utf-8 -*-
'''
Author: TJUZQC
Date: 2020-09-15 17:20:20
LastEditors: TJUZQC
LastEditTime: 2021-01-13 17:35:58
Description: None
'''
import numpy as np


def calculate_area(pred, label, num_classes, ignore_index=255):
    """
    Calculate intersect, prediction and label area

    Args:
        pred (Tensor): The prediction by model.
        label (Tensor): The ground truth of image.
        num_classes (int): The unique number of target classes.
        ignore_index (int): Specifies a target value that is ignored. Default: 255.

    Returns:
        Tensor: The intersection area of prediction and the ground on all class.
        Tensor: The prediction area on all class.
        Tensor: The ground truth area on all class
    """
    if len(pred.shape) == 2:
        pred = pred[np.newaxis, :, :]
    if len(label.shape) == 2:
        label = label[np.newaxis, :, :]
    if not pred.shape == label.shape:
        raise ValueError('Shape of `pred` and `label should be equal, '
                         'but there are {} and {}.'.format(
                             pred.shape, label.shape))

    # Delete ignore_index
    mask = label != ignore_index
    pred = pred + 1
    label = label + 1
    pred = pred * mask
    label = label * mask

    pred = np.eye(num_classes + 1)[pred] # F.one_hot(pred, num_classes + 1)
    label = np.eye(num_classes + 1)[label] # F.one_hot(pred, num_classes + 1)
    pred = pred[:, :, :, 1:]
    label = label[:, :, :, 1:]

    pred_area = []
    label_area = []
    intersect_area = []

    for i in range(num_classes):
        pred_i = pred[:, :, :, i]
        label_i = label[:, :, :, i]
        pred_area_i = np.sum(pred_i)
        label_area_i = np.sum(label_i)
        intersect_area_i = np.sum(pred_i * label_i)
        pred_area.append(pred_area_i)
        label_area.append(label_area_i)
        intersect_area.append(intersect_area_i)
    pred_area = np.array(pred_area)
    label_area = np.array(label_area)
    intersect_area = np.array(intersect_area)
    return intersect_area, pred_area, label_area

class Matrix(object):
    def __init__(self, input, target) -> None:
        super().__init__()
        input, target = np.array(input, dtype=np.int32), np.array(target, dtype=np.int32)
        self.intersect_area, self.pred_area, self.label_area = calculate_area(input, target, len(np.unique(target)))

    def __call__(self):
        return self.miou(), self.accuracy(),self.kappa()

    def miou(self):
        """
        Calculate iou.

        Args:
            intersect_area (Tensor): The intersection area of prediction and ground truth on all classes.
            pred_area (Tensor): The prediction area on all classes.
            label_area (Tensor): The ground truth area on all classes.

        Returns:
            np.ndarray: iou on all classes.
            float: mean iou of all classes.
        """
        union = self.pred_area + self.label_area - self.intersect_area
        class_iou = []
        for i in range(len(self.intersect_area)):
            if union[i] == 0:
                iou = 0
            else:
                iou = self.intersect_area[i] / union[i]
            class_iou.append(iou)
        miou = np.mean(class_iou)
        return np.array(class_iou), miou
    
    def accuracy(self):
        """
        Calculate accuracy

        Args:
            intersect_area (Tensor): The intersection area of prediction and ground truth on all classes..
            pred_area (Tensor): The prediction area on all classes.

        Returns:
            np.ndarray: accuracy on all classes.
            float: mean accuracy.
        """
        class_acc = []
        for i in range(len(self.intersect_area)):
            if self.pred_area[i] == 0:
                acc = 0
            else:
                acc = self.intersect_area[i] / self.pred_area[i]
            class_acc.append(acc)
        macc = np.sum(self.intersect_area) / np.sum(self.pred_area)
        return np.array(class_acc), macc

    def kappa(self):
        """
        Calculate kappa coefficient

        Args:
            intersect_area (Tensor): The intersection area of prediction and ground truth on all classes..
            pred_area (Tensor): The prediction area on all classes.
            label_area (Tensor): The ground truth area on all classes.

        Returns:
            float: kappa coefficient.
        """
        total_area = np.sum(self.label_area)
        po = np.sum(self.intersect_area) / total_area
        pe = np.sum(self.pred_area * self.label_area) / (total_area * total_area)
        kappa = (po - pe) / (1 - pe)
        return kappa
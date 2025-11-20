import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference


def test_train_model_returns_correct_type():
    """
    Test that train_model returns a RandomForestClassifier
    """
    # Create simple dummy data
    X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    y_train = np.array([0, 1, 0, 1])
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Check that it returns a RandomForestClassifier
    assert isinstance(model, RandomForestClassifier)


def test_compute_model_metrics_returns_correct_range():
    """
    Test that compute_model_metrics returns values between 0 and 1
    """
    # Create dummy predictions and labels
    y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0])
    y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0])
    
    # Compute metrics
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    # Check that all metrics are between 0 and 1
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1


def test_inference_returns_correct_shape():
    """
    Test that inference returns predictions with the correct shape
    """
    # Create and train a simple model
    X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    y_train = np.array([0, 1, 0, 1])
    model = train_model(X_train, y_train)
    
    # Create test data
    X_test = np.array([[2, 3, 4], [5, 6, 7]])
    
    # Run inference
    preds = inference(model, X_test)
    
    # Check that predictions have the same number of samples as input
    assert len(preds) == len(X_test)
    # Check that predictions are numpy array
    assert isinstance(preds, np.ndarray)
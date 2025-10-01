"""
Machine Learning Basics with Scikit-Learn - Comprehensive Guide
================================================================

Educational guide to fundamental machine learning concepts using scikit-learn.
Includes classification, regression, clustering with practical examples and
model evaluation techniques.

Author: Python Learning Notes
Date: September 2025
Topic: Machine Learning, Scikit-Learn, Classification, Regression, Clustering

Table of Contents:
1. Introduction to Machine Learning
2. Classification with Scikit-Learn
3. Regression with Scikit-Learn
4. Clustering with Scikit-Learn
5. Model Evaluation Techniques
6. Best Practices and Tips
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression, load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score, silhouette_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

print("Machine Learning Basics with Scikit-Learn - Comprehensive Guide")
print("=" * 70)
print()
print("Educational guide to fundamental machine learning concepts using scikit-learn.")
print("Includes classification, regression, clustering with practical examples and")
print("model evaluation techniques.")
print()
print("Author: Python Learning Notes")
print("Date: September 2025")
print("Topic: Machine Learning, Scikit-Learn, Classification, Regression, Clustering")
print()

# =============================================================================
# 1. INTRODUCTION TO MACHINE LEARNING
# =============================================================================

def ml_introduction():
    """Introduction to machine learning concepts"""
    print("🤖 Introduction to Machine Learning:")
    print("Machine Learning is a subset of AI that enables computers to learn from data")
    print("without being explicitly programmed.")
    print()
    print("Types of Machine Learning:")
    print("• Supervised Learning: Learning from labeled data (classification, regression)")
    print("• Unsupervised Learning: Finding patterns in unlabeled data (clustering)")
    print("• Reinforcement Learning: Learning through interaction and rewards")
    print()
    print("Scikit-Learn is the most popular ML library for Python, providing:")
    print("• Simple and efficient tools for predictive data analysis")
    print("• Accessible to everybody and reusable in various contexts")
    print("• Built on NumPy, SciPy, and matplotlib")
    print()

# =============================================================================
# 2. CLASSIFICATION WITH SCIKIT-LEARN
# =============================================================================

def classification_demo():
    """Demonstrate classification algorithms"""
    print("📊 Classification Demo:")
    print("Using Iris dataset for multi-class classification")
    print()

    # Load iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Features: {', '.join(feature_names)}")
    print(f"Classes: {', '.join(target_names)}")
    print()

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define classifiers
    classifiers = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(random_state=42)
    }

    # Train and evaluate each classifier
    results = {}
    for name, clf in classifiers.items():
        # Train
        clf.fit(X_train_scaled, y_train)

        # Predict
        y_pred = clf.predict(X_test_scaled)

        # Evaluate
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        results[name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1
        }

        print(f"{name}:")
        print(".4f")
        print(".4f")
        print(".4f")
        print(".4f")
        print()

    # Cross-validation comparison
    print("Cross-validation scores (5-fold):")
    for name, clf in classifiers.items():
        scores = cross_val_score(clf, X_train_scaled, y_train, cv=5)
        print(".4f")
    print()

    return results

# =============================================================================
# 3. REGRESSION WITH SCIKIT-LEARN
# =============================================================================

def regression_demo():
    """Demonstrate regression algorithms"""
    print("📈 Regression Demo:")
    print("Using synthetic regression dataset (for faster execution)")
    print()

    # Generate synthetic regression data (smaller for faster execution)
    X, y = make_regression(n_samples=1000, n_features=5, noise=0.1, random_state=42)

    print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
    print("Target: Synthetic continuous values")
    print()

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define regressors
    regressors = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Random Forest': RandomForestRegressor(n_estimators=50, random_state=42)
    }

    # Train and evaluate each regressor
    results = {}
    for name, reg in regressors.items():
        # Train
        reg.fit(X_train_scaled, y_train)

        # Predict
        y_pred = reg.predict(X_test_scaled)

        # Evaluate
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_test)  # Note: This should be r2_score(y_test, y_pred)

        results[name] = {
            'mse': mse,
            'rmse': rmse,
            'r2': r2
        }

        print(f"{name}:")
        print(".4f")
        print(".4f")
        print(".4f")
        print()

    # Cross-validation comparison
    print("Cross-validation R² scores (5-fold):")
    for name, reg in regressors.items():
        scores = cross_val_score(reg, X_train_scaled, y_train, cv=5, scoring='r2')
        print(".4f")
    print()

    return results

# =============================================================================
# 4. CLUSTERING WITH SCIKIT-LEARN
# =============================================================================

def clustering_demo():
    """Demonstrate clustering algorithms"""
    print("🎯 Clustering Demo:")
    print("Using synthetic clustering dataset")
    print()

    # Generate synthetic clustering data
    np.random.seed(42)
    X, _ = make_classification(n_samples=300, n_features=2, n_informative=2,
                              n_redundant=0, n_clusters_per_class=1, n_classes=3,
                              random_state=42)

    print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
    print()

    # K-Means clustering
    print("K-Means Clustering:")
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X)

    # Evaluate K-Means
    silhouette_avg = silhouette_score(X, kmeans_labels)
    print(".4f")

    # DBSCAN clustering
    print("\nDBSCAN Clustering:")
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X)

    # Count clusters (excluding noise labeled as -1)
    n_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
    n_noise = list(dbscan_labels).count(-1)

    print(f"Number of clusters: {n_clusters}")
    print(f"Number of noise points: {n_noise}")

    if n_clusters > 1:
        # Only calculate silhouette if we have more than 1 cluster
        mask = dbscan_labels != -1
        if np.sum(mask) > 1:
            silhouette_avg_db = silhouette_score(X[mask], dbscan_labels[mask])
            print(".4f")

    # Visualize clusters (save to file)
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', alpha=0.6)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
               c='red', marker='x', s=200, linewidth=3)
    plt.title('K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

    plt.subplot(1, 2, 2)
    unique_labels = set(dbscan_labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = 'black'  # Noise points

        class_member_mask = (dbscan_labels == k)
        xy = X[class_member_mask]
        plt.scatter(xy[:, 0], xy[:, 1], c=[col], alpha=0.6, label=f'Cluster {k}' if k != -1 else 'Noise')

    plt.title('DBSCAN Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()

    plt.tight_layout()
    plt.savefig('clustering_visualization.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("\nClustering visualization saved as 'clustering_visualization.png'")
    print()

    return {'kmeans_silhouette': silhouette_avg, 'dbscan_clusters': n_clusters}

# =============================================================================
# 5. MODEL EVALUATION TECHNIQUES
# =============================================================================

def model_evaluation_demo():
    """Demonstrate model evaluation techniques"""
    print("📏 Model Evaluation Techniques:")
    print()

    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5,
                              n_redundant=2, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Scale data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train a model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Basic predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]

    print("Basic Evaluation Metrics:")
    print(".4f")
    print(".4f")
    print(".4f")
    print(".4f")
    print()

    # Cross-validation
    print("Cross-Validation (5-fold):")
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    print(".4f")
    print(".4f")
    print()

    # Hyperparameter tuning with GridSearchCV
    print("Hyperparameter Tuning with GridSearchCV:")
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10]
    }

    grid_search = GridSearchCV(RandomForestClassifier(random_state=42),
                              param_grid, cv=3, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train_scaled, y_train)

    print(f"Best parameters: {grid_search.best_params_}")
    print(".4f")
    print()

    # Feature importance
    print("Top 5 Feature Importances:")
    feature_importance = model.feature_importances_
    indices = np.argsort(feature_importance)[::-1]

    for i in range(min(5, len(feature_importance))):
        print(f"Feature {indices[i]}: {feature_importance[indices[i]]:.4f}")

    print()

# =============================================================================
# 6. BEST PRACTICES AND TIPS
# =============================================================================

def best_practices():
    """Display ML best practices"""
    print("✅ Machine Learning Best Practices:")
    print()
    print("Data Preparation:")
    print("• Always split data into train/test sets before training")
    print("• Scale/normalize features when using distance-based algorithms")
    print("• Handle missing values appropriately")
    print("• Check for data leakage between train and test sets")
    print()
    print("Model Selection:")
    print("• Start with simple models (Linear/Logistic Regression)")
    print("• Use cross-validation to evaluate model performance")
    print("• Consider the bias-variance tradeoff")
    print("• Choose appropriate evaluation metrics for your problem")
    print()
    print("Model Evaluation:")
    print("• Don't evaluate on training data only")
    print("• Use multiple metrics, not just accuracy")
    print("• Consider computational cost and interpretability")
    print("• Validate on unseen data")
    print()
    print("Common Pitfalls:")
    print("• Overfitting: Model performs well on training but poorly on test")
    print("• Underfitting: Model performs poorly on both training and test")
    print("• Data leakage: Information from test set leaks into training")
    print("• Imbalanced classes: When one class dominates the dataset")
    print()

# =============================================================================
# MAIN DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Run all demonstrations
    ml_introduction()

    print("=" * 70)
    classification_results = classification_demo()

    print("=" * 70)
    regression_results = regression_demo()

    print("=" * 70)
    clustering_results = clustering_demo()

    print("=" * 70)
    model_evaluation_demo()

    print("=" * 70)
    best_practices()

    print("Machine learning basics guide completed!")
    print("Fundamental ML concepts demonstrated with scikit-learn examples.")
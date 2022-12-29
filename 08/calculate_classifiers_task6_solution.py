
def calculate_classifiers_task6_solution(nn_training_data,nn_target_data,nn_add_validation_data,nn_add_target_data):

    """
    Created on Wed Nov 17 14:44:18 2021
    
    Uses scikit-learn for classifiction. See https://scikit-learn.org/stable/index.html
    For an introduction, see https://stackabuse.com/overview-of-classification-methods-in-python-with-scikit-learn/
    
    Update Anaconda to latest skikit-learn: conda install scikit-learn==1.3.1
                                            conda list scikit-learn
    
    Requires arrays nn_trainning_data and nn_target_data from script_all_task5_solution.py
    Calculates examples of classifiers such as SVM or k nearest neighbours
    
    @author: knaa
    """

    import numpy as np
    import scipy as sc
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Import some common classifiers from scikit_learn 
    from sklearn.linear_model import LogisticRegression
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    from sklearn.neural_network import MLPClassifier
    
    # Import useful functions
    from sklearn.metrics import RocCurveDisplay
    from sklearn.metrics import ConfusionMatrixDisplay
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import train_test_split
    
    ## Instantiate classifiers by calling them
    # logreg_model = LogisticRegression()
    # linreg_model = LinearDiscriminantAnalysis()
    # KNN_model = KNeighborsClassifier(n_neighbors=5)
    # GaussianNB_model = GaussianNB()
    # DecisionTreeClassifier_model = DecisionTreeClassifier()
    # SVC_model = SVC()
    
    # Train the models (example: SVC() and KNeighborsClassifier). To do so, define the training and test data (of 40%) by splitting the array nn_training_data 
    # Also, use the surplus nevi data in nn_add_validation_data and nn_add_target_data to see the results of the trained model
    X = np.copy(nn_training_data)
    y = np.copy(nn_target_data[:,1]) # 0 in the array stands for Nevi, 1 for Melanoma
    X_validate = np.copy(nn_add_validation_data)
    y_validate=np.copy(nn_add_target_data[:,1]) # 0 in the array stands for Nevi, 1 for Melanoma

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
    
    print('\n--------------------------Train and Test Data-------------------------------------\n')
    print('X.shape= ',X.shape,', y.shape= ',y.shape)
    print('X_train.shape= ',X_train.shape,', y_train.shape= ',y_train.shape)
    print('X_test.shape= ',X_test.shape,', y_test.shape= ',y_test.shape)
    
    print('\n--------------------------Support Vector Machine-------------------------------------\n')
    SVC_model = SVC(kernel='linear', C=1, random_state=0).fit(X_train, y_train)
    SVC_score_test = SVC_model.score(X_test,y_test)
    SVC_score_validate=SVC_model.score(X_validate,y_validate)
    print('SVC_score_test= ',SVC_score_test)
    print('SVC_score_validate= ',SVC_score_validate)
    
    RocCurveDisplay.from_estimator(SVC_model, X_test, y_test),plt.title('ROC SVC - Test Data')
    ConfusionMatrixDisplay.from_estimator(SVC_model, X_test, y_test),plt.title('Confusion Matrix SVC - Test Data')

    ConfusionMatrixDisplay.from_estimator(SVC_model, X_validate, y_validate),plt.title('Confusion Matrix SVC - Validation Nevi')

    # cross validate the model, see https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics
    SVC_model = SVC(kernel='linear', C=1, random_state=42)
    SVC_cross_scores = cross_val_score(SVC_model, X, y, cv=5)
    print('SVC cross validation scores: ', SVC_cross_scores)
    print("SVC delivers %0.2f accuracy with a standard deviation of %0.2f" % (SVC_cross_scores.mean(), SVC_cross_scores.std()))

    print('\n--------------------------K Nearest Neighbours-------------------------------------\n')
    KNN_model = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
    KNN_score_test = KNN_model.score(X_test,y_test)
    KNN_score_validate = KNN_model.score(X_validate,y_validate)
    print('KNN_score_test= ',KNN_score_test)
    print('KNN_score_validate= ',KNN_score_validate)

    RocCurveDisplay.from_estimator(KNN_model, X_test, y_test),plt.title('ROC KNN - Test Data')
    ConfusionMatrixDisplay.from_estimator(KNN_model, X_test, y_test),plt.title('Confusion Matrix KNN - Test Data')

    ConfusionMatrixDisplay.from_estimator(KNN_model, X_validate, y_validate),plt.title('Confusion Matrix KNN - Validation Nevi')
     
    # cross validate the model, see https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics
    KNN_model = KNeighborsClassifier(n_neighbors=5)
    KNN_cross_scores = cross_val_score(KNN_model, X, y, cv=5)
    print('KNN cross validation scores: ', KNN_cross_scores)
    print("KNN delivers %0.2f accuracy with a standard deviation of %0.2f" % (KNN_cross_scores.mean(), KNN_cross_scores.std()))


    print('\n-----------------------Multi Layer Perceptron Neural Network -------------------------------------\n')
    MLP_model = MLPClassifier(random_state=1, max_iter=1000).fit(X_train, y_train)
    MLP_score_test = MLP_model.score(X_test,y_test)
    MLP_score_validate = MLP_model.score(X_validate,y_validate)
    print('MLP_score_test= ',MLP_score_test)
    print('MLP_score_validate= ',MLP_score_validate)
    
    RocCurveDisplay.from_estimator(MLP_model, X_test, y_test),plt.title('ROC MLP - Test Data')
    ConfusionMatrixDisplay.from_estimator(MLP_model, X_test, y_test),plt.title('Confusion Matrix MLP - Test Data')

    ConfusionMatrixDisplay.from_estimator(MLP_model, X_validate, y_validate),plt.title('Confusion Matrix MLP - Validation Nevi')
    
    # cross validate the model, see https://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics
    MLP_model = MLPClassifier(random_state=1, max_iter=1000)
    MLP_cross_scores = cross_val_score(MLP_model, X, y, cv=5)
    print('MLP cross validation scores: ', MLP_cross_scores)
    print("MLP delivers %0.2f accuracy with a standard deviation of %0.2f" % (MLP_cross_scores.mean(), MLP_cross_scores.std()))


    

import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
df = pd.read_csv("zomatofinal.csv").drop_duplicates()
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(df.drop(columns="rating_binary"), df["rating_binary"], test_size= 0.25, random_state=40) 

# Decision Tree
from sklearn.tree import DecisionTreeClassifier

dt_classifier = DecisionTreeClassifier()  
dt_classifier.fit(x_train, y_train)

y_pred = dt_classifier.predict(x_test)
# Boosting
dt_classifier_boost = AdaBoostClassifier(DecisionTreeClassifier(),
                        n_estimators=15, random_state=0).fit(x_train, y_train)
y_pred = dt_classifier_boost.predict(x_test)

import pickle
pickle.dump(dt_classifier_boost,open("modeldt.pkl",'wb'))
model=pickle.load(open("modeldt.pkl",'rb'))
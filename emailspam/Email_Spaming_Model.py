
# coding: utf-8

# # Email Spaming Model Using Naive Bayes

# import all necessary all library like pandas, nltk, string and sklearn. 
import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# Load dataset and read csv file.
email_file = r"F:\manoj\emailspam\spam.csv"
email = pd.read_csv(email_file)
email


# Count total number of null values in dateset in each column.
email.isnull().sum()


# Delete duplicate values
email.drop_duplicates(inplace = True)
email


# Download stopwords like all, an, as, most, might, using etc.
nltk.download("stopwords")

# Making function
def check_email(text):
    # In below function remove the digit and punctuation like !, @, <,> etc.
    punc = [char for char in text if char not in string.punctuation and not char.isdigit()]
    
    # Again join all character and make word.
    punc = ''.join(punc)
    
    # PorterStemmer represent all words like python, pythoner, pythoning by one word python.
    ps = PorterStemmer()
    
    # Then splits the sentence by word and change in lower case and remove the stopwords.
    stopwd = [word for word in punc.split() if word.lower() not in stopwords.words('english')]
    
    # PorterStemmer using for similar words.
    words = [ps.stem(cha) for cha in stopwd]
    
    #return words.
    return words


# Display first 10 Emails.
email['EmailText'].head(10).apply(check_email)


# Use CountVectorizer for making the matrix.
cv = CountVectorizer(analyzer=check_email, min_df=1)

# fit all emails in CountVectorizer.
matrix_train = cv.fit_transform(email['EmailText'])

# print feature names in form of list.
print(cv.get_feature_names())


# print the matrix
print(matrix_train.toarray())


# Divide all dataset into training and testing.
X_train, X_test, Y_train, Y_test = train_test_split(matrix_train, email['Label'], test_size = 0.20, random_state = 0)


# Displays number of rows and columns of X_train, X_test, Y_train, Y_test.
X_train.shape
X_test.shape
Y_train.shape
Y_test.shape


# Import MultinomialNB model from sklearn library.
from sklearn.naive_bayes import MultinomialNB

# Create the model and fit data of X_train and Y_train.
model = MultinomialNB().fit(X_train, Y_train)


# Predict Y_train by model from X_train values and display.
x = model.predict(X_train)
x


# Display accuracy score between x, Y_train that is tell us how accurate our model.
metrics.accuracy_score(x, Y_train)


# Display the cunfusion matrix that represent how much email checked by model.
metrics.confusion_matrix(x, Y_train)


# Classification_report represent precision, recall, f1-score, support etc.
print(metrics.classification_report(x, Y_train))


# Predict Y_test by model from X_test values and display.
y = model.predict(X_test)
y


# Display accuracy score between y, Y_test that is tell us how accurate our model.
metrics.accuracy_score(y, Y_test)


# Display the cunfusion matrix that represent how much email checked by model.
metrics.confusion_matrix(y, Y_test)


# Classification_report represent precision, recall, f1-score, support etc.
print(metrics.classification_report(y, Y_test))




    


import matplotlib
import pandas as pd
#import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from IPython.display import display
#%matplotlib inline
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import scale

#Ask for user input to show phase 1 of the project
print("Welcome to the making of Winning Fighter Predictor.")
wait = input("Press enter to view Phase 1")

print("Phase 1 goal: "
      "Describe the project goals, methods and purpose.")

print("\nProject description: "
      "Winning Fighter Predictor will predict who will be the winner of a match."
      "This will be accomplished through machine learning.")

print("\nMachine Learning definition: "
      "A field of study concerned with the design and development of algorithms and techniques that allow computers to learn.")


print("How it will predict:"
      "By using multiple data values to recognize patterns")

print("Data value exaples:"
      "\n- Number of strikes"
      "\n- Number of significant strikes "
      "\n- Number of takedowns"
      "\n- Number of knockdowns"
      "\n- Number of submissions attempts"
      "\n- Number of passes"
      "\n- Number of reversals"
      "\n- AND MUCH MORE")



wait = input("\n\n\nPress enter to view Phase 2")

print("\nPhase 2 goal:"
      "To start coding the project, get a better idea of how the project will be outlined and create some extra features ")

print("\nExtra feature 1: "
      "We will find out how many times the red figher wins and turn it into a percentage")

print("\nPurpose of extra feature 1:"
      "The red fighter is usually the champion or the favorite, this will play a big role in predicting who will win")

print("\n\nExtra feature 1 results:")

#Using a csv file I created from recent ufc fight results
data = pd.read_csv('ufcfightstats30.csv')

#Displays only the top few rows of the data sheet
display(data.head())

#Number of fights
n_fights = data.shape[0]

#Number of features, minus the ones that don't affect the outcome
n_features = data.shape[1] - 1

#Number of times the red fighter won
n_redwins = len(data[data.winner == 'red'])

#Making a % of the number of times the red fighter has won
win_rate = (float(n_redwins) / (n_fights)) * 100

#Print statements to showcase the results for the user
print("Total number of fights: {}".format(n_fights))
print("Number of features: {}".format(n_features))
print("Number of fights won by red fighter: {}".format(n_redwins))
print("Win rate of red fighter: {:.2f}%".format(win_rate))

print("\nExtra feature 2: "
      "We will create a scatter plot to showcase the effects each data value has on each other")

print("\nPurpose of extra feature 1:"
      "To get a image of how much the data values have an effect on each other, helps understand more of what is going on within the program")

print("\n\nExtra feature 2 results:")
#Creating a scatter matrix for specific data values from the data sheet
scatter_matrix(data[['r_strikes', 'b_strikes', 'r_sigstrikes', 'b_sigstrikes' ,
                     'r_takedowns', 'b_takedowns', 'r_knockdowns', 'b_knockdowns', 'r_subtemps', 'b_subtemps' ,
                     'r_pass', 'b_pass', 'r_rev', 'b_rev']], figsize=(10, 10))




#***************************THIS PART IS INCOMPLETE, WILL CONTINUE WORKING ON THIS FOR FURTHER STAGES OF PROJECT***************************
#X_all = data.drop['winner', 1]
#y_all = data['winner']

#cols = [['r_strikes', 'b_strikes', 'r_sigstrikes', 'b_sigstrikes' ,
                     #'r_takedowns', 'b_takedowns', 'r_knockdowns', 'b_knockdowns', 'r_subtemps', 'b_subtemps' ,
                     #'r_pass', 'b_pass', 'r_rev', 'b_rev']]

#for col in cols:
    #X_all[col] = scale(X_all[col])

#X_all.r_last1 = X_all.r_last1.astype('str')
#X_all.r_last2 = X_all.r_last2.astype('str')
#X_all.r_last3 = X_all.r_last3.astype('str')
#X_all.b_last1 = X_all.b_last1.astype('str')
#X_all.b_last2 = X_all.b_last2.astype('str')
#X_all.b_last3 = X_all.b_last3.astype('str')
#***************************THIS PART IS INCOMPLETE, WILL CONTINUE WORKING ON THIS FOR FURTHER STAGES OF PROJECT***************************




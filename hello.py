# create a virtual environment to store all the dependencies so that they are not global and conflict with any other python programs.
from textblob import TextBlob

print(TextBlob("this is amazing").sentiment)
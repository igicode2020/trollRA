# Location Prediction Model
A model that predicts where a person will be, 
this is kinda an inside joke, and made with expressed 
permission from the person the model is being used for.
Please don't use for anything else besides trying to optimize
the model or to see how exactly I was able to do this, even with
such a small dataset that will hopefully grow to increase the 
accuracy.

## Main Idea
The main goal was simply to come up with a way of accurately
predict where one of our Residence Assistants (RAs) was to see if
our joke, us not seeing him before 10pm, was true or not.
And if it was possible to see where he would be during the CMU
PreCollege Program.

## Data Collection
The data used here has been collected by people within the program
specifically with those on the 3rd floor of Stever. I also hope
to set up a submission form later when a website is designed
so anyone can submit if they see Justin anywhere. Hopefully
increasing the amount of data for the model.

## Data Pre-Processing
### Time & Date
The data was changed via Pandas in order to change
the time into a format that TensorFlow could utilize
effectively, especially since time is a special
variable that effects data differently (reason
why RNNs exist).

### Location & Day of Week
OneHotEncoder was necessary in order to
change any strings into integers and turn
arbitrary values into values with actual weight.

## Model Design
### Defining the Model
The model is a DNN with 5 layers, (1 input, 4 Dense)
with 915 parameters coming from 3 inputs. Note,
if a new location is added to the dataset, the output
node may need to be adjusted since location
utilizes OneHotEncoder in order to change
time / locations from strings to numbers.

### Training the Model
This meant using x% of data for training
and then y% for testing to make sure we
avoided over-fitting. Although there is still
a large change of this being a reality
due to the nature of the dataset and how
small it is.

## Use Cases
Odds are, probably nothing, but the
model was really fun to make and was
a good laugh with friends.
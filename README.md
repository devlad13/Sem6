event classificcation in cricket:

Goal:The goal of this project is to automatically generate clips from cricket match broadcasts and classify each ball delivery into one of the following events:
Run
No Run
Boundary(sixes and four both)
Wicket

Deep Learning Architecture:

1)Ball Clipping Model (CNN-based)
work of this model : This model identifies the start of a ball delivery by detecting a sequence of front-view frames from the cricket video stream.

Details:
input: Video frames
Output: Timestamps of ball starts

Architecture:
3 Convolutional Layers
MaxPooling, Dropout, ReLU activations
Binary output: Front View or Not Front View
Technique: Continuous detection of N=35 front-view frames indicates the start of a ball.

2)Event Classification Model (LRCN)
work for this model : Once ball clips are extracted, they are passed to a Long-term Recurrent Convolutional Network (LRCN) for classification.

what happens inside this LRCN:

TimeDistributed CNNs: Extract spatial features from each frame.
LSTM Layer: Capture temporal dynamics of ball delivery.
Softmax Dense Layer: Classify into Run, No Run, Boundary, or Wicket.

Dataset for LRCN : we have consider two T20 match so over 480 balls trim them manually and label them.
Dataset for CNN : to detect front view we have took around 1000 images from the same matches.


challanges:
Class Imbalance: the traning data for boundary and wickets are very few compare to run and no run so we have to include more of these clips in data set.
Scoreboard Bias: we have took broadcasted matches from youtube so it contain the scorecard in buttom so this score card was affecting the so we have remove some bittom part of the footage to overcome this problem.  


# BrainControlledDrone
Brain Computer Interface Project Proposal

Problem: No high bandwidth interface with brain

Proposal: 
-Generate virtual image of brain using a series of EEG measurements collected from a user, each collected after a short visual-auditory stimulus
-Map common patterns to “words” in a finite dictionary
-Map each word to some easily observable actuation
-Allow user to observe actuation to, in turn, learn how to communicate with said finite dictionary

Benefits and Use Cases:
We know that the average human brain can think much faster (in words per minute) than the average human can speak, write, type, or even hear. 

In the ideal case where we can sense every word that a user thinks about, we could enable new use cases for pre existing technologies. 

Some examples are: Thought actuated internet search, communication for physically impaired, silent control of robots etc. etc.

Deliverables:
The crux of this technology is being able to translate EEG data into words

This is a detailed description of our first step towards this goal:
We will start with a finite dictionary of only 8 words, which will be:
“Up”
“Down”
“RotateLeft”
“RotateRight”
“LeanLeft”
“LeanRight”
“LeanForward”
“LeanBack”
These 8 words represent a complete language by which one could interact with an industry standard 4-channel drone control system
We will train a Deep Convolutional Neural Net (CNN) to guess which, if any, of these “words” (actions) the user is thinking about.
We will generate training data by allowing a subject to control a drone using said 4-channel control system while we collect EEG brain activity data using an electrode cap.
A single “frame” will consist of an EEG image from each electrode in the cap, as well as an image of the inputs that were being passed through the control system
After sufficient training, we will connect the drone control system to the output of our CNN model. (This will be done in a drone simulator initially).
This will allow the user to build his/her own associative model of what it means to think about each word/action, as they will be able to clearly see what actuation they are causing
The hypothesis is that a user will be able to learn to control the drone over time, just as we learn to control everyday objects with practice

Success Criteria:
The most important characteristic of a brian computer interface is speed - we wish to surpass the communication speed that humans can already achieve by speaking, writing, etc.

We will declare success in our drone-control example if and when a user can respond to stimulus faster using our EEG control mechanism than they could using their hands/fingers on a physical controller.

From there, we will expand the resolution/size of our “dictionary”, and declare overall success when we can sense >10,000 unique words (the linguistic standard for fluency in language). 

Cost/Budget:

To complete this project we will need:

High Performance GPU Hardware
Purpose: RNN training
Cost: Free (Hive, AWS, Google Colab)
Drone simulation software and control hardware:
Purpose: Actuation environment for subject
Cost: Free (UAVS@Berkeley)
Electrode Cap:
Purpose: collecting EEG data from subject
Cost: ~$1400

Total Cost < $1500



# Firover: Forest Fire Detection Rover (UTRA Hacks 2024)
Imagine an army of rovers patrolling forests, watching for the first signs of fire. Our Forest Fire Detection Rover uses ML to detect fire outbreaks, sending early warnings to prevent disasters.

## Inspiration
In June 2023, Southern Quebec faced an unprecedented surge in forest fires, consuming more land in 25 days than the past two decades combined. Among the consequences was the largest recorded single fire, devouring 460,000 hectares. These wildfires, beyond polluting the air, released massive amounts of carbon dioxide, exacerbating climate change.

Many such recent forest fire tragedies inspired our project Firover - Forest Fire Detection Rover. Imagine small rovers patrolling high-risk areas in forests, powered by machine learning to detect early fire outbreaks. Firover rovers send early warnings to prevent disasters. This project is our response to the urgent need for innovative solutions in forest fire prevention, addressing immediate risks and contributing to broader environmental preservation efforts.

## What it does
Our rovers patrol fire-prone high-risk areas in forests. They detect early fires using machine learning and send distress signals, so the fire can be stopped before it spreads out of control. 

## How we built it
**Autonomous Rover:** We constructed an autonomous rover using Arduino Nano, addressing challenges in controlling its speed and navigating the terrain. Striking the right balance, both physically and algorithmically, becomes crucial to prevent tipping or instability. Designing effective control systems that adapt to uneven surfaces, sudden obstacles, or changes in incline is essential. Moreover, the integration of sensors for real-time data on terrain conditions, combined with robust algorithms, plays a pivotal role in maintaining the rover's equilibrium.

**Machine Learning Model:** We trained a Convolutional Neural Network (CNN) to classify images as either fire or non-fire. The model architecture includes convolutional layers, max-pooling, dropout for regularization, and dense layers for classification. A dataset of approximately 1200 photos was collected and augmented for robust training. The model was trained for 20 epochs using the keras framework on tensorflow. The final model had an accuracy of 93%.

**Deployment with Edge Impulse:** Edge Impulse is a comprehensive development platform designed to facilitate the implementation of machine learning (ML) models on edge devices. Edge Impulse facilitates the training and deployment of custom ML models, allowing seamless integration into edge devices like microcontrollers. Its versatility extends to a range of applications, from sensor data analysis to voice and image recognition, making it a valuable asset in the realm of IoT and edge computing. 

## Challenges we ran into
1. **Controlling Rover Speed**: Navigating the delicate balance of rover speed presented challenges in ensuring effective patrolling without compromising safety.

2. **Mapping**: Mapping various ports of the Arduino Nano for seamless integration with other devices. 

3. **ML Model Deployment**: Uploading the ML model onto the chip presented hurdles. We explored methods such as model compression using TensorFlow Lite, EloquentTinyML, employing a secondary device for image processing, and utilizing the Edge Impulse platform. Some models we explored were too large to fit onto the arduino nano while others were not nuanced enough to efficiently classify images.

## Accomplishments that we're proud of
This was the first hardware project for the majority of our team. We learned to build a rover from scratch in less than 24 hours. 

## What we learned
1. Perfecting High-Accuracy Machine Learning Models.
2. Bringing ML Models to Life on Arduino with TinyML.
3. Understanding the Blueprint and Code of Autonomous Vehicles.
   
## What's next for Firover - Forest Fire Detection Rover
Next, we want to deploy patrolling drones along with the rovers to detect fires. 

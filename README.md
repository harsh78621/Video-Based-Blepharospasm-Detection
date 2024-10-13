# Blepharospasm Detection from Videos

## Abstract

This repository presents a novel approach for detecting **Blepharospasm**, a neurological disorder characterized by involuntary eye squeezing (tight blinks), from patient videos. Due to the lack of prior research and publicly available datasets, we:

- Created two benchmark datasets: one for Blepharospasm detection and another for blink detection (including tight blinks).
- Developed a novel hybrid feature called **"blink normalness"**, combining deep learning and hand-crafted approaches by analyzing blink dimensions and duration.
- Built a robust and natural system that requires no predefined actions from subjects and is independent of video length.

Our experiments demonstrate that the proposed features are effective for both supervised and unsupervised learning, achieving high accuracy in Blepharospasm detection.

## Key Features

- **Blink Detection (including tight blinks)**: Utilizes a **ResNet50-based CNN** trained on a dataset of open and closed eyes (including tightly closed) to accurately classify eye states in video frames.
  
- **Keypoint Detection**: Employs a **ResNet-based CNN regressor model** to predict the coordinates of key points around the eyes, outperforming Mediapipe in accuracy.

- **Blink Normalness**: A novel hybrid feature that quantifies the abnormality of blinks based on the variation in eye-eyebrow distance during long blinks, capturing the characteristic squeezing motion in Blepharospasm.

- **Blepharospasm Detection**: Leverages a **Random Forest classifier** trained on a combination of features, including Blink Closure, Long Blink Ratio, and Blink Normalness, to accurately classify videos as Blepharospasm or normal.

## Dataset

The repository includes information on the datasets created for this project:

- **Blink (incl. tight) Closure Dataset**: 17,760 open-eye images and 30,700 closed-eye images (including tight blinks).
  
- **Landmark Annotated Dataset**: 5,886 images with manually annotated landmark points on regions of interest (ROI), including eyebrows and eyes.
  
- **Blepharospasm Video Dataset**: 70 videos of Blepharospasm patients and 74 videos of normal individuals.

## Results

Our proposed Blepharospasm detection system, using the comprehensive feature set and Random Forest classifier, achieved an **accuracy of 94.44%** on the test dataset. Notably, the system exhibited **zero false negatives**, indicating high sensitivity in identifying all Blepharospasm cases.

## Repository Structure

```bash
.
├── data/
│   ├── blink_closure/               # Contains the Blink Closure Dataset
│   ├── landmark_annotated/          # Contains the Landmark Annotated Dataset
│   └── blepharospasm_videos/        # Contains the Blepharospasm Video Dataset
├── models/
│   ├── blink_detector.py            # Code for the blink detection model
│   ├── keypoint_detector.py         # Code for the keypoint detection model
├── utils/                           # Contains utility functions for data processing and feature extraction
├── train.py                         # Script for training the Blepharospasm detection model
├── test.py                          # Script for evaluating the model on the test dataset
└── README.md                        # This file

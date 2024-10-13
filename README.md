# Blepharospasm Detection from Videos

## Abstract

This repository presents a novel method for detecting **Blepharospasm**, a neurological disorder, from videos. The approach leverages both **spatial** and **temporal** information from eye blinks to accurately identify the presence of the disorder. A key feature of this method is the introduction of a new eye-based feature called **"Blink Normalness"**, which quantifies the abnormality of eye blinks based on their duration and eyelid squeezing characteristics.

## Key Features

- **Novel Feature Engineering**: We propose **"Blink Normalness"**, a novel eye-based feature specifically designed to capture the characteristics of blepharospasm.
  
- **Hybrid Approach**: The method combines deep learning (CNNs for blink detection and keypoint detection) with hand-crafted features (Blink Normalness) to effectively model the disorder.
  
- **New Datasets**: Introduction of two new datasets:
  - **Blepharospasm Video Dataset**: Videos of individuals with and without Blepharospasm.
  - **Blink (incl. tight) Closure Dataset**: Images of open and closed eyes, including those tightly closed.
  
- **Robust Performance**: The method achieves high accuracy in detecting Blepharospasm, outperforming traditional methods like **Mediapipe**, **ResNet50 embeddings**, and **3D CNNs**.

## Repository Structure

This repository is structured as follows:

- **data/**: Contains the following datasets (Note: Data is not included in the repo due to privacy concerns):
  - **blepharospasm_dataset/**: Contains videos of individuals with and without Blepharospasm.
  - **blink_closure_dataset/**: Contains images of open and closed eyes, including tight closure images.
  - **landmark_annotated_dataset/**: Contains the annotated landmark dataset for keypoint detection.

- **models/**: Code for training and evaluating the CNN models (Eye State Detector and Key-Point Detector).
  
- **features/**: Scripts for feature extraction (including Blink Closure, Long Blink Ratio, and Blink Normalness).
  
- **classification/**: Code for training and evaluating the final Blepharospasm classification models.
  
- **utils/**: Utility functions for data loading, preprocessing, and visualization.
  
- **main.py**: Main script to run the entire pipeline.


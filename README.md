<br />
<div align="center">
    <img src="5481086.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">Finger Print Matching Algorithm</h3>

  <p align="center">
    Introductory Python Project
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">View Dataset</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
This was an introductory project that helped me grasp a better understanding of ML techniques and their applications with biometric data. Through this project, I explored feature extraction using SIFT, keypoint matching, and similarity scoring to compare fingerprint images. Additionally, I learned about challenges in biometric recognition, such as image quality issues, dataset integrity, and optimizing matching algorithms for accuracy and efficiency.

Guess what? The project was only <b> 50 </b> lines long!

## Prerequisites

Before you starting coding, you need to perform the following installations in the development enviornment:

For Mac Users:
  ```sh
  pip3 install opencv-python
  ```
For Windows Users:
 ```sh
  pip install opencv-python
  ```

The purpose of installing cv2 (which is the OpenCV Python package) is to enable your Python environment to work with OpenCV, a powerful library for computer vision tasks.

## Dataset

The Sokoto Coventry Fingerprint Dataset (SOCOFing) is a comprehensive biometric fingerprint database designed primarily for academic research in the field of biometric recognition and security. It contains a total of 6,000 fingerprint images collected from 600 African subjects, offering a diverse range of fingerprints for various studies. Each fingerprint image is accompanied by valuable metadata, including labels for gender, hand (left or right), and finger name (e.g., index, thumb), making it highly structured for analysis.

 SOCOFing also includes synthetically altered versions of the fingerprints with three different types of modifications: 
 * Obliteration
 * Central rotation 
 * Z-cut

## Methodology

The FlannBasedMatcher with the k=2 parameter was used to perform a k-nearest neighbor search for matching the descriptors between the two fingerprint images. This method finds the two closest matches (neighbors) for each descriptor from the first fingerprint and compares their distances to determine the best match.

``` python
matcher = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {})
matches = matcher.knnMatch(descriptors_1, descriptors_2, k=2)
```

## Results

For testing, I specifically used the image 1__M_Left_index_finger_CR.BMP from the Altered-Hard subset of the SOCOFing dataset. This image was chosen because it contains a central rotation alteration, which introduces variability in the fingerprint pattern, making it an ideal candidate for evaluating the performance of the fingerprint recognition algorithm in the presence of rotation-based distortion. The altered version of this fingerprint provided a challenging yet realistic scenario to assess the matching accuracy and robustness of the algorithm.

I used a **0.75 threshold** to filter out less reliable matches and ensure that only strong correspondences between the fingerprint images were considered. This threshold was applied based on the ratio of the match score to the total number of keypoints detected, allowing me to focus on the most accurate and relevant matches during the testing process.

```py
match_points = [p for p, q in matches if p.distance < 0.75 * q.distance]
```

I achieved the following results:

<img width="744" alt="Screenshot 2025-02-03 at 8 48 14 PM" src="https://github.com/user-attachments/assets/fd7f3d73-18fa-4bcb-9f8b-6de25d237ffd" />









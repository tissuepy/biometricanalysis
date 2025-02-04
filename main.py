import os
import cv2

# Load query image
image_path_str = "/Users/nitishg/Desktop/Py Projects/biometric finger print recognition/biometric/SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP"
image_path = cv2.imread(image_path_str)

# Initialize variables
best_score = 0
image = None
filename = None
kp1, kp2, mp = None, None, None

real_images_path = "/Users/nitishg/Desktop/Py Projects/biometric finger print recognition/biometric/SOCOFing/Real"

counter = 0
for file in os.listdir("/Users/nitishg/Desktop/Py Projects/biometric finger print recognition/biometric/SOCOFing/Real")[:1000]:  # Process only first 1000 files
    file_path = os.path.join("/Users/nitishg/Desktop/Py Projects/biometric finger print recognition/biometric/SOCOFing/Real", file)  # Properly join path

    if counter % 10 == 0:
        print(counter, "Processing:", file_path)
    counter += 1

    fingerprint_image = cv2.imread(file_path)

    # Check if the image is read properly

    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(image_path, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    # Ensure descriptors are not None before matching
    if descriptors_1 is None or descriptors_2 is None:
        print(f"Warning: No descriptors found for {file_path}. Skipping.")
        continue

    matcher = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {})
    matches = matcher.knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = [p for p, q in matches if p.distance < 0.75 * q.distance]

    keypoints = min(len(keypoints_1), len(keypoints_2))
    if keypoints == 0:
        continue

    score_calc = len(match_points) / keypoints * 100

    if score_calc > best_score:
        best_score = score_calc
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points


# Ensure image is loaded before trying to display
if image is not None:
    result = cv2.drawMatches(image_path, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=4, fy=4)
    cv2.imshow("Result", result)
    cv2.waitKey(0)  # Corrected function
    cv2.destroyAllWindows()

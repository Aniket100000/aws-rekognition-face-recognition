# aws-rekognition-face-recognition
Cloud-based Face Recognition using AWS Rekognition and S3
Cloud-Based Face Recognition System (AWS Rekognition)

📌 Project Overview

This project demonstrates a cloud-native face recognition system using AWS Rekognition and Amazon S3.
The system detects and matches human faces from images stored in S3 using AWS managed AI services.
The project was initially implemented on a local environment for learning, and later upgraded to AWS to follow real-world cloud and serverless practices.

🚀 Technologies Used

AWS Rekognition – Face detection and face comparison
Amazon S3 – Image storage
AWS CloudShell – Command-line execution
AWS CLI
Linux (CloudShell environment)

🏗️ Architecture

1.Images are uploaded to an S3 bucket
2.A face collection is created using AWS Rekognition
3.Faces are indexed from stored images
4.A test image is compared against the collection
5.Rekognition returns:
>Face match confidence
>Face ID
>Bounding box & landmarks

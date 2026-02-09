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

📂 Project Structure

 face-recognition-aws/
│
├── screenshots/
│   ├── collection-created.png
│   ├── face-indexed.png
│   ├── face-matched.png
│   └── s3-bucket.png
│
├── commands/
│   └── rekognition-commands.txt
│
└── README.md


⚙️ Steps Performed

1️⃣ Configure AWS Region

aws configure set region ap-south-1

2️⃣ Create Face Collection

aws rekognition create-collection \
  --collection-id free-face-collection

✔ Output confirms:
StatusCode: 200
Collection ARN created

3️⃣ Upload Image to S3

Created S3 bucket:
face-recognition-free-test

Uploaded image inside:
test/person1.jpeg

4️⃣ Index Face into Collection

aws rekognition index-faces \
  --collection-id free-face-collection \
  --image "S3Object={Bucket=face-recognition-free-test,Name=test/person1.jpeg}" \
  --external-image-id "person1"

  ✔ Output includes:
  
FaceMatches
Similarity percentage
Bounding box & landmarks

📊 Sample Output

Face Match Similarity: 99%+
Face detected successfully
Matched with indexed face (person1)

💰 Cost Consideration

Project executed within AWS Free Tier
Used minimum images to avoid charges
No EC2 instances used (serverless approach)

🎯 Key Learnings

Hands-on experience with AWS Rekognition
Using AI services without managing servers
Working with S3 + Rekognition integration
Understanding real-world cloud workflows

🔮 Future Enhancements

Add multiple face indexing
Integrate with a web application
Store results in DynamoDB
Add IAM role-based security


🚀 FaceID Cloud – Intelligent Face Recognition System 

A complete cloud-based face recognition system built using AWS Rekognition, supporting both:

🧪 Serverless CLI-based workflow (S3 + CloudShell)
🌐 Full-stack Web App (Flask + EC2 + Modern UI)

🌐 Live Demo (Web App)

👉 http://13.233.45.217:5000

📌 Project Overview

This project demonstrates how to build a real-world AI-powered face recognition system using AWS services.

It was developed in two phases:

🔹 Phase 1: Serverless (AWS CLI + S3)

Face recognition using AWS Rekognition + S3
No backend server required
Executed via AWS CloudShell

🔹 Phase 2: Full Stack Web App

Interactive UI built with modern frontend
Backend using Flask (Python)
Deployed on AWS EC2
Real-time face upload and matching


✨ Features

🔍 Upload image and detect faces instantly
🤖 AWS Rekognition powered matching
⚡ Fast response (<2 seconds)
🎯 High accuracy (~99%+)
🧠 Face collection-based matching
💻 Modern UI/UX dashboard
☁️ Cloud deployment on AWS EC2
🔄 Supports both CLI and Web workflows
🖥️ Tech Stack


🔹 Frontend

HTML5
CSS3 (Modern UI Design)
JavaScript

🔹 Backend (Phase 2)

Flask (Python)
Boto3 (AWS SDK)

🔹 Cloud Services

AWS Rekognition (Face Detection & Matching)
Amazon S3 (Image Storage)
AWS EC2 (Hosting)
AWS IAM (Security & Access Control)
AWS CloudShell (CLI Execution)



🏗️ Architecture

🔹 Serverless Flow (Phase 1)

User → S3 Bucket → AWS Rekognition → Face Collection → Result

🔹 Web App Flow (Phase 2)

User → Web UI → Flask Backend → AWS Rekognition → Result UI



📸 Screenshots
🔹 Web UI (Modern Interface)




🔹 Face Detection




🔹 Collection Created





⚙️ Steps Performed (Phase 1 – CLI)

1️⃣ Configure AWS
aws configure set region ap-south-1

2️⃣ Create Collection
aws rekognition create-collection \
  --collection-id free-face-collection

3️⃣ Upload Image to S3
Bucket: face-recognition-free-test
Path: test/person1.jpeg

4️⃣ Index Face
aws rekognition index-faces \
  --collection-id free-face-collection \
  --image "S3Object={Bucket=face-recognition-free-test,Name=test/person1.jpeg}" \
  --external-image-id "person1"


  
🌐 How Web App Works (Phase 2)

User uploads image from browser
Flask backend receives file
Image sent to AWS Rekognition
Faces matched with collection
Result shown with confidence score


📊 Example Output

✅ Match Found
🎯 Confidence: 100%
🧑 Person ID: person1


📂 Project Structure

face-recognition-aws/
│
├── app.py
├── templates/
├── static/
├── screenshots/
├── commands/
│   └── rekognition-commands.txt
└── README.md


🔐 Security

IAM roles used (no hardcoded credentials)
Secure API access to Rekognition
Follows best practices


💰 Cost Consideration

Built using AWS Free Tier
Minimal resource usage
Optimized API calls


🎯 Key Learnings

AWS Rekognition hands-on implementation
Serverless architecture (S3 + CLI)
Full-stack deployment on EC2
Integration of AI with web apps
Real-world cloud project building


🔮 Future Enhancements

🔐 User authentication system
📸 Live webcam face detection
📱 Mobile responsiveness
🔒 HTTPS (SSL) setup
🗄️ Store results in DynamoDB

👨‍💻 Author
Aniket Kushwaha
📧 Aniketkushwaha10064@gmail.com
📱 9736550069

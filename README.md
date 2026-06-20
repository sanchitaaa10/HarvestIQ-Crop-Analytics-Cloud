# 🌾 HarvestIQ Crop Analytics Cloud
 
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED)
![License](https://img.shields.io/badge/License-Educational-lightgrey)
 
A cloud-based Crop Analytics and Management System built using **Flask, MySQL, Docker, and AWS Cloud Services**. HarvestIQ enables users to manage crop records, analyze agricultural yield, generate reports, and store files securely in the cloud.
 
---
 
## 📑 Table of Contents
 
* [Project Overview](#-project-overview)
* [Features](#-features)
* [System Architecture](#️-system-architecture)
* [Technologies Used](#️-technologies-used)
* [Project Structure](#-project-structure)
* [Installation & Setup](#️-installation--setup)
* [Docker Deployment](#-docker-deployment)
* [AWS Deployment](#️-aws-deployment)
* [Database Schema](#️-database-schema)
* [Application Screens](#-application-screens)
* [Security Features](#-security-features)
* [AWS Services Used](#-aws-services-used)
* [Estimated AWS Cost](#-estimated-aws-cost)
* [Learning Outcomes](#-learning-outcomes)
* [Author](#-author)
* [License](#-license)
---
 
## 📌 Project Overview
 
HarvestIQ is designed to demonstrate practical cloud engineering concepts by integrating AWS services with a web application. The system allows users to:
 
* Secure Login Authentication
* Add Crop Records
* View Crop Records
* Edit Crop Details
* Delete Crop Records
* Generate Crop Analytics Reports
* Upload Files to Amazon S3
* Store Data in Amazon RDS MySQL
* Deploy Application using Docker on AWS EC2
---
 
## 🚀 Features
 
### User Authentication
 
* Admin login system
* Secure access to dashboard
### Crop Management
 
* Add crop information
* View crop records
* Edit crop details
* Delete crop entries
### Analytics Dashboard
 
* Total crops
* Total yield
* Total locations
### Reports Module
 
* Crop statistics
* Yield analysis
### Cloud Storage
 
* Upload files to Amazon S3
* Cloud-based file management
### Cloud Deployment
 
* Dockerized Flask application
* Hosted on AWS EC2
* Connected to AWS RDS MySQL
---
 
## 🏗️ System Architecture
 
```text
User Browser
      |
      v
+----------------+
| EC2 Instance   |
| Flask + Docker |
+----------------+
      |
      +------------------+
      |                  |
      v                  v
+-----------+      +-----------+
| RDS MySQL |      | S3 Bucket |
+-----------+      +-----------+
 
      |
      v
 CloudWatch
 Monitoring
```
 
---
 
## 🛠️ Technologies Used
 
| Layer | Technology |
| --- | --- |
| Frontend | HTML5, CSS3 |
| Backend | Python, Flask |
| Database | MySQL, Amazon RDS |
| Cloud Services | AWS EC2, AWS RDS, AWS S3, AWS IAM, AWS CloudWatch |
| DevOps Tools | Docker, Git, GitHub |
| Operating System | Ubuntu Linux |
 
---
 
## 📂 Project Structure
 
```text
HarvestIQ-Crop-Analytics-Cloud/
│
├── app.py
├── create_db.py
├── requirements.txt
├── Dockerfile
├── harvestiq.db
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── add_crop.html
│   ├── crops.html
│   ├── edit_crop.html
│   └── reports.html
│
├── static/
│   └── css/
│       └── style.css
│
├── backups/
├── database/
├── reports/
└── README.md
```
 
---
 
## ⚙️ Installation & Setup
 
### 1. Clone Repository
 
```bash
git clone https://github.com/sanchitaaa10/HarvestIQ-Crop-Analytics-Cloud.git
cd HarvestIQ-Crop-Analytics-Cloud
```
 
### 2. Create Virtual Environment
 
```bash
python3 -m venv venv
source venv/bin/activate
```
 
### 3. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Run Application
 
```bash
python app.py
```
 
Application will be available at:
 
```text
http://127.0.0.1:5000
```
 
---
 
## 🐳 Docker Deployment
 
### Build Docker Image
 
```bash
docker build -t harvestiq .
```
 
### Run Container
 
```bash
docker run -d -p 5000:5000 harvestiq
```
 
### Verify Running Container
 
```bash
docker ps
```
 
---
 
## ☁️ AWS Deployment
 
### EC2
 
* Ubuntu Server
* Flask application hosting
* Docker runtime
### RDS MySQL
 
* Database name: `harvestiq`
* Managed relational database service
### S3
 
* File upload storage
* Cloud object storage
### IAM
 
* Role-based access control
* Secure S3 access from EC2
### VPC & Security Groups
 
* Network isolation within a dedicated VPC
* Firewall rules restricting EC2 and RDS access
### CloudWatch
 
* EC2 monitoring
* Resource utilization tracking
---
 
## 🗄️ Database Schema
 
### `crops` Table
 
| Column | Type |
| --- | --- |
| id | INT (Primary Key) |
| crop_name | VARCHAR |
| location | VARCHAR |
| yield_amount | FLOAT |
 
---
 
## 📸 Application Screens
 
* Login Page
* Dashboard
* Add Crop
* Crop Records
* Edit Crop
* Reports Dashboard
* File Upload Module
---
 
## 🔒 Security Features
 
* IAM role-based access
* Security groups for EC2 & RDS
* SSH key authentication
* Managed, access-controlled database
---
 
## 📊 AWS Services Used
 
| Service | Purpose |
| --- | --- |
| EC2 | Application hosting |
| RDS MySQL | Database |
| S3 | File storage |
| IAM | Access control & security |
| VPC | Network isolation |
| Security Groups | Firewall & access control |
| CloudWatch | Monitoring |
| Docker | Containerization |
 
---
 
## 💰 Estimated AWS Cost
 
| Service | Configuration | Approx. Cost / Month |
| --- | --- | --- |
| EC2 | t3.micro | $8.00 |
| RDS MySQL | db.t4g.micro | $13.00 |
| S3 | 1 GB Storage | $0.03 |
| CloudWatch | Basic Monitoring | Free Tier |
| IAM | Roles & Policies | Free |
| VPC | Default VPC | Free |
| Security Groups | EC2 & RDS Rules | Free |
| **Total** | | **≈ $21.03 / month** |
 
> Costs are approximate and may vary based on AWS region and usage.
 
---
 
## 📈 Learning Outcomes
 
This project demonstrates:
 
* Cloud infrastructure deployment
* Linux administration
* AWS resource management
* Database integration
* Docker containerization
* Cloud storage integration
* Monitoring & logging
* Security best practices
---
 
## 👩‍💻 Author
 
**Sanchita Suryawanshi**
B.Tech Computer Science & Engineering
ITM Skills University
 
GitHub: [sanchitaaa10](https://github.com/sanchitaaa10)
 
---
 
## 📜 License
 
This project is developed for educational and academic purposes as part of Cloud Computing and AWS Cloud Engineering coursework.
 

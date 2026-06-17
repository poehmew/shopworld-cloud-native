# ShopWorld Cloud Native

A cloud-native e-commerce application built on Google Cloud Platform.

## Architecture

```text
User
↓
Firebase Authentication
↓
Cloud Run Frontend
↓
Cloud Run Backend
↓
Cloud SQL Database
↓
BigQuery Analytics
↓
Cloud Monitoring Dashboard
```

## Technologies Used

- Google Cloud Run
- Cloud SQL
- BigQuery
- Firebase Authentication
- Cloud Monitoring
- GitHub Actions
- Terraform
- Docker

## Features

- Product catalogue
- Shopping cart
- Checkout workflow
- User authentication with Google
- Analytics reporting
- Infrastructure monitoring

## Monitoring Dashboard

The application is monitored using Google Cloud Monitoring with custom dashboards showing:

- Cloud Run Request Count
- Cloud Run Latency
- Cloud Run Errors
- Cloud SQL CPU Usage
- Cloud SQL Connections

## Infrastructure as Code

Terraform configuration is available in the `/terraform` folder.

## Project Structure

```text
shopworld-cloud-native
├── backend
├── frontend
├── database
├── terraform
├── .github/workflows
├── deploy.yml
└── README.md
```

## Author
Poe Eint Hmew
BAchelor of Computer Science

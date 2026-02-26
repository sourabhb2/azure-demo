# 🚀 Python Flask Deployment to Azure App Service using GitHub Actions (OIDC)

This repository demonstrates a **simple, modern, and production‑ready CI/CD pipeline** to deploy a Python Flask application to Azure App Service using **GitHub Actions with OIDC authentication (no secrets)**.

This approach is recommended by Microsoft and widely used in real DevOps environments.

---

## 🎯 Project Overview

This project covers:

* Python Flask application
* Azure App Service deployment
* GitHub Actions automation
* Secure OIDC authentication
* Continuous deployment on every commit

---

## 📌 Architecture

Developer → GitHub → GitHub Actions → Azure OIDC → Azure App Service

---

## 🧰 Tech Stack

* Python
* Flask
* GitHub Actions
* Azure App Service
* Azure Active Directory (OIDC)

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## ✅ Step 1: Create Python Flask App

### app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Python deployed successfully 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

### requirements.txt

```
Flask
gunicorn
```

---

## ✅ Step 2: Create Azure App Service

1. Go to Azure Portal
2. Search "App Services"
3. Click "Create Web App"
4. Select:

   * Python runtime
   * Region
   * Free or Basic plan

---

## ✅ Step 3: Create Service Principal

Run in Azure Cloud Shell:

```
az ad sp create-for-rbac --name github-oidc-deploy --role contributor
```

Save:

* appId

---

## ✅ Step 4: Get Subscription and Tenant

```
az account show
```

Save:

* subscriptionId
* tenantId

---

## ✅ Step 5: Configure Federated Credential

```
az ad app federated-credential create \
  --id <APP_ID> \
  --parameters '{
    "name": "github",
    "issuer": "https://token.actions.githubusercontent.com",
    "subject": "repo:<GITHUB_USERNAME>/<REPO>:ref:refs/heads/main",
    "audiences": ["api://AzureADTokenExchange"]
  }'
```

---

## ✅ Step 6: GitHub Repository Setup

Enable in:

Settings → Actions → General

* Read and write permissions

---

## ✅ Step 7: GitHub Actions Workflow

Create:

```
.github/workflows/deploy.yml
```

```yaml
name: Deploy Python App

on:
  push:
    branches:
      - main

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Azure Login
        uses: azure/login@v1
        with:
          client-id: <APP_ID>
          tenant-id: <TENANT_ID>
          subscription-id: <SUBSCRIPTION_ID>

      - name: Deploy
        uses: azure/webapps-deploy@v2
        with:
          app-name: <APP_SERVICE_NAME>
          package: .
```

---

## ✅ Step 8: Deploy

Push code to GitHub.

GitHub Actions automatically deploys.

---

## 🌐 Step 9: Verify

Open:

```
https://<APP_SERVICE_NAME>.azurewebsites.net
```

---

## 🔄 CI/CD Testing

Update app.py and push.

New version deploys automatically.

---

## 🛠 Troubleshooting

### Azure login fails

Check:

* Federated credential
* Branch name
* Workflow permissions

### App not loading

* Azure log stream
* Restart app

---

## 🔐 Security Best Practices

* No secrets
* OIDC authentication
* Least privilege
* Role-based access

---

## 🚀 Future Enhancements

* Docker deployment
* Terraform automation
* Multi-environment pipelines
* Monitoring and alerts
* Canary deployments

---

## ⭐ Why This Project Matters

This project demonstrates:

* Modern DevOps
* Secure CI/CD
* Azure cloud automation
* Production-ready practices

It is ideal for:

* DevOps Engineers
* Cloud Engineers
* Azure Developers

---

## 🙌 Author

Sourabh Bhoyar
DevOps Engineer

---

If you find this helpful, please ⭐ the repository!

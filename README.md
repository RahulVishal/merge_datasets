merge_datasets 🧩

A Django-powered web platform that allows users to upload two datasets (e.g. CSV files) and merge them using various join types—inner, outer, left, or right—directly from the browser.

Table of Contents

Features
Tech Stack
Installation
Usage
How It Works
File Structure
Contributing
License
Features

Upload two dataset files via web interface
Choose merge type: inner, outer, left, or right
Download merged result instantly
Clean UI with clear instructions
Tech Stack

Backend Framework: Django
Data Processing: Pandas
Front-end: Django Templates (HTML + CSS)
Others: Bootstrap (optional), Python 3.8+
Installation

Clone the repository
git clone https://github.com/RahulVishal/merge_datasets.git
cd merge_datasets
Set up virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Apply Django migrations
python manage.py migrate
Create a superuser (optional, for admin access)
python manage.py createsuperuser
Start the development server
python manage.py runserver
Access the app by visiting http://127.0.0.1:8000/ in your browser.
Usage

Navigate to the homepage.
Upload two datasets (CSV format preferred).
Select join type from the dropdown menu.
Click Merge—the merged dataset displays on screen.
Optionally, click Download to retrieve the result as a CSV.
How It Works

The core logic is in views.py:

import pandas as pd

# Read uploaded files into DataFrames
left_df = pd.read_csv(request.FILES['file1'])
right_df = pd.read_csv(request.FILES['file2'])

# Merge based on selected type
merged_df = pd.merge(left_df, right_df, how=join_type)

# Save result to HttpResponse for download/render inline
Supported join types correspond to pd.merge(how=<join>):

inner (default)
outer
left
right
File Structure

merge_datasets/
├── merge_datasets/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/
│   ├── views.py       ← Merge logic
│   ├── forms.py       ← Upload forms
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html ← Upload & merge UI
│   │   └── result.html← Display merged data
├── static/            ← CSS & JS (if any)
├── requirements.txt
└── manage.py
Contributing

Fork the repo 🔀
Create a feature branch (git checkout -b feature/my-feature)
Make your edits & add tests
Submit a Pull Request for review

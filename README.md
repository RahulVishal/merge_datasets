
# merge_datasets 🧩

A Django-powered web platform that allows users to upload two datasets (e.g. CSV files) and merge them using various join types—**inner**, **outer**, **left**, or **right**—directly from the browser.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Upload two dataset files via web interface  
- Choose merge type: `inner`, `outer`, `left`, or `right`  
- Download merged result instantly  
- Clean UI with clear instructions  

---

## Tech Stack

- **Backend Framework**: Django  
- **Data Processing**: Pandas  
- **Front-end**: Django Templates (HTML + CSS)  
- **Others**: Bootstrap (optional), Python 3.8+

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/RahulVishal/merge_datasets.git
   cd merge_datasets
   ```

2. **Set up virtual environment & install dependencies**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Apply Django migrations**  
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**  
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Access the app** by visiting `http://127.0.0.1:8000/` in your browser.

---

## Usage

1. Navigate to the homepage.  
2. Upload two datasets (CSV format preferred).  
3. Select **join type** from the dropdown menu.  
4. Click **Merge**—the merged dataset displays on screen.  
5. Optionally, click **Download** to retrieve the result as a CSV.

---

## How It Works

The core logic is in `views.py`:

```python
import pandas as pd

# Read uploaded files into DataFrames
left_df = pd.read_csv(request.FILES['file1'])
right_df = pd.read_csv(request.FILES['file2'])

# Merge based on selected type
merged_df = pd.merge(left_df, right_df, how=join_type)

# Save result to HttpResponse for download/render inline
```

Supported join types correspond to `pd.merge(how=<join>)`:  
- `inner` (default)  
- `outer`  
- `left`  
- `right`

---

## File Structure

```
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
```

---

## Contributing

1. Fork the repo 🔀  
2. Create a feature branch (`git checkout -b feature/my-feature`)  
3. Make your edits & add tests  
4. Submit a Pull Request for review

---

## License

This project is released under the [MIT License](LICENSE). Made with ❤️ by Rahul.

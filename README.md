# NLP Assignment 1 – Custom Dataset Creation

## Project Description

This project creates a custom NLP dataset by scraping Wikipedia pages of famous inventors.
Each inventor's information is extracted and stored in separate text files.
All files are then merged into a single master dataset.

This assignment demonstrates:

* Web scraping
* Data collection
* File handling
* Dataset creation
* GitHub and Kaggle dataset publishing

---

## Topic

The selected topic for this dataset is:

**Famous Inventors**

Inventors included in this dataset:

* Thomas Edison
* Nikola Tesla
* Alexander Graham Bell
* James Watt
* Alan Turing
* Tim Berners-Lee
* Johannes Gutenberg
* Leonardo da Vinci
* Wright Brothers
* Benjamin Franklin

---

## Project Structure

```
NLP-LAB-Assignments
│
├── ASSIGN1.PY
├── README.md
├── inventions_inventors_dataset.csv
│
└── inventor_files
    ├── thomas_edison.txt
    ├── nikola_tesla.txt
    ├── alan_turing.txt
    ├── james_watt.txt
    └── ...
```

---

## Workflow

### Step 1 – Individual Data Extraction

The Python script visits the Wikipedia page of each inventor and extracts textual data from the page.

Each inventor’s data is saved as an individual `.txt` file inside the `inventor_files` folder.

Examples:

* `thomas_edison.txt`
* `nikola_tesla.txt`
* `alan_turing.txt`

---

### Step 2 – Data Merging

After generating individual text files, the script reads all files and merges them into a master dataset:

```
inventions_inventors_dataset.csv
```

The dataset contains the following columns:

| Column   | Description              |
| -------- | ------------------------ |
| Inventor | Name of the inventor     |
| Text     | Extracted Wikipedia text |

---

## Libraries Used

The following Python libraries are used in this project:

* os
* csv
* time
* requests
* beautifulsoup4 (bs4)

---

## Installation

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

---

## How to Run

Run the Python script using:

```bash
python ASSIGN1.PY
```

---

## Output

After running the script:

1. A folder named `inventor_files` is created.
2. Separate text files are saved for each inventor.
3. A master dataset file is generated:

```
inventions_inventors_dataset.csv
```

---

## Data Source

The dataset is collected from:

Wikipedia

---

## Submission Links

GitHub Repository
https://github.com/project496/NLP_assignment_1

Kaggle Dataset
https://www.kaggle.com/datasets/aleezagulzar/inventions-inventors

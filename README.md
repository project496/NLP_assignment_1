diff --git a/c:\Users\eb034\LLM\NLP\ASSIGNMENT\README.md b/c:\Users\eb034\LLM\NLP\ASSIGNMENT\README.md
new file mode 100644
--- /dev/null
+++ b/c:\Users\eb034\LLM\NLP\ASSIGNMENT\README.md
@@ -0,0 +1,99 @@
+# NLP Assignment 1
+
+This project creates a custom NLP dataset by scraping Wikipedia pages of famous inventors, storing each inventor's text in a separate file, and combining all files into one master CSV dataset.
+
+## Files
+
+- `ASSIGN1.PY` - main Python script
+- `inventor_files/` - individual text files for each inventor
+- `inventions_inventors_dataset.csv` - merged master dataset
+
+## Topic
+
+The topic selected for this assignment is **famous inventors**.
+
+Inventors included:
+
+- Thomas Edison
+- Nikola Tesla
+- Alexander Graham Bell
+- James Watt
+- Alan Turing
+- Tim Berners-Lee
+- Johannes Gutenberg
+- Leonardo da Vinci
+- Wright brothers
+- Benjamin Franklin
+
+## What the Script Does
+
+### 1. Individual Extraction
+
+The script opens the Wikipedia page of each inventor and extracts text from the first paragraph sections of the page.
+
+Each inventor's data is saved as a separate `.txt` file inside the `inventor_files` folder.
+
+Examples:
+
+- `thomas_edison.txt`
+- `nikola_tesla.txt`
+- `alan_turing.txt`
+
+### 2. Data Merging
+
+After creating the individual text files, the script reads them all and merges the content into one CSV file:
+
+- `inventions_inventors_dataset.csv`
+
+The CSV contains:
+
+- `Inventor`
+- `Text`
+
+## Libraries Used
+
+- `os`
+- `csv`
+- `time`
+- `requests`
+- `bs4` (`BeautifulSoup`)
+
+## How to Run
+
+Install required libraries:
+
+```bash
+pip install requests beautifulsoup4
+```
+
+Run the script:
+
+```bash
+python ASSIGN1.PY
+```
+
+## Output
+
+After running the script:
+
+1. A folder named `inventor_files` is created.
+2. Separate text files are saved for each inventor.
+3. A master CSV file named `inventions_inventors_dataset.csv` is generated.
+
+## Data Source
+
+The data is collected from:
+
+- Wikipedia
+
+## Important Note
+
+If the `Text` column in the CSV is empty, the scraper may not have successfully extracted the page content. In that case, the scraping logic should be improved by adding headers, checking response status, or updating the HTML selection logic.
+
+## Submission Links
+
+Add your final links here after upload:
+
+- GitHub Repository: `[PASTE_YOUR_GITHUB_REPOSITORY_LINK](https://github.com/project496/NLP_assignment_1)`
+- Kaggle Dataset: `[PASTE_YOUR_KAGGLE_DATASET_LINK](https://www.kaggle.com/datasets/aleezagulzar/inventions-inventors)`

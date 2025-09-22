# Info-Retrieval-system from Multiple PDF with PaLM2

# How to run?
### STEPS:

clone the repository

```bash
Project repo: https://github.com/anjeesanjeet/Info-Retrieval-system
```

### STEP 1 - Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.8 -y
```

```bash
conda activate llmapp
```

### STEP 2 - Install the requirements
```bash
pip install -r requirements.txt
```

### Create a '.env' file in the root directory and add your GOOGLE_API_KEY as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
#Finally run the following command
streamlit run app.py
```

Now,
```bash
open: https://localhost:8501

### Techstack Used:

-Python
-LangChain
-Streamlit
-PaLM2
-FAISS
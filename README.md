# Automated Student Submission Evaluator

This GitHub repository contains a tool for automatically evaluating student submissions. Follow the steps below to set up and use the tool effectively.## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)

---

## Prerequisites

Before you can use this tool, make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [Git](https://git-scm.com/downloads)

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/MadhavBohra/Automaded-Code-Evaluation-Tool.git
```
   
2. Change your current directory to the project folder:
   
```bash
cd Automaded-Code-Evaluation-Tool
```
         
3. Create a Python virtual environment:
         
```bash
python -m venv venv
```
                
4. Activate the virtual environment:
                
- On Windows:
                  
```bash
venv\\Scripts\\activate
```
                              
- On macOS and Linux:
                               
```bash
source venv/bin/activate
```
                                        
5. Install the required Python packages:
                                        
```bash
pip install -r requirements.txt
```


---



## Usage

To evaluate student submissions, follow these steps:

1. Ensure the correct folder structure (as mentioned above) is in place.

2. Run the provided shell script (`run.sh`) to create the folder structure and execute the evaluation:

```bash
    ./run.sh
```

This script will set up the necessary directories and run the evaluation.



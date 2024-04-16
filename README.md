# Recipe Directory Project

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:andrew-laing-uk/recipe_directory_project.git recipe_directory_project

# Or, if you don't have SSH keys set up
; git clone https://github.com/andrew-laing-uk/recipe_directory_project.git recipe_directory_project

# Enter the directory
; cd recipe_directory

# Set up the virtual environment
; python -m venv recipe_directory_venv

# Activate the virtual environment
; source recipe_directory_venv/bin/activate 

# Install dependencies
(recipe_directory_venv); pip install -r requirements.txt

# Create the database
(recipe_directory_venv); createdb recipe_directory

# Run the tests
(recipe_directory_venv); pytest

# Run the app
(recipe_directory_venv); python app.py
```
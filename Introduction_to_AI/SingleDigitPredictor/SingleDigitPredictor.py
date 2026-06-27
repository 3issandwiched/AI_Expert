# for this newer version of python Tensorflow is compatible 
# we need to downgrade the python 


#Step 1: Install a Supported Python Version globallyGo to the official Python Downloads for Windows page,
#  download the installer for Python 3.12, and install it.Crucial: During installation, 
# ensure you check the box that says "Add python.exe to PATH" so Windows can discover it from your command line


#Step 2: Create a Clean, Version-Targeted Virtual Environment

# # 1. Exit your current unsupported environment
#deactivate

# 2. Create a new environment explicitly targeting Python 3.12
#py -3.12 -m venv tf_env

# 3. Activate the new environment
#.\tf_env\Scripts\activate


#Step 3: Run the Installation Again

#python -m pip install --upgrade pip
#pip install tensorflow


#OR

#Use Colab
import webbrowser

# Replace this with your actual target URL
url = "https://colab.research.google.com/drive/1yCH3Xjwhm-K_7y1Y6feZWJArHXt9xVky?usp=sharing"

print(f"Opening your link: {url}")

# This opens the URL in the user's default browser (Chrome, Edge, Safari, etc.)
webbrowser.open(url)


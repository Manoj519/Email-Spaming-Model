# Email-Spaming-Model
Email spaming model tell us that email is spam or not.

## There are some steps to set-up the project.

### 1.) Folder Making
Make a folder in any drive(eg. F:\Email Spam).

### 2.) Download Project
Download project in "Email Spam" folder.

### 3.) Create Virtual Environment
###### Install Virtual Environment
'Pip install virtualenv'<br/>
This command type in command prompt at specific location(eg. F:\Email Spam).<br/>
Now here 2 folder and 4 files are present : <br/>
A.) emailspam (Project)<br/>
B.) myenv (Virtual Environment)<br/>
C.) Email-Spaming-Model.html (html file for visualization of code.)<br/>
D.) requirement.txt (text file with all packages.)<br/>
E.) .gitignore<br/>
F.) README.md <br/>

###### Folder Creation
'''
Virtualenv myenv 
'''<br/>
This Command create virtual environment with myenv folder automatically.<br/>

###### Enter Into Virtual Environment
'''
F:\Email Spam>myenv\scripts\activate 
'''<br/>
Now activate the virtual environment by above command. And it will change<br/>
(myenv) F:\Email Spam>myenv>

###### Install Django and Other Packages<br/>
'''
pip install -r requirements.txt 
'''<br/>
Using this command django and other libraries install automatically.<br/>

### 4.) Open Project
Open Pycharm and tab on open and select the "emailspam" folder as project.

### 5.) Makemigrations
Now back to command prompt and type <br/>
'''
Python manage.py makemigrations
'''<br/>
(eg. (myenv) F:\Email Spam>myenv>Python manage.py makemigrations).

### 6.) Migrate
'''
Python manage.py migrate 
'''<br/>
(eg. (myenv) F:\Email Spam>myenv>Python manage.py migrate).

### 7.) Run Server
'''
Python manage.py runserver 
'''<br/>
(eg. (myenv) F:\Email Spam>myenv>Python manage.py runserver).<br/>
This will run the server and give the localhost path in it.(eg. http://127.0.0.1:8000/)<br/>
Copy the url from your command prompt and paste on browser and enjoy the project.

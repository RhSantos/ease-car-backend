# 🛠 EaseCar Backend

## ℹ️ About the Backend
EaseCar App Backend using **Python Django 5.0.3**

## 🌐 API Routes
undefined

## 🗃️ Database Architecture
undefined

## 🧪 Tests

### Unit Tests
undefined

## :file_folder: Package Structure
undefined

## :package: Dependencies
- Django REST Framework
- Pillow (Image Library)
- Virtual Env (For dependency management)

## ▶️ Running the Server

### Local Instance

#### Install Python and Django
Make sure you have Python installed on your system. Then, install Django using pip:
`pip install django`

#### Navigate to the Project Directory
Navigate to the directory of your existing Django project.

#### Create and Use the Virtual Environment

1. **Install Python Virtual Environment**:
   If you are using Python 3.3 or later, you can use the built-in `venv` module to create a virtual environment. For earlier versions, you can use the third-party `virtualenv` tool.<br/>

2. **Create a Virtual Environment**:
   For Python 3.3 or later, use the following command to create a virtual environment:
   ```
   python -m venv myenv
   ```
   For earlier versions using `virtualenv`, use:
   ```
   pip install virtualenv
   virtualenv myenv
   ```
   Replace `myenv` with the desired name for your virtual environment.<br/>

3. **Activate the Virtual Environment**:
   After creating the virtual environment, you need to activate it. The command to activate the environment varies depending on your operating system:
   - **Windows**:
     `myenv\Scripts\activate`
   - **Unix/MacOS**:
     `source myenv/bin/activate`
   Once the environment is activated, you will see the name of the virtual environment in your command prompt.

#### Install Dependencies
Ensure all dependencies are installed by running: 
`pip install -r requirements.txt`

#### Configure Database Settings
Set up the database configurations in the `settings.py` file.

#### Apply Migrations
Apply any pending migrations with: 
```
python manage.py makemigrations 
python manage.py migrate
```
#### Start the Development Server
Start the Django development server with: 
`python manage.py runserver`

### Remote Working Instance

Use this server on:

status: `Not Running ❌`
url: undefined

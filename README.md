# Python Email Sender

This Python script enables you to effortlessly send emails. By simply providing the recipient's email address and the subject of the email, you can swiftly dispatch messages. Additionally, you have the option to customize the content of the email by configuring the `index.html` file.

## Configuration

1. **Before running your Python script, configure your email and Google app password.**

   **Create & use app passwords**
   Important: To create an app password, you need 2-Step Verification on your Google Account.
   
   1. Go to your [Google Account](https://myaccount.google.com/).
   2. Select Security.
   3. Under "How you sign in to Google," select 2-Step Verification.
   4. At the bottom of the page, select App passwords.
   5. Enter a name that helps you remember where you’ll use the app password.
   6. Select Generate.
   7. To enter the app password, follow the instructions on your screen. The app password is the 16-character code that generates on your device.
   8. Select Done.

   If you’ve set up 2-Step Verification but can’t find the option to add an app password, it might be because:

   - Your Google Account has 2-Step Verification set up only for security keys.
   - You’re logged into a work, school, or another organization account.
   - Your Google Account has Advanced Protection.

   Tip: Usually, you’ll need to enter an app password once per app or device.

2. **Now, you need to configure your email credentials in the environment variables. This will ensure that the script can access your email account securely. You have two options to do this:**

   1. **Manual Configuration in the Command Line:**
      Use your operating system's commands to define the environment variables `EMAIL_REMITTER` and `EMAIL_PASSWORD` with your email address and the password you have generated, respectively.

      - On Unix/Linux systems, you can do it as follows:
        ```
        export EMAIL_REMITTER=your_email@gmail.com
        export EMAIL_PASSWORD=your_password
        ```

      - On Windows, you can do it this way:
        ```
        set EMAIL_REMITTER=your_email@gmail.com
        set EMAIL_PASSWORD=your_password
        ```

   2. **Using the python-dotenv Library:**
      You can utilize the `python-dotenv` library to automatically load environment variables from a `.env` file in the project directory. First, make sure to install the library using pip:
      ```
      pip install python-dotenv
      ```

      Then, create a `.env` file in the project directory and define the environment variables:
      ```
      EMAIL_REMITTER=your_email@gmail.com
      EMAIL_PASSWORD=your_password
      ```

      Now, in your Python script, you can use `python-dotenv` to load these variables:
      ```python
      from dotenv import load_dotenv
      import os

      # Load environment variables from the .env file
      load_dotenv()

      # Get the environment variables
      remitter = os.getenv("EMAIL_REMITTER")
      password = os.getenv("EMAIL_PASSWORD")
      ```

## HTML File Configuration
The script provides the flexibility to customize the content of the email using an HTML file. This file, named `index.html`, acts as the template for the body of the email. You can edit this file to include the design, format, and specific content you want to send in your emails.

## Usage
Open a terminal and navigate to the project directory:
```
cd send-emails
```
Run the script with the following command:
```
python main.py
```
Follow the instructions in the terminal to provide the recipient's email address and the subject of the email.
That's it! The email will be automatically sent using your Gmail account.
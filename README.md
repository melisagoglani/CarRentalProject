# Car Rental Project
## Overview
A system to rent cars as a customer, taking into account the availability of said cars. While as a manager of the system, you can add, edit, and delete cars from the database.

This project was the finals project for my beginners' Python university course, using **Python** and the **file-handling** in Python for the logic, and  **prettytable** for the UI.

This project uses a simple UI ran on the terminal with numbers next texts to indicate actions. After errors, and seeing an empty table, or successfully renting a car, using the **time** built-in Python library, natural pauses occur before returning to the last tree.

Successfully renting a car adds it to your invoices, which is accessible through the customer panel. 

To access the admin panel, a hard-coded password is required (see source code) — flagged in Future Improvements as something to fix.

## Future improvements
1. Using maybe SQLite or other database frameworks for this project is necessary, however I simply didn't have the knowledge back then
2. Letting the admin choose their passwords, enabling usernames and passwords for customers, and using hashing for a higher level of security
3. Utilizing graphics for ease of use, either as an app, or a website

## The UI
<img width="490" height="341" alt="Screenshot" src="https://github.com/user-attachments/assets/81e64528-6509-4792-b507-03cb3b66016f" />

## How to run
1. Clone the repo
2. Run CarRentalProject.py
3. Choose from the actions displayed by entering the number next to it

#ML-Model-Flask-Deployment



This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

Prerequisites You must have Scikit Learn, Pandas (for Machine Learning Model) and Flask (for API) installed.

Project Structure

#This project has four major parts :


model.py - This contains code fot our Machine Learning model to Predict the probability of Forest-Fire Occurence absed on trainign data in 'Forest_fire.csv' file.

app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.

request.py - This uses requests module to call APIs already defined in 'app.py' and dispalys the returned value.

templates - This folder contains the HTML template to allow user to enter employee detail and displays the Predict the probability of Forest-Fire Occurence.

#Running the project


Ensure that you are in the project home directory.

Create the machine learning model by running below command - (python model.py)

This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API (python app.py)

By default, flask will run on port 5000.

Navigate to URL http://localhost:5000

![Screenshot 2024-04-21 085727](https://github.com/osama3442ws/Website-for-Predicting-Forest-Fires/assets/141057634/59ba2616-f6d5-4bcd-ae45-05f890ce0523)
![Screenshot 2024-04-21 085826](https://github.com/osama3442ws/Website-for-Predicting-Forest-Fires/assets/141057634/f523eb5d-ed9f-424a-9d80-4f034c183a2f)
![Screenshot 2024-04-21 090815](https://github.com/osama3442ws/Website-for-Predicting-Forest-Fires/assets/141057634/c8be6b95-ca31-412d-a7b8-4461f2d0b9e1)
![Screenshot 2024-04-14 185403](https://github.com/osama3442ws/Website-for-Predicting-Forest-Fires/assets/141057634/fc1b6693-32b0-4065-877a-851e561e4d6f)
![Screenshot 2024-04-14 185453](https://github.com/osama3442ws/Website-for-Predicting-Forest-Fires/assets/141057634/290cd3b5-1f76-48a4-a8dc-050fe8b40c05)
![Screenshot 2024-04-14 185529](https://github.com/osama3442ws/Website-for-Predicting-Forest-Fires/assets/141057634/934c4bda-b507-4811-86f5-71207cc92b3a)






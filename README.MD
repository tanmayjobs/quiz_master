# Quiz Master

Quiz Master is a platform where you can create your own quizzes and can play quizzes by creators across the globe.

## Getting Started

To run the program, please follow these steps to get started:

1. Clone this repository to your local machine.
2. Change directory to `quiz_master/src/`.
3. Run the program using `python main.py`.

## Folder Structure

This repo contains three major folders:
1. `docs`: This folder contains project documentations, such as Requirement, Class Diagram and DB Diagram.
2. `src`: This folder contains the code for the project.
   1. constants: This folder contains `constants.yaml` which contains all the constant. Also contain the classes used to access those constants.
   2. controller: This folder contains the controlling functions. These functions are responsible for extracting the parameters for user request and send them to respective service. And then wrap data of the services and send it to screens.
   3. data_containers: This folder contains the data models for programs.
   4. database: This folder is responsible to initialize the database and provide one single instance of database to perform operations.
   5. log: This folder contains the log of our application.
   6. screens: This folder contains the UI part of our application.
   7. services: This folder contains the services which are responsible to interact with database.
   8. utils: This folder contains the utilities for our program.
   9. `.yaml`: This file is not used by system, but is used to know about the application.
   10. `main.py`: This is the entry point of the system.

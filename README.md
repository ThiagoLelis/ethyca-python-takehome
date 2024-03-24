# Flask Application README

This README provides instructions for setting up and running the Flask application. Please ensure you have Python installed on your system.

## Dependencies

```
- Flask
```

## Installation

1. Clone the repository:

    ```git clone https://github.com/ThiagoLelis/ethyca-python-takehome.git```

2. Navigate to the project directory: 

    ```cd ethyca-python-takehome```

3. Create a new virtualenv with Python 3.7 or greather

4. Install dependencies using pip:

    ```pip install -r requirements.txt```

## Running the Application

To run the Flask application, execute the following command:

```python app.py```


This will start the Flask server, and you should be able to access the application at `http://localhost:5000` in your web browser.

## Running Tests

Before running the tests, ensure that the required dependencies are installed by executing:

```pip install -r requirements.txt```


To run the tests, use the following command:

```python run_tests.py```


## Specifications

### Endpoints

### Create New Game

- **URL:** `/api/v1/games`
- **Method:** `POST`
- **Description:** Creates a new game with an optional board type parameter (`board_type`). If not specified, a normal-sized board is created. Available board types are "normal", "large", and "small".
- **Request Body:**
  ```json
  {
    "board_type": "normal"
  }
- **Response:** Returns the game id.

### Get All Games
- **URL:** `/api/v1/games`
- **Method:** `GET`
- **Description:** Retrieves a list of all available games.
- **Response:** Returns a list of game objects.

### Make Move
- **URL:** `/api/v1/games/<game_id>/moves`
- **Method:** `POST`
- **Description:** Makes a move in the specified game identified by game_id.
- **URL Parameters:** game_id: ID of the game to make a move in.
- **Request Body:**
```json
{
  "x": 2,
  "y": 2
}
```
- **Response:** Returns the updated game state after the move.

### Get Moves
- **URL:** `/api/v1/games/<game_id>/moves`
- **Method:** `GET`
- **Description:** Retrieves a list of moves made in the specified game identified by game_id.
- **URL** Parameters: game_id: ID of the game to retrieve moves from.
- **Response:** Returns a list of move objects.


## Notes

### Tradeoffs


- I assumed not to use any database at the beginning due to the short time, in a real application this is unthinkable due to the limitations it brings

- I focused on creating the tests first and then implementing

- I created more integration tests only when it depended on random objects I created unit tests

- I decided to use flask due to the simplicity of the application, I considered between django and fastapi, but due to the greater complexity with django it was initially discarded, leaving the doubt between fastapi and flask.

### Extra Feature
```
- It is possible to pass the board_type parameter as a parameter when creating the game with the values large and and huge, where large will create a 5x5 game and huge will create a 10x10
```

### Time Spent

```
- Approximately 4 hours were spent on this work.
- Approximately 30 minutes with documentation
```

### Git Logs

Below are the Git logs with the changes made during development:
![image](https://github.com/ThiagoLelis/ethyca-python-takehome/assets/42333/5777a64a-458b-419c-81a7-caceea032efa)

Feel free to explore the commit history for more details on the changes made.


### Coverage report
![image](https://github.com/ThiagoLelis/ethyca-python-takehome/assets/42333/9256d3e8-023e-4143-8239-8dfb067d42c4)

# YouTube Manager

YouTube Manager is a command-line application built using Python that helps users manage their collection of YouTube videos. The application allows users to list, add, update, and delete video information, with the data being stored in a `.txt` file using the `json` module for structured storage.

## Features

1. **List all YouTube videos**  
   Displays all videos stored in the system along with their name and duration.

2. **Add a YouTube video**  
   Allows the user to input a new YouTube video by providing its name and duration.

3. **Update YouTube video details**  
   Enables the user to modify the name or duration of an existing video.

4. **Delete a YouTube video**  
   Allows the user to remove a video from the list.

5. **Exit the application**  
   Closes the program.

## How it Works

The program uses a `.txt` file to store video details (name and duration) in JSON format. The following steps are performed during the execution of each task:

- **List videos**: Reads from the file and displays the video details.
- **Add video**: Adds a new video entry to the list and updates the file.
- **Update video**: Modifies the details of an existing video and updates the file.
- **Delete video**: Removes a video entry from the file.

## Installation

1. Clone the repository to your local machine:
    git clone https://github.com/Sid080802/YouTube_Manager.git
    

2. Navigate to the project directory:
    cd YouTube_Manager

3. Make sure you have Python installed on your system. You can install Python from [here](https://www.python.org/downloads/).

## Usage

1. Run the Python script:
    python youtube_manager.py

2. Follow the on-screen prompts to manage your YouTube video collection.

## File Structure

- `youtube_manager.py`: The main Python file that runs the command-line application.
- `youtube_manager.txt`: Stores the YouTube video details in JSON format.

## Dependencies

- Python 3.12.5
- No external dependencies required, only Python's built-in `json` module is used.



# importing json package for data loading...
import json

#these function is for load the data of paticular file in json format.
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#these function save the changes in file.
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

#these function show the list of all videos in the file.
def list_all_videos(videos):
    print('\n')
    print('*'*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

    print('\n')
    print('*'*70)

#these function add the new youtube video name and time in list.
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    print("**********Video added sucessfully*********")
    save_data_helper(videos)

#these function update video details in the given list.
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))

    if 1<= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos[index-1] = {'name': name, 'time': time}
        print("**********Video updated sucessfully*********")
        save_data_helper(videos)
    else:
        print("Invalid index selected")

#these function delete the video by indexing.
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))

    if 1<= index <= len(videos):
        del videos[index-1]
        print("**********Video deleted sucessfully*********")
        save_data_helper(videos)
    else:
        print("Invalid index selected")

# Entry point of program start execution from these function.
def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        #it takes user input or choices
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            # these is default case or if user choose other number that 1-5 these case will execute.
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
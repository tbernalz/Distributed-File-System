import grpc
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Protobufs import Service_pb2
from Protobufs import Service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051') # Replace with the address of your nameNode Leader bootstrap
    nameNode_stub = Service_pb2_grpc.ClientServiceStub(channel)

    while True:
        print("\nMenu:")
        print("1. List files") # mostrar todos los nombres de los archivos que hay en el sistema
        print("2. Create file") # es como hacer mkdir. (file_name, data)
        print("3. Open file to read or write") # es como hacer cd directory_name. (directory_name)
        print("4. Close file") # es como hacer cd..  (directory_name)
        print("5. Read file") # (file_name)
        print("6. Write file") # (file_name)
        print("7. Exit")     

        choice = input("Enter your choice: ")

        if choice == '1':
            response = nameNode_stub.ListFiles(Service_pb2.Empty())
            print("Client received: " + ', '.join(response.files))

        elif choice == '2':
            file_name = input("Enter the name of the file to create: ")            
            # Open the file in read mode
            with open(f'files/{file_name}', 'r') as file:
                file_content = file.read()          
            file_data = Service_pb2.FileData(name=file_name, data=file_content)           
            response = nameNode_stub.CreateFile(file_data)
            print(response.message)

        elif choice == '3':
            while(True):
                file_name = input("Enter the name of the file")
                # check if the file exist
                action = input("Press 1 to read, 2 to write and 3 to return: ")
                if action == '1':
                    # Read logic
                    pass
                elif action == '2':
                    # Write logic
                    pass
                elif action == '3':
                    break
                else:   
                    print("Invalid choice. Please enter a number between 1 and 3")   

        elif choice == '4':
            # Call Close here
            pass
        elif choice == '5':
            # Call Read here
            pass
        elif choice == '6':
            # Call Write here
            pass
        elif choice == '7':
            break         
        else:
            print("Invalid choice. Please enter a number between 1 and 7")

if __name__ == '__main__':
    run()
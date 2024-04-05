import grpc
import os
import sys
import tempfile
import partitionManagement


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Protobufs import Service_pb2
from Protobufs import Service_pb2_grpc

# this dictionary will be in nameNode Class
dataNode_addresses = {
    "datanode_id1": "localhost:50052",
    "datanode_id2": "localhost:50053",
    "datanode_id3": "localhost:50054",
    "datanode_id4": "localhost:50055",
    "datanode_id5": "localhost:50056",
}

# Takes a DataNode address and returns a stub to communicate with that DataNode
def get_dataNode_stub(dataNode_id):
    dataNode_address = dataNode_addresses[dataNode_id]
    channel = grpc.insecure_channel(dataNode_address)
    stub = Service_pb2_grpc.DataNodeServiceStub(channel)
    return stub


def run():
    channel_nameNode = grpc.insecure_channel('localhost:50051') # Replace with the address of your nameNode Leader bootstrap
    nameNode_stub = Service_pb2_grpc.ClientServiceStub(channel_nameNode)
    #dataNode_stub = Service_pb2_grpc.DataNodeServiceStub(channel_dataNode)

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
            channel_dataNode = grpc.insecure_channel('localhost:50052') # Replace with the address of your nameNode Leader bootstrap
            dataNode_stub = Service_pb2_grpc.DataNodeServiceStub(channel_dataNode)
            file_name = input("Enter the name of the file to create: ")    

            # Open the file in read mode
            '''with open(f'files/{file_name}', 'r') as file:
                file_content = file.read()
            blocks = partitionManagement.file_partition(file_content)'''
            blocks = partitionManagement.file_partition(f'files/{file_name}')
            file_data = Service_pb2.FileInfo(name=file_name, num_blocks=len(blocks))        
            response = nameNode_stub.CreateFile(file_data)

            # Send each block to the DataNode
            for i, block in enumerate(blocks):
                block_data = Service_pb2.BlockData(id=block, data=f"{block} data")
                response = dataNode_stub.StoreBlock(block_data)
                print(response.message)
            # then delete the block's directory

        elif choice == '3':        
            while (True):
                file_name = input("Enter the name of the file: ")
                # check if the file exist
                action = input("Press 1 to read, 2 to write and 3 to return: ")
                if action == '1':
                    blocks = []
                    block_locations_map = nameNode_stub.GetBlockLocations(Service_pb2.FileName(name=file_name))                
                    # Create a temporary directory to store the blocks
                    with tempfile.TemporaryDirectory() as temp_dir:
                        print("pasa por aqui #2")
                        for block_locations in block_locations_map.locations:
                            print("pasa por aqui #3")
                            block_id = block_locations.block_id
                            dataNode_id = block_locations.dataNode_id
                            dataNode_stub = get_dataNode_stub(dataNode_id) # takes a DataNode address and returns a stub to communicate with that DataNode
                            block_request = Service_pb2.BlockId(id=block_id)                            
                            block = dataNode_stub.SendBlock(block_request)
                            # Write each block to a file in the temporary directory
                            with open(os.path.join(temp_dir, block_id), 'w') as block_file:
                                block_file.write(block.data)
                        # pass the temporary directory to join_partitioned_files
                        print("pasa por aqui #4")
                        file_data = partitionManagement.join_partitioned_files(temp_dir, f'reconstructed_{file_name}.txt')
                        print("pasa por aqui #5")
                        #print(file_data)
                
                elif action == '2':
                    
                    data_to_write = input("Enter the content to write to the file: ")
                    blocks = partitionManagement.file_partition(data_to_write)
                     # Solicitar al NameNode que cree el archivo y determine la ubicación de los bloques
                    try:
                        file_info = Service_pb2.FileInfo(name=file_name, num_blocks=len(blocks))
                        response = nameNode_stub.CreateFile(file_info)

                        if not response.success:
                            print(f"Failed to create file {file_name}: {response.message}")
                            continue

                        block_locations = nameNode_stub.GetBlockLocations(Service_pb2.FileName(name=file_name))

                    # Enviar cada bloque al DataNode correspondiente.
                        for block_data, block_location in zip(blocks, block_locations.locations):
                         # Asumiendo que get_dataNode_stub devuelve el stub correcto basado en el dataNode_id.
                            dataNode_stub = get_dataNode_stub(block_location.dataNode_id)
                            block_request = Service_pb2.BlockData(id=block_location.block_id, data=block_data)

                        # Almacenar el bloque en el DataNode.
                            store_response = dataNode_stub.StoreBlock(block_request)
                        if not store_response.success:
                            print(f"Failed to store block {block_location.block_id}: {store_response.message}")
                            break  # Salir del bucle si hay un error.
                        else:
                            print(f"Block {block_location.block_id} stored successfully.")
                    except grpc.RpcError as e:
                                print(f"Failed to write content to {file_name}: {e}")

        
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
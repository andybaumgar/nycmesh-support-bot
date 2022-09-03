import mesh_database_client
import os
from dotenv import load_dotenv

load_dotenv()

# spreadsheet_id = os.environ.get("SPREADSHEET_ID")
spreadsheet_id = os.environ.get("SPREADSHEET_ID_TEST")

database_client = mesh_database_client.DatabaseClient(spreadsheet_id=spreadsheet_id)

def test_name_to_nn():
    nn = database_client.name_to_nn("Heather Gibson")
    print(nn)
    assert nn==1612

def test_email_to_nn():
    nn = database_client.email_to_nn("Andrea.Gray@test.com")
    print(nn)
    assert nn == 2111

def test_address_to_nn():
    nn = database_client.address_to_nn("227 Madison St, Manhattan, NY 10002")
    print(f'nn:{nn}')
    assert nn == 3234

def test_nn_to_linked_nn():
    nodes = database_client.nn_to_linked_nn(2699)
    print(nodes)
    assert nodes == [844, 2090, 2645]

def test_nn_to_linked_nn_too_large():
    nodes = database_client.nn_to_linked_nn(100000)
    print(nodes)
    assert nodes == []

if __name__ == '__main__':
    test_address_to_nn()
from dnacentersdk import api 
import time

def my_main():

    my_dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac.cisco.com",
        username="devnetuser",
        password="Cisco123!",
        verify=False
    )

    new_device_dict ={
        "ipAddress": ["192.0.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetrry": 1,
        "snmpTimeout": 60,
        "cliTransport": "ssh",
        "userName": "champ",
        "password": "password123",
        "enablePassword": "password123"
    }

    add_data = my_dnac.devices.add_device(**new_device_dict)

    time.sleep(10)
    task = add_data["response"]["taskId"]
    task_data = my_dnac.task.get_task_by_id(task)

    if not task_data["response"]["isError"]:
        print("New device successfully added")
    else:
        print(f"Async task error seen: {task_data['progress']}")

my_main()
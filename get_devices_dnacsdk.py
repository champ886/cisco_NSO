from dnacentersdk import api 

def my_main():

    my_dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac.cisco.com",
        username="devnetuser",
        password="Cisco123!",
        verify=False
    )

    devices=my_dnac.devices.get_device_list()

    for device in devices["response"]:
        print(f"ID: {device['id']} IP: {device['managementIpAddress']}")


my_main()
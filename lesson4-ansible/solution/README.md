To run this solution:

1. Make sure `hosts` file contains hostnames which can be resolved.
You could either replace `host1` and `host2` by their respective IP addresses, or add them into SYSTEM hosts file on the ansible control node as follows:
```
192.168.10.101	host1
192.168.10.102	host2
```

2. Make sure `app.com` can be resolved on the machine used to test result of ansible play and point to correct hosts. This can be achieved via editing SYSTEM hosts file as follows:
```
192.168.10.101	app.com
```

3. Replace encrypted values for nexus repository variables if necessary

4. Run following command from ansible directory:
```sh
ansible-playbook site.yml -i hosts --ask-vault-pass
```

5. Check `http://app.com` is accessible and request to `http://app.com/api/` responds with 
```json
{"ping": "pong"}
```
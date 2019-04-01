# hooky
Call a webhook from a set of webhooks defined in a JSONfile via a command-line argument

# Requirements
 - Python 3

# Creating your controls.json
Your controls.json should look something like this:
```json
{"commands":[
        {
            "commandId": "example1",
            "hookUrl": "http://example.url"
        },
        {
            "commandId": "example2",
            "hookUrl": "http://example.url",
            "requestType": "GET"
        },
        {
            "commandId": "example3",
            "hookUrl": "http://example.url",
            "data": "some post data"
        },
         {
            "commandId": "example4",
            "hookUrl": "http://example.url",
            "data": "some post data",
            "requestType": "POST"
        }
    ]
}
```
The default method is POST, and only POST and GET are available. Data will be ignored on GET. You'd have to specify the get parameters in the URL.

# Usage
```bash
./hooky.py example1
```

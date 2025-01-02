import requests

# Presigned URL and fields (replace with actual values from the output)
url = "https://tempo-traces-bharat.s3.amazonaws.com/"
fields = {
    'key': 'test.txt',  # Name of the file to upload
    'AWSAccessKeyId': 'ASIA6GBMFOIBECQSB2EH',  # AWS Access Key ID
    'x-amz-security-token': 'FwoGZXIvYXdzEPL//////////wEaDFQudeXa5PSznrlsziKoASgX371Fms5OV+8vxPYwv+q1IFchRT3mcl1dBK8Vb+xj9+SWo6fOl3C8dDrMyN7UhSMmBEB/jajPTXkQ2+xHZnB7jUg4PRZHoT0Kf2bcNuAPB3+eWhBMrLsOyey6TCq8oCGUffzj8elR1fpXQya0H71UisZvLMLWkJueBNywpUaqRX+rTn1NUIicrdPd03eetcQhLBJjG86jmAqTvcdbB0so0fh+FokhdCjq/dO7BjItMlNwuPpi4uDIaSkb1Zik/gaIfdWuVEV9hNL2qScURre0uNd+O4g8H0BtT22Y',  # Security token
    'policy': 'eyJleHBpcmF0aW9uIjogIjIwMjUtMDQtMjdUMDI6MjQ6NDNaIiwgImNvbmRpdGlvbnMiOiBbeyJzdWNjZXNzX2FjdGlvbl9zdGF0dXMiOiAiMjAxIn0sIFsic3RhcnRzLXdpdGgiLCAiJGtleSIsICIiXSwgWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDM2ODYyNzIwXSwgeyJ4LWFtei1hbGdvcml0aG0iOiAiQVdTNC1ITUFDLVNIQTI1NiJ9LCB7ImJ1Y2tldCI6ICJ0ZW1wby10cmFjZXMtYmhhcmF0In0sIHsia2V5IjogInRlc3QudHh0In0sIHsieC1hbXotc2VjdXJpdHktdG9rZW4iOiAiRndvR1pYSXZZWGR6RVBMLy8vLy8vLy8vL3dFYURGUXVkZVhhNVBTem5ybHN6aUtvQVNnWDM3MUZtczVPVis4dnhQWXd2K3ExSUZjaFJUM21jbDFkQks4VmIreGo5K1NXbzZmT2wzQzhkRHJNeU43VWhTTW1CRUIvamFqUFRYa1EyK3hIWm5CN2pVZzRQUlpIb1QwS2YyYmNOdUFQQjMrZVdoQk1yTHNPeWV5NlRDcThvQ0dVZmZ6ajhlbFIxZnBYUXlhMEg3MVVpc1p2TE1MV2tKdWVCTnl3cFVhcVJYK3JUbjFOVUlpY3JkUGQwM2VldGNRaExCSmpHODZqbUFxVHZjZGJCMHNvMGZoK0Zva2hkQ2pxL2RPN0JqSXRNbE53dVBwaTR1RElhU2tiMVppay9nYUlmZFd1VkVWOWhOTDJxU2NVUnJlMHVOZCtPNGc4SDBCdFQyMlkifV19',  # Policy
    'signature': 'xs64Hi202QyqOavOb2ALR4MgiqY=',  # Signature
    'success_action_status': '201',  # Explicitly set to match the policy
    'x-amz-algorithm': 'AWS4-HMAC-SHA256'  # Ensure the correct algorithm is specified
}

# Open the file to upload (make sure the path is correct)
with open('test.txt', 'rb') as file:
    # Send POST request with file and fields
    response = requests.post(url, data=fields, files={'file': file})

    # Check response status
    if response.status_code == 201:
        print("File uploaded successfully!")
    else:
        print(f"Upload failed, status code: {response.status_code}")
        print(response.text)

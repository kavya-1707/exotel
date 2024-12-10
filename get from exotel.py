import json

def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")
    call_from = event.get('queryStringParameters', {}).get('CallFrom')
    call_sid = event.get('queryStringParameters', {}).get('CallSid')
    print(f"CallFrom: {call_from}")
    print(f"CallSid: {call_sid}")
    
    response = {
        'statusCode': 200,
        'body': json.dumps({
            'CallFrom': call_from,
            'CallSid': call_sid
        })
    }

    # Print the response for debugging purposes
    print(f"Response: {json.dumps(response)}")

    # Return the response
    return response

def safe_json_parse(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"[ERROR] - Failed to parse JSON: {e}")
        return None

# Lambda 3 (Filtering_low_confidence)
import json

THRESHOLD = 0.93  # Corrected the THRESHOLD value to be a float (0.93)

def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = event.get("inferences", [])  # Fill in to retrieve 'inferences' from the event

    # Check if any values in our inferences are above THRESHOLD
    
    meets_threshold = any(i > THRESHOLD for i in inferences)  # Fill in to calculate if any value exceeds the threshold
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise ValueError("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
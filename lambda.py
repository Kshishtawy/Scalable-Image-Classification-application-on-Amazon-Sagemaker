# Lambda 1 (serializeImageData)
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    s3.download_file(bucket, key, '/tmp/image.png')
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
#_______________________________

# Lambda 2 (classifying image)
import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer
from sagemaker.predictor import Predictor

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-10-26-02-28-01-181'  # TODO: fill in your endpoint name

def lambda_handler(event, context):

    # Decode the image data
    image_data = base64.b64decode(event['image_data'])  # TODO: fill in the key used for image data in your event

    # Instantiate a Predictor
    predictor = Predictor(endpoint_name=ENDPOINT, sagemaker_session=sagemaker.Session())

    # For this model, the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image_data)

    # We return the data back to the Step Function    
    event['inferences'] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': {
            "info_data": json.dumps(event),
            "inferences": json.loads(event['inferences'])
        }
    }

#_______________________________

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
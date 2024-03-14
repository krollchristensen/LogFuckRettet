import logging
import json

# Tilpasser logging til at bruge struktureret format (JSON)
class StructuredMessage:
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return json.dumps({"message": self.message, **self.kwargs})

def setup_logger():
    logger = logging.getLogger()
    handler = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(message)s')  # Kun brugerdefinerede beskeder
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()

def handle_request(user_id, request_data):
    # Anonymiserer eller fjerner følsomme data før logging
    if "credit_card_number" in request_data:
        request_data = "{operation: 'purchase'}"  # Anonymiseret eksempel

    logger.info(StructuredMessage("Handling request", user_id=user_id, request_data=request_data))

    try:
        # Simulerer en operation, der kan fejle
        result = "Operation successful"
        logger.info(StructuredMessage("Operation result", user_id=user_id, result=result))
    except Exception as e:
        logger.error(StructuredMessage("Error during operation", user_id=user_id, error=str(e)))

def main():
    user_requests = [("user123", "{credit_card_number: '1234-5678-9012-3456', operation: 'purchase'}"),
                     ("user456", "{operation: 'check_balance'}")]

    for user_id, request_data in user_requests:
        handle_request(user_id, request_data)

if __name__ == "__main__":
    main()

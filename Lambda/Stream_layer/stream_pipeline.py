import time
import threading
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def producer_thread():
    while True:
        try:
            file_path = '../Stream_data/stream_data.csv'
            message = generate_real_time_data(file_path)

            send_message(message)
            print("Message sent to Kafka topic")

            # Sleep for 5 seconds before collecting and sending the next set of data
            time.sleep(5)

        except Exception as e:
            print(f"Error in producer_thread: {str(e)}")


def consumer_thread():
    while True:
        try:
            # Simulate message consumption
            message = consum()  # Replace with actual Kafka or queue consumer function
            if message:
                logging.info(f"Consumed message: {message}")

                # Simulate message parsing and processing
                try:
                    data = json.loads(message)
                except json.JSONDecodeError:
                    logging.warning("Received non-JSON message, skipping.")
                    continue

                # Example of processing logic
                value = data.get("value", random.randint(1, 100))
                timestamp = data.get("timestamp", str(datetime.datetime.now()))
                
                # Simulated computation or transformation
                processed_value = round(value * random.uniform(0.8, 1.2), 2)
                logging.info(f"Processed value: {processed_value} at {timestamp}")

            else:
                logging.debug("No new messages available.")
            
        except Exception as e:
            logging.error(f"Error in consumer_thread: {str(e)}")
            traceback.print_exc()
            time.sleep(2)  # Prevent tight error loop            
        
            
            

# Create separate threads for producer and consumer
producer_thread = threading.Thread(target=producer_thread)
consumer_thread = threading.Thread(target=consumer_thread)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish (which will never happen in this case as they run infinitely)
producer_thread.join()
consumer_thread.join()














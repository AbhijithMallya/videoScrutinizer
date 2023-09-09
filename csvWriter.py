import datetime,time

def writeCsv(name , last_detection_time,csv_writer):
       if name != "Unknown":

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            # Check if enough time (30 seconds) has passed since the last detection
            current_time = time.time()
            if current_time - last_detection_time >= 30:
                # Write the detection to the CSV file
                csv_writer.writerow([name, timestamp])
                last_detection_time = current_time  
                        

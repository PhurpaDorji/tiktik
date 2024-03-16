from queue import Queue

#Initilaize queue for patient registration
patient_queue = Queue()

#function to register a new patient
def register_patient():
    name = input("Enter patient's name: ")
    patient_queue.put(name)
    print("Patient registered successfully.")

#Function to femove a patient after meeting the doctor
def remove_patient():
    if patient_queue.empty():
        print("Patient queue is empty.")
    else:
        removed_patient = patient_queue.get()
        print(f"Patient {removed_patient} removed after meeting the doctor.")

        #Function to display the current patient queue
        def display_queue():
            if patient_queue.empty():
                print("Patient queue is empty.")
            else:
                print("\ncurrent Patient Queue:")
                for index, patient in enumerate(list(patient_queue.queue), start=1):
                    print(f"{index}. {patient}")

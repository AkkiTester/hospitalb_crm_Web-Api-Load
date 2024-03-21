import json
import threading


class ReportData3:
    def __init__(self, report_name="report_data.json"):
        self.report_name = report_name
        self.data = {}
        self.lock = threading.Lock()  # Create a lock for thread safety
        self._load_existing_data()

    def _load_existing_data(self):
        """Loads existing data from the JSON file (if it exists) without duplicates."""
        try:
            with open(self.report_name, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}  # Create an empty dict if file doesn't exist

    def set_test_case_name(self, test_name):
        self.current_test_name = test_name
        try:
            with self.lock:  # Acquire lock for thread safety
                self.data.pop(test_name)  # Remove existing data if present
        except KeyError:
            pass  # Ignore missing key
        self.data[test_name] = []

    def set_test_case_log(self, log_type, log_message):
        if self.current_test_name:
            with self.lock:  # Acquire lock for thread safety
                self.data[self.current_test_name].append({"log_type": log_type, "log_message": log_message})
            self._write_data_to_json()  # Write data immediately after logging

    def set_test_result(self, result: bool):
        if self.current_test_name:
            with self.lock:  # Acquire lock for thread safety
                self.data[self.current_test_name + "Result"] = result
            self._write_data_to_json()  # Write data immediately after setting result

    def _write_data_to_json(self):
        """Writes the updated data to the JSON file with thread safety."""
        with self.lock:  # Acquire lock for thread safety
            with open(self.report_name, "w") as f:
                json.dump(self.data, f, indent=4)


# Example usage:
report_data = ReportData3()

# Test case 1
report_data.set_test_case_name("Test1")
report_data.set_test_case_log("INFO", "Checking Log")
report_data.set_test_case_log("INFO", "Another Log Message")
report_data.set_test_result(True)



# Test case 2 (no duplicates)
report_data.set_test_case_name("Test2")
report_data.set_test_case_log("WARNING", "Something might go wrong")
report_data.set_test_result(False)

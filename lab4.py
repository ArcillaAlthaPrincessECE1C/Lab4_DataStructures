import array
from collections import deque, defaultdict

# Student Identity
LAST_NAME = "Arcilla"  
STUDENT_ID = "TUPM-26-1087"  

# Derive computational parameters[span_0](start_span)[span_0](end_span)
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

# Encapsulate state into a Dictionary (Associative Map)[span_1](start_span)[span_1](end_span)
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

# Display system state[span_2](start_span)[span_2](end_span)
print("=== SYSTEM CONFIGURATION ===")
for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")

# Task 5: Dynamic List Operations[span_0](start_span)[span_0](end_span)
base_val = sys_config["base_seed"]
number_sequence = [base_val, base_val + 15, sys_config["checksum"]]
print(f"\nInitial Sequence: {number_sequence}")

number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")

# Task 6: Sequential Operations[span_1](start_span)[span_1](end_span)
new_numbers = [base_val + 5, sys_config["vector_dim"], base_val]
number_sequence.extend(new_numbers)
print(f"After Extend: {number_sequence}")

base_count = number_sequence.count(base_val)
print(f"Occurrences of {base_val}: {base_count}")

number_sequence.sort()
print(f"Sorted Sequence: {number_sequence}")

# Task 7: Immutable Sequences (Tuples)[span_2](start_span)[span_2](end_span)
fixed_coordinates = (sys_config["vector_dim"], sys_config["base_seed"], 0)
print(f"\nFixed Coordinates: {fixed_coordinates}")

x_val, y_val, z_val = fixed_coordinates
print(f"Unpacked Values -> X: {x_val}, Y: {y_val}, Z: {z_val}")

print("\nAttempting modification...")
try:
    fixed_coordinates[0] = 99
except TypeError as error_msg:
    print(f"Modification Error: {error_msg}")

# Task 8: Key-Value Mappings (Dictionaries)[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)
data_payload = {
    "identifier": sys_config["auth_id"],
    "dimension": sys_config["vector_dim"],
    "status": "active"
}

print("--- Payload Data ---")
for key, value in data_payload.items():
    print(f"{key.capitalize()}: {value}")

data_payload["efficiency_rating"] = 98.5
print(f"\nUpdated Payload: {data_payload}")

# Task 9: Data De-duplication[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)
base_val = sys_config["base_seed"]
raw_data = [base_val, base_val + 5, base_val, sys_config["vector_dim"], base_val + 5]
print(f"\nRaw List (with duplicates): {raw_data}")

unique_data = set(raw_data)
print(f"Unique Set: {unique_data}")

# Task 10: Mathematical Set Operations[span_7](start_span)[span_7](end_span)
reference_set = {base_val, base_val + 10, base_val + 20}
print(f"Reference Set: {reference_set}")

common_elements = unique_data.intersection(reference_set)
combined_elements = unique_data.union(reference_set)

print(f"Intersection (Common): {common_elements}")
print(f"Union (Combined): {combined_elements}")

# Task 11: Homogeneous Arrays[span_8](start_span)[span_8](end_span)
number_array = array.array('i', [sys_config["base_seed"], sys_config["vector_dim"], 100])
print(f"\nInteger Array: {number_array}")

print("\nAttempting to append a string...")
try:
    number_array.append("invalid")
except TypeError as error_msg:
    print(f"Type Error: {error_msg}")

# Task 12: List Comprehensions[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)
base_val = sys_config["base_seed"]
generated_list = [(x * base_val) for x in range(1, 6)]
print(f"Generated Comprehension: {generated_list}")

filtered_list = [x for x in generated_list if x > 15]
print(f"Filtered Comprehension (Values > 15): {filtered_list}")

# Task 13: Double-Ended Queues (Deque)[span_11](start_span)[span_11](end_span)
data_queue = deque([sys_config["base_seed"], sys_config["vector_dim"]])
print(f"\nInitial Deque: {data_queue}")

data_queue.append(100)
data_queue.appendleft(200)
print(f"After Appends: {data_queue}")

data_queue.popleft()
print(f"Final Deque (After Popleft): {data_queue}")

# Task 14: Fault-Tolerant Key Mappings (Defaultdict)[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span)
default_data = defaultdict(int)
default_data['active_key'] = sys_config["vector_dim"]

print(f"\nExisting Key Value: {default_data['active_key']}")
print(f"Missing Key Value (Auto-generated): {default_data['unknown_key']}")
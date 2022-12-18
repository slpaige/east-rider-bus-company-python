import json

# Write your code here
json = json.loads(input())

total_errors = 0
bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0

for route in json:
    if not isinstance(route["bus_id"], int):
        bus_id += 1

    if not isinstance(route["stop_id"], int):
        stop_id += 1

    if not isinstance(route["stop_name"], str) or route["stop_name"] == "":
        stop_name += 1

    if not isinstance(route["next_stop"], int):
        next_stop += 1

    if not isinstance(route["stop_type"], str) or len(route["stop_type"]) > 1:
        stop_type += 1

    if not isinstance(route["a_time"], str) or route["a_time"] == "":
        a_time += 1

print(f"Type and required field validations: {bus_id + stop_id + stop_name + next_stop + stop_type + a_time} errors")
print(f"bus_id: {bus_id}")
print(f"stop_id: {stop_id}")
print(f"stop_name: {stop_name}")
print(f"next_stop: {next_stop}")
print(f"stop_type: {stop_type}")
print(f"a_time: {a_time}")

data = (1, (0.5385981514616195, 0.3226315593708624, 0.14130763384267375, 0.18364212554983866))

# Unpack the tuple
class_id, bbox = data

# Combine class ID and bounding box coordinates into a single list
combined_list = [class_id] + list(bbox)

print(combined_list)
0
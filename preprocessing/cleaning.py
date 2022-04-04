import numpy as np

labels = [
    "Number of bedrooms",
    "Livable surface",
    "Balcony",
    "Surface bedroom 1",
    "Furnished",
    "Surface of living-room",
    "Cellar",
    "Surface kitchen",
    "Number of facades",
    "Terrace",
    "Surface terrace",
    "Garden",
    "Surface garden",
    "Garage",
    "Kitchen equipment_Fully equipped",
    "Kitchen equipment_Not equipped",
    "Kitchen equipment_Partially equipped",
    "Kitchen equipment_Super equipped",
    "State of the property_Excellent",
    "State of the property_Fully renovated",
    "State of the property_New",
    "State of the property_Normal",
    "State of the property_To be renovated",
    "Type of property_flat",
    "Type of property_house",
]


def cleaning_by_key(data, key, details):
    type_, default = details
    if data:
        try:
            return type_(data)
        except:
            print(
                f"The data for {key} ({data}) is not in the right format (expected {type_})"
            )
    else:
        return default


label_details = {
    "Number of bedrooms": (int, 1),
    "Livable surface": (float, 100),
    "Balcony": (bool, False),
    "Surface bedroom 1": (float, 20),
    "Furnished": (bool, False),
    "Surface of living-room": (float, 50),
    "Cellar": (bool, False),
    "Surface kitchen": (float, 20),
    "Number of facades": (int, 2),
    "Terrace": (bool, False),
    "Surface terrace": (float, 0),
    "Garden": (bool, False),
    "Surface garden": (bool, 0),
    "Garage": (bool, False),
    "Kitchen equipment": (str, "Not equipped"),
    "State of the property": (str, "Normal"),
    "Type of property": (str, "Flat"),
}


def cleaning(data):
    for key in data:
        data[key] = cleaning_by_key(data[key], key, label_details[key])
    undefined_keys = [
        key for key in label_details.keys() if key not in data.keys()
    ]
    for key in undefined_keys:
        data[key] = cleaning_by_key(None, key, label_details[key])


one_hot_labels = [
    "Kitchen equipment_Fully equipped",
    "Kitchen equipment_Not equipped",
    "Kitchen equipment_Partially equipped",
    "Kitchen equipment_Super equipped",
    "State of the property_Excellent",
    "State of the property_Fully renovated",
    "State of the property_New",
    "State of the property_Normal",
    "State of the property_To be renovated",
    "Type of property_flat",
    "Type of property_house",
]


def one_hot_helper(data, key, label):
    quality = data[label].upper()
    if quality in key.upper():
        data[key] = 1
    else:
        data[key] = 0


def one_hot(data):
    for key in one_hot_labels:
        if "Kitchen" in key:
            one_hot_helper(data, key, "Kitchen equipment")
        elif "State" in key:
            one_hot_helper(data, key, "State of the property")
        elif "Type" in key:
            one_hot_helper(data, key, "Type of property")


def data_to_array(data):
    return np.array([[data[key] for key in labels]])

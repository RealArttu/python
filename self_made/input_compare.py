
def compare_input():

    original_data = input("Enter original data to compare with yours: ")
    own_data = input("Enter own data to compare with the original data: ")

    if original_data != own_data:
        print("Original data and own data do not match " + str(original_data) + " and " + str(own_data))
        return False
    elif original_data == own_data:
        print("Original data and own data match " + str(original_data)  + " and " + str(own_data))

compare_input()
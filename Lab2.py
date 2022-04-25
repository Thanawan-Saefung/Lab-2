def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    num_list = []
    string = input()
    num_list = (string.split(","))
    num_list = [int(i) for i in num_list]
    return num_list

def calc_average(num_list):
    calc_average = sum(num_list)/len(num_list)
    return calc_average

def find_min_max(num_list):
    value = []
    value.append(min(num_list))
    value.append(max(num_list))
    return value

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    avg=calc_average(num_list)
    print("Average of the temperature is ", avg)
    min=find_min_max(num_list)[0]
    max=find_min_max(num_list)[1]
    print("Minimum value is ",min)
    print("Maximum value is ",max)

if __name__ == "__main__":
    main()
import csv
import matplotlib.pyplot as graph_tool

def load_csv_file_into_2d_array():
    two_dimensional_array = []

    # read from the csv file
    with open('graph_points.csv', newline='') as csv_file:
        file_data = csv.reader(csv_file)
        for row in file_data:
            x_coordinate = int(row[0]) # convert the data we are reading to an int/number type
            y_coordinate = int(row[1]) # convert the data we are reading to an int/number type
            point = [x_coordinate, y_coordinate] # store the coordinates in an array
            two_dimensional_array.append(point) # save the coordinates as array inside of an array to fulfill the 2D array requirement
            
    return two_dimensional_array

def graph_points_in_2d_array(two_dimensional_array):
    graph_tool.title("Graph from 2D Array")
    graph_tool.xlabel("X Axis")
    graph_tool.ylabel("Y Axis")
        
    for point in two_dimensional_array:
        x_coordinate = point[0]
        y_coordinate = point[1]
        graph_tool.scatter(x_coordinate, y_coordinate) # we are placing the point on the graph here

    graph_tool.savefig("graph_output.png") # we are saving the graph as an image here

# Here we call our code to execute it!
two_dimensional_array = load_csv_file_into_2d_array()
graph_points_in_2d_array(two_dimensional_array)

# Project Details
1. Open a csv file, make sure it stores values that can be graphed
2. Read all of the data stored in it and move it into a 2-D array, make sure any numerical data is converted into the proper type
3. Graph the data from the file
4. Export the graph into an image, could be png or jpg
5. Save the data from the 2-D array and the graph image into a new excel

## 1. Open a csv file, make sure it stores values that can be graphed
For this step I will manually create a very simple csv with three points (x and y coordinates). See the ```graph_points.csv``` file in this repository.

```
1,1
2,2
3,3
```

## 2. Read all of the data stored in it and move it into a 2-D array, make sure any numerical data is converted into the proper type
See the python scipt ```solution.py``` in this repository, below I pasted a code snippet from the script that does this step.

```python
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
```

## 3. Graph the data from the file
## 4. Export the graph into an image, could be png or jpg
I did steps 3 and 4 in the same code snippet. It was not clear in the instruction on how to "graph" the data from the file. If you worked with a graphing library in previous assignments, I would use that - get clarity on this requirement with the instructor. For the purpose of this example, I will use a graphing library called ```matplotlib```. First you need to install this library on your machine, I am using python 3 on my machine so I installed with the following command ```python3 -m pip install matplotlib```. Once installed, you can use this library in your code - I pasted a code snippet where I use this library to achieve our goal.

```python
import matplotlib.pyplot as graph_tool

def graph_points_in_2d_array(two_dimensional_array):
    graph_tool.title("Graph from 2D Array")
    graph_tool.xlabel("X Axis")
    graph_tool.ylabel("Y Axis")
        
    for point in two_dimensional_array:
        x_coordinate = point[0]
        y_coordinate = point[1]
        graph_tool.scatter(x_coordinate, y_coordinate) # we are placing the point on the graph here

    graph_tool.savefig("graph_output.png") # we are saving the graph as an image here
```

## 5. Save the data from the 2-D array and the graph image into a new excel
I'll let you work through this last step :). It is not clear in the instruction if this has to be done via python or if this can be done manually - check with the instructor to understand this requirement.

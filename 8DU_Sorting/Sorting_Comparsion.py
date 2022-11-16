import time
import random
import os.path
import matplotlib.pyplot as plt

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        ret = func(*args,**kwargs)
        stop = time.time()
        #print(f"Elapsed time: {stop - start}")
        return ret, stop - start
    return inner

@calculate_time
def selection_sort(array):
    data = array.copy()
    size = len(data)
    for step in range(size):
        min_index = step

        for i in range(step, size):
            if data[i] < data[min_index]:
                min_index = i
        data[step], data[min_index] = data[min_index], data[step]
    return data

@calculate_time
def bubble_sort(array):
    data = array.copy()
    size = len(data)

    for i in range(size):
        swapped = False
        for j in range(size-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break

    return data

def merge_sort(data):
    if len(data) > 1:
        r = len(data)//2

        left = data[:r]
        right = data[r:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i = i + 1
            else:
                data[k] = right[j]
                j = j + 1

            k = k + 1

        while i < len(left):
            data[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            data[k] = right[j]
            j = j + 1
            k = k + 1

    return data

@calculate_time
def calling_merge_sort(array):
    data = array.copy()
    return merge_sort(data)

if __name__ == "__main__":
    number_of_tests = 500
    
    #check for result file
    if not os.path.exists("results.txt"):
    
        selection_time = [None]*number_of_tests
        bubble_time = [None]*number_of_tests
        merge_time = [None]*number_of_tests
        
        for test in range(number_of_tests):
            print(f"test#{test} is running")
            number_of_elements_in_test = test*10
            array = ([random.randint(-10000,10000) for i in range(number_of_elements_in_test)])
            
            sorted_selection    = selection_sort(array)
            selection_time[test] = sorted_selection[1]
            
            sorted_bubble       = bubble_sort(array)
            bubble_time[test] = sorted_bubble[1]
            
            sorted_merge        = calling_merge_sort(array)
            merge_time[test] = sorted_merge[1]
        
        file = open("results.txt", "w")
        
        #writing selection algorithm times
        file.write('Selection: ')
        for time in selection_time:
            file.write(str(time).rstrip('\n')+", ")
        file.write("\n")
        #writing bubble algorithm times
        file.write('Bubble: ')
        for time in bubble_time:
            file.write(str(time).rstrip('\n')+", ")
        file.write("\n")
        #writing merge algorithm times
        file.write('Merge: ')
        for time in merge_time:
            file.write(str(time).rstrip('\n')+", ")
        
        file.close()

    if os.path.exists("results.txt"):
        file = open("results.txt", "r")
        all_data = file.readlines()
        
        selection_sort_data = all_data[0]
        selection_sort_data = selection_sort_data[11:]
        selection_sort_data = selection_sort_data.split(', ')[:-1]
        selection_sort_data = [float(x) for x in selection_sort_data]
        
        bubble_sort_data = all_data[1]
        bubble_sort_data = bubble_sort_data[8:]
        bubble_sort_data = bubble_sort_data.split(', ')[:-1]
        bubble_sort_data = [float(x) for x in bubble_sort_data]
        
        merge_sort_data = all_data[2]
        merge_sort_data = merge_sort_data[7:]
        merge_sort_data = merge_sort_data.split(', ')[:-1]
        merge_sort_data = [float(x) for x in merge_sort_data]
        
        X = [i*10 for i in range(number_of_tests)]
        
        plt.plot(X,selection_sort_data)
        plt.plot(X,bubble_sort_data)
        plt.plot(X,merge_sort_data)
        
        plt.legend(["Selection sort","Bubble sort","Merge sort"])
        plt.xlabel("Amount of list's elements")
        plt.ylabel("Processing time")
        plt.title("Comparsion of sorting algorithms")
        
        #plt.show()
        
        
        
        selection_sort_bar_data = [None]*249
        bubble_sort_bar_data = [None]*249
        merge_sort_bar_data = [None]*249
        
        for i in range(249):
        
            selection_sort_bar_data[i] = [[i*200+100],[selection_sort_data[ (i)*20 : (i+1)*20 ]]]
            bubble_sort_bar_data[i] = [[i*200+100],[bubble_sort_data[ (i)*20 : (i+1)*20 ]]]
            merge_sort_bar_data[i] = [[i*200+100],[merge_sort_data[ (i)*20 : (i+1)*20 ]]]
            
            plt.boxplot(selection_sort_bar_data[i][1], positions = selection_sort_bar_data[i][0], widths = 50)
            plt.boxplot(bubble_sort_bar_data[i][1], positions = bubble_sort_bar_data[i][0], widths = 50)
            plt.boxplot(merge_sort_bar_data[i][1], positions = merge_sort_bar_data[i][0], widths = 50)
            plt.xlim([0,4990])
        plt.savefig('sorting.png')
        plt.show()
        

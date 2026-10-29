import numpy as np

def create_array_from_list():
    return np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def create_array_with_arrange():
    return np.arange(1, 11)

def describe_array(arr):
    print("Array:", arr)
    print("Data type:", arr.dtype)
    print("Shape:", arr.shape)
    print("Dimensions:", arr.ndim)
    print("Size:", arr.size)

if __name__ == "__main__":
    arr1 = create_array_from_list()
    arr2 = create_array_with_arrange()

    print("Array created using list:")
    describe_array(arr1)

    print("\nArray created using arange:")
    describe_array(arr2)

    print("\nArrays are equal:", np.array_equal(arr1, arr2))

    print("\nVectorized Operations:")
    print("Array * 2:", arr1 * 2)
    print("Array + 100:", arr1 + 100)
    print("Sum:", arr1.sum())
    print("Mean:", arr1.mean())

    print("\nIndexing and Slicing:")
    print("First element:", arr1[0])
    print("Last element:", arr1[-1])
    print("First five elements:", arr1[:5])
    print("Every second element:", arr1[::2])

    print("\nArray from 1 to 20:")
    arr3 = np.arange(1, 21)
    describe_array(arr3)

#!/usr/bin/env python3

class CountedIterator:
    """
    A custom iterator that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable and a counter.

        Args:
            iterable: The iterable object to iterate over.
        """
        self.iterator = iter(iterable)  # Create an iterator from the iterable
        self.count = 0  # Initialize the counter

    def __next__(self):
        """
        Returns the next item from the iterator and increments the counter.

        Raises:
            StopIteration: If there are no more items to iterate.

        Returns:
            The next item from the iterator.
        """
        try:
            item = next(self.iterator)  # Get next item from original iterator
            self.count += 1  # Increment the counter
            return item
        except StopIteration:
            raise  # Re-raise StopIteration if original iterator is exhausted

    def get_count(self):
        """
        Returns the current value of the counter.

        Returns:
            The number of items iterated over so far.
        """
        return self.count  # Return the current value of the counter


if __name__ == "__main__":
    # Example usage:
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")

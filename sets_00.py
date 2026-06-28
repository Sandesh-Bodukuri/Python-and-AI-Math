if __name__ == '__main__':
    # Read the number of elements (not strictly needed for the calculation)
    n = int(input())
    
    # Read the space-separated scores and convert them into a list of integers
    scores = list(map(int, input().split()))
    
    # 1. Remove duplicates by converting the list to a set
    unique_scores = set(scores)
    
    # 2. Remove the maximum score from the unique set
    unique_scores.remove(max(unique_scores))
    
    # 3. The new maximum of the remaining elements is the runner-up score
    print(max(unique_scores))

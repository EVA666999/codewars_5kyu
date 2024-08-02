def queue_time(customers, n): # costumers время клиентов на обслуживание, n количество кас 
    result = [0] * n
    for i in customers:
        min_index = result.index(min(result))
        result[min_index] += i
    return max(result)
 
print(queue_time(customers=[2, 3, 10], n=2))
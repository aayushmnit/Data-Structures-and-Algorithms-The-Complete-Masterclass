def run(n):
    if n ==0:
        return 0
    print(n)
    run(n-1)
    

n=3
run(n)
print("Completed")


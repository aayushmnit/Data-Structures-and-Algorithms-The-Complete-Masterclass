def recursion(count):
    if count == 500: ## Base case 
        return 0
    else:
        print(count,R"Hello World")
        recursion(count+1) ## Calling itself

recursion(0)
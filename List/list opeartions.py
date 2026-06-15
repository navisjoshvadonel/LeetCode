if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        command_arg = input().split()
        command = command_arg[0]
        
        if command =="insert":
            index = int(command_arg[1])
            element = int(command_arg[2])
            result.insert(index,element)
        elif command =="print":
            print(result)
        elif command == "remove":
            element = int(command_arg[1])
            result.remove(element)
        elif command == "append":
            element = int(command_arg[1])
            result.append(element)
        elif command == "sort":
            result.sort()
        elif command =="pop":
            result.pop()
        elif command =="reverse":
            result.reverse()
                    
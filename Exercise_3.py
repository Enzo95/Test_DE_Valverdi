def sleeping_sheep(file_name):
    """
        This function uses a file as input, to determinate in whats number the sheep sleep.

        Parameters:

        file_name = file type .in
    """
    f = open(file_name)
    file = f.read().split('\n')
    T = int(file[0])
    Ns = list()
    check = ['0','1','2','3','4','5','6','7','8','9']

    for number in range(1,T+1):
        Ns.append(int(file[number]))

    for N in Ns:

        digits = list()
        i = 1

        while i <= 300:
            number = N * i
            number_str = list(str(number))

            for x in number_str:
                if x not in digits:
                    digits.append(x)
            digits.sort()
            if digits == check:
                break
            else:
                i += 1
                
        if digits == check:
            print(f"Case #{Ns.index(N)+1}: {number}")
        else:
            print(f"Case #{Ns.index(N)+1}: INSOMNIA")

if __name__ == "__main__":

    sleeping_sheep('c-input.in')
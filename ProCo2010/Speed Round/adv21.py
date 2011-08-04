import sys
if __name__ == '__main__':
    nums=sys.stdin.read().split('\n')
    num1=nums[0]
    num2=nums[1]
    for i in range(len(num1)):
        sys.stdout.write(str((int(num1[i])+int(num2[i]))%10))
    sys.stdout.write('\n')
    sys.stdout.flush()
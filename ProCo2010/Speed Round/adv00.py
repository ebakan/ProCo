import sys
if __name__ == '__main__':
    nums = sys.stdin.read().split()
    sys.stdout.write(str(int(nums[1])-int(nums[0])+1))
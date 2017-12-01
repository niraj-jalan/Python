import sys

sys.setrecursionlimit(2 * 10 ** 5)


class BearHairCut:
    def main(argv=None):
        for t in range(int(input())):
            n_spcl_days, start_day, end_day = map(int, input().split())
            spcl_days = list(map(int, input().split()))

            dp_array = []
            dp_array.append(0)
            t = []
            t.append(1);

            max_spcl_day = max(spcl_days)
            min_spcl_day = min(spcl_days)

            # print(max_spcl_day)
            for i in range(1, max_spcl_day + 2):
                dp_array.append(0);

            for i in range(1, max_spcl_day + 1):
                t.append(0)

            for i in spcl_days:
                # print(i)
                t[i] = 1

            for i in range(0, max_spcl_day + 1):
                # print('i = %s'%i)
                if i >= 1:
                    dp_array[i] = max(dp_array[i], dp_array[i - 1])

                cnt = 0;
                for j in range(i + start_day, min(i + end_day + 1, max_spcl_day + 1)):
                    # print(j)
                    if t[j] == 1:
                        cnt = cnt + 1
                    dp_array[j] = max(dp_array[j], dp_array[i] + cnt)

            dp_array[max_spcl_day + 1] = max(dp_array[max_spcl_day + 1], dp_array[max_spcl_day]);
            print(dp_array[max_spcl_day + 1])


bear_haircut = BearHairCut()
bear_haircut.main()


def fibonacci(n, history):
    if n <= 1:
        return 1
    elif n in history:
        return history[n]
    else:
        fib = fibonacci(n - 1, history) + fibonacci(n - 2, history)
        history[n] = fib
        print(fib, end=',')
        return fib


def calc_ways_2_climb(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return calc_ways_2_climb(n - 1) + calc_ways_2_climb(n - 2) + calc_ways_2_climb(n - 3)


# print(calc_ways_2_climb(3))
print(1, end=',')
fibonacci(30, history={})

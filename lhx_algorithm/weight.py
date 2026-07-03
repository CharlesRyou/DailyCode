def dfs(n, k, recover):
    isrecover = "取反" if recover == -1 else ""
    print(f"等价于找第 {n} 个字符串编号为 {k} 的字符颜色{isrecover};")
    if n == 1:
        if recover == 1:
            return "R"
        else:
            return "B"

    if k <= (2 ** (n - 2)) - 1:
        return dfs(n - 1, k, recover * -1)
    else:
        return dfs(n - 1, k - 2 ** (n - 2), recover)

def weight():
    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))
    print(f"开始回溯第 {n} 个字符串编号为 {k} 的字符颜色")
    result = dfs(n, k, 1)
    print(f"第 {n} 个字符串编号为 {k} 的字符颜色是: {result}")

if __name__ == "__main__":
    weight()

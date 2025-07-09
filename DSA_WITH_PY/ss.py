class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

bst = BST()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.inorder(bst.root)











def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)



















class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
visited = set()
g.dfs(1, visited)










class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def print_graph(self):
        for row in self.graph:
            print(row)

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.print_graph()






def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

weights = [1, 2, 3, 8, 7, 4]
values = [20, 5, 10, 40, 15, 25]
capacity = 10
print(knapsack(weights, values, capacity))







import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(dijkstra(graph, 'A'))






class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

trie = Trie()
trie.insert("hello")
trie.insert("world")
print(trie.search("hello"))
print(trie.search("world"))
print(trie.search("python"))











def is_safe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    if solve(board):
        for row in board:
            print(row)
    else:
        print("No solution exists")

main()











#1
def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def main():
    n = 4
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve(board, 0, n):
        for row in board:
            print(row)
    else:
        print("Solution does not exist")

main()











#2
def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]

def main():
    string = list("ABCD")
    permute(string, 0, len(string) - 1)

main()








#3
def subsets(nums, start, current, result):
    result.append(current[:])
    for i in range(start, len(nums)):
        current.append(nums[i])
        subsets(nums, i + 1, current, result)
        current.pop()

def main():
    nums = [1, 2, 3]
    result = []
    subsets(nums, 0, [], result)
    print(result)

main()




#4
def combination_sum(candidates, target, start, current, result):
    if target == 0:
        result.append(list(current))
        return
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            continue
        current.append(candidates[i])
        combination_sum(candidates, target - candidates[i], i, current, result)
        current.pop()

def main():
    candidates = [2, 3, 6, 7]
    target = 7
    result = []
    combination_sum(candidates, target, 0, [], result)
    print(result)

main()




#5
def count_subsets(nums, target):
    n = len(nums)
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

def main():
    nums = [1, 2, 3, 3]
    target = 6
    print(f"Count of subsets with sum {target}: {count_subsets(nums, target)}")

main()








#6
def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]

def main():
    s = "applepenapple"
    word_dict = {"apple", "pen"}
    print(word_break(s, word_dict))

main()







#7
def lcs(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def main():
    x = "AGGTAB"
    y = "GXTXAYB"
    print(f"Length of Longest Common Subsequence: {lcs(x, y)}")

main()








#8
def is_safe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    if solve(board):
        for row in board:
            print(row)
    else:
        print("No solution exists")

main()








#9
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Maximum Subarray Sum: {max_subarray_sum(arr)}")

main()







#10
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def main():
    coins = [1, 2, 5]
    amount = 11
    print(f"Minimum coins needed: {coin_change(coins, amount)}")

main()






def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def min_cut_palindrome_partition(s):
    n = len(s)
    dp = [0] * n
    for i in range(n):
        min_cut = i
        for j in range(i + 1):
            if is_palindrome(s, j, i):
                min_cut = 0 if j == 0 else min(min_cut, dp[j - 1] + 1)
        dp[i] = min_cut
    return dp[n - 1]

def main():
    s = "aab"
    print(f"Minimum cuts for palindrome partitioning: {min_cut_palindrome_partition(s)}")

main()








def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

def main():
    s = "bbabcbcab"
    print(f"Longest Palindromic Subsequence Length: {longest_palindromic_subsequence(s)}")

main()









from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            level.reverse()
        
        result.append(level)
        left_to_right = not left_to_right
    
    return result

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(f"Zigzag Level Order Traversal: {zigzag_level_order(root)}")

main()

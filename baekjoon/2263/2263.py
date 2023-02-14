import sys

def solution(n, inorder, postorder):
    stack = [(0, n - 1, 0, n - 1)] # inorder_start, inorder_end, postorder_start, postorder_end

    while stack:
        in_start, in_end, post_start, post_end = stack.pop()
        if in_end < in_start:
            continue
        root = postorder[post_end]
        print(root, end=' ')
        in_root_index = inorder.index(root)
        in_left_subtree_range = (in_start, in_root_index - 1)
        in_right_subtree_range = (in_root_index + 1, in_end)
        post_left_subtree_range = (post_start, post_start + in_root_index - 1 - in_start)
        post_right_subtree_range = (post_start + in_root_index - in_start, post_end - 1)
        stack.append((*in_right_subtree_range, *post_right_subtree_range))
        stack.append((*in_left_subtree_range, *post_left_subtree_range))

n = int(sys.stdin.readline())
inorder = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]
postorder = [int(i) for i in sys.stdin.readline().rstrip().rsplit()]

solution(n, inorder, postorder)
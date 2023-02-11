def str_from_linked(node):
    if not node.next:
        return node.val
    return f"{node.val} + {str_from_linked(node.next)}"

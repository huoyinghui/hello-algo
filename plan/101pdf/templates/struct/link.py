
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoubleListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def list_to_linked_list(nums):
    """将列表转换为单链表"""
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def linked_list_to_list(head):
    """将单链表转换为列表"""
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


def list_to_doubly_linked_list(nums):
    """将列表转换为双链表"""
    if not nums:
        return None
    head = DoubleListNode(nums[0])
    cur = head
    for num in nums[1:]:
        new_node = DoubleListNode(num)
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next
    return head


def doubly_linked_list_to_list(head):
    """将双链表转换为列表"""
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


def print_linked_list(head):
    """打印单链表"""
    result = []
    cur = head
    while cur:
        result.append(str(cur.val))
        cur = cur.next
    return " -> ".join(result)


def print_doubly_linked_list(head):
    """打印双链表（仅向前方向）"""
    result = []
    cur = head
    while cur:
        result.append(str(cur.val))
        cur = cur.next
    return " <-> ".join(result)


def get_tail(head):
    """获取双链表的尾节点"""
    if not head:
        return None
    cur = head
    while cur.next:
        cur = cur.next
    return cur


def insert_after(node, val):
    """在指定节点后插入新节点（适用于双链表）"""
    if not node:
        return
    new_node = DoubleListNode(val)
    new_node.next = node.next
    new_node.prev = node
    if node.next:
        node.next.prev = new_node
    node.next = new_node


def delete_node(node):
    """删除指定节点（适用于双链表）"""
    if not node:
        return
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev




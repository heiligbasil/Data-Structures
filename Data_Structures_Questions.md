Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
> O(1) because it doesn't need to search and can just perform the action on the item straight away

2. What is the runtime complexity of `dequeue`?
> O(1) because this is a single operation and the other parts of the list are ignored

3. What is the runtime complexity of `len`?
> O(1) because the variable is already stored as the size and just needs to retrieve it.<br>
> If, on the other hand, I hadn't made use of the helper variable to retrieve the size,<br>
>     I would have to traverse the whole list counting the nodes, resulting in O(n) 

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
> O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
> O(1)

3. What is the runtime complexity of `ListNode.delete`?
> O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
> O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
> O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
> O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
> O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
> O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
> O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
> O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    > O(1) - same because it is calling the Node delete function

11. What is the runtime complexity of `DoublyLinkedList.get_max`?
> O(n)
 
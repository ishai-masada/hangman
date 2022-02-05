#include "stdio.h"
#include "stdlib.h"

struct StackElem
{
    int value;
    struct StackElem *_next;
};

struct Stack
{
    struct StackElem *_first;
};

struct Stack new_stack()
{
    struct Stack stack = {._first = NULL};
    return stack;
}

void push(struct Stack *stack, int value)
{
    struct StackElem *new_elem = malloc(sizeof(struct StackElem));
    new_elem->value = value;
    new_elem->_next = stack->_first;
    stack->_first = new_elem;
}

int pop(struct Stack *stack)
{
    if (stack->_first == NULL)
    {
        return -1;
    }
    else
    {
        struct StackElem *elem = stack->_first;
        stack->_first = elem->_next;
        return elem->value;
    }
}

int peek(struct Stack *stack)
{
    if (stack->_first == NULL)
    {
        return -1;
    }
    else
    {
        return stack->_first->value;
    }
}

int len(struct Stack *stack)
{
    if (stack->_first == NULL) {
        return 0;
    } else {
        return _elem_len(stack->_first);
    }
}

int _elem_len(struct StackElem *stack_elem)
{
    if (stack_elem->_next == NULL) {
        return 1;
    } else {
        return 1 + _elem_len(stack_elem->_next);
    }
}

int main()
{
    struct Stack stack = new_stack();

    // Push thrice
    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);

    printf("stack len: %d\n", len(&stack));

    // Pop all elements
    printf("%d\n", pop(&stack));
    printf("%d\n", pop(&stack));
    printf("%d\n", pop(&stack));

    // Attempt to pop once more
    printf("%d\n", pop(&stack));

    return 0;
}


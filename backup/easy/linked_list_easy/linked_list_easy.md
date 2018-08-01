## 21 mergeTwoLists
> 把两个有序链表合并成为一个有序链表。

* 拼接即可，注意细节。

## 83 deleteDuplicates
> 有序链表去重

* 两个指针共同遍历，拼接即可，注意细节。

## 141 hasCycle
> 判断链表中是否有环

* 两个遍历，其中一个为一步，一个为两步。
* 当二者重逢时则链表有环。

## 160 getIntersectionNode
> 找到两个链表的相交部分

* 两个指针都遍历两个链表。
* 一个从a开始，一个从b开始。
* 最后二者相等的地方就是相交的部分。

## 203 removeElements
> 删除链表中相应的值

* 链表头也要判断，所以生成一个额外的链表头，用next给出表头。


## 206 reverseList
> 反转链表



## 234 isPalindrome
> 判断链表是否是回文串

* 用快慢指针的方式达到链表中点。
* 逐个对比。

## 237 deleteNode
> 删除给定的节点

* 给定的是节点，不是链表。
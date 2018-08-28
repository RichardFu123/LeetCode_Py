## 046 permute
> list
> 给出给定列表的所有全排列。

* itertools中的permutations(iterable)可以迭代返回iterable中的全排列。

## 047 permuteUnique
> list
> 给出列表中的不重复全排列.

* 在046的基础上用set去重即可.

## 075 sortColors
> list
> 将列表原地排序

* 用列表的sort().

## 077 combine
> list
> 返回1~n的全部k位组合。

* 用itertools的combinations迭代器即可解决。

## 078 subsets
> list
> 找到给定集合的所有子集。

* 用itertools中的combinations可以轻松解决问题。
* combinations(iterable，i)可以迭代返回iterable中所有长度为i的组合形式。
* []空集也是子集之一。

## 094 inorderTraversal
> tree
> 返回中序遍历

* 递归返回

## 096 numTrees
> tree
> DP
> 返回用1~n个节点能构造出多少种不同的二叉搜索树.

* 用动态规划的思想,每个节点的左子叶可以为所有比其小的数,右子叶可以为所有比其大的数.

## 137 singleNumber2
> list
> 找出数组内只出现过一次的数。

* 用collections中的Counter统计次数。
* 用Counter的most_common()方法来给出从高到低的统计二维数列。
* 其中最后一项的第一项既是结果。

## 162 findPeakElement
> binary search
> 找出数组的任意一个峰值。

* 先确定首尾。
* 再进行搜索。
* 搜索时用try减少麻烦。

## 215 findKthLargest
> list
> 找出列表中第k大的数字.

* 用list的sort就能解决.

## 216 combinationSum3
> list
> 找到1-9的和为n的k个数的组合

* combinations解决

## 226 invertTree
> tree
> recrusion
> 翻转二叉树

* 用递归调用，交换左右子叶，并对左右子叶也执行翻转函数。

## 260 singleNumber
> list
> 找出数组中两个只出现过一次的数。

* 同137题。

## 338 countBits
> bit manipulation
> dynamic programming
> 用列表形式打出range(num+1)的所有二进制中1的计数。

* 二进制第一位有0，1.
* 二进制第二位有1，2.
* 二进制第三位有1，2，2，3.
* 可知，每一位上的1的个数组合即为前面所有值+1：
* 第四位：1，2，2，3，2，3，3，4.

## 347 topKFrequent
> list
> 统计列表中出现最多的k个元素。

* 在Python中，调用collections中的Counter即可。

## 413 numberOfArithmeticSlices
> dynamic programming
> list
> 找到严格单增数列里有多少等差子列。

* 因为是严格的单增数列，所以不存在差值为0的两项。
* 所以在搜索的时候不需要考虑相隔数字的问题。

## 419 countBattleships
> list
> 找出二维平面内有几个独立的X区域

* 遍历时统计两个值：
	1. 有多少个x
	2. 每个x在下侧和右侧有多少个相邻的x
* 使用try，except来省略遍历中是否越界的判断。
* 将以上统计的两个值相减既是独立x区域。

## 442 findDuplicates
> list
> 找到数组中哪些数字出现了两次。

* 排序后遍历即可。

## 535 encodeAndDecodeTinyurl
> math 
> hash table
> 将字符串encode后decode

* 在函数内保存两组字典，保存字符串和hash值，交换输出即可。

## 647 countSubstrings
> DP
> string
> 找到字符串有多少个回文子串。

* (x，x)保证了aba类型的全部回文子串，(x,x+1)保证了aa类型的子串。

## 654 constructMaximumBinaryTree
> tree
> 从最大值开始，左子树和右子树分别由左侧和右侧的最大值构成。

* 递归调用即可。

## 677 MapSum
> trie
> 设计实现MapSum功能

* 用字典。

## 789 escapeGhosts
> math
> 确保ghosts数组中都比（0，0）离target远。

* 计算出全部ghosts离target的路径长度。
* 对比target与原点的路径长度即可。

## 807 maxIncreaseKeepingSkyline
> list
> 在一个二维数组内，将每一个值变成行、列最大值的较小值需要多少。

* 用zip获得列的排列数组。
* 遍历原数组，用行的最大值与列的最大值的较小值减去原数累加即可。

## 814 pruneTree
> tree
> 将二叉树所有只含0的子树去除。

* 用递归调用，目标是所有左右子叶都为null且val为0的节点。
* 由于递归调用是从树的末端开始，故可以去除全部为0分支。

## 890 findAndReplacePattern
> string
> 找到words中所有符合pattern的单词。

* 制作一个翻译器，其核心是一个字典，用字母为键，用字母出现的顺序为值。
* 如上制作的翻译器，可以保证同样pattern的单词的输出均一致。
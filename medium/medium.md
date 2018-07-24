## 046 permute
> list
> 给出给定列表的所有全排列。

* itertools中的permutations(iterable)可以迭代返回iterable中的全排列。

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

## 137 singleNumber2
> list
> 找出数组内只出现过一次的数。

* 用collections中的Counter统计次数。
* 用Counter的most_common()方法来给出从高到低的统计二维数列。
* 其中最后一项的第一项既是结果。

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
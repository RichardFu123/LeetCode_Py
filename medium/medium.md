##046 permute
> 给出给定列表的所有全排列。

	* itertools中的permutations(iterable)可以迭代返回iterable中的全排列。

##078 subsets
> list
> 找到给定集合的所有子集。

	* 用itertools中的combinations可以轻松解决问题。
	* combinations(iterable，i)可以迭代返回iterable中所有长度为i的组合形式。
	* []空集也是子集之一。

##338 countBits
> bit manipulation
> dynamic programming
> 用列表形式打出range(num+1)的所有二进制中1的计数。

	* 二进制第一位有0，1.
	* 二进制第二位有1，2.
	* 二进制第三位有1，2，2，3.
	* 可知，每一位上的1的个数组合即为前面所有值+1：
	* 第四位：1，2，2，3，2，3，3，4.

##535 encodeAndDecodeTinyurl
> math 
> hash table
> 将字符串encode后decode

	* 在函数内保存两组字典，保存字符串和hash值，交换输出即可。


##807 maxIncreaseKeepingSkyline
> list
> 在一个二维数组内，将每一个值变成行、列最大值的较小值需要多少。

	* 用zip获得列的排列数组。
	* 遍历原数组，用行的最大值与列的最大值的较小值减去原数累加即可。
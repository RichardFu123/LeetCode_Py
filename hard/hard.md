## 065 isNumber
> string
> math
> 判断一个字符串是否是一个正确的数字。

* 用try捕捉异常即可。 

## 149 maxPoints
> math
> iterable
> hash table
> 判断有多少个点在一条直线上。

* 难点：
	1. 存在相同的点
	2. 存在某一坐标值相同的点（slope时对分母0的处理）
* 可以用collections中的Counter来解决重复问题
* 可以用itertools中的combinations来解决两点组合问题。
* 可以通过slope为键，点或次数为值来构建字典，获得有多少个两两组合的点斜率相同。

## 239 maxSlidingWindow
> stack
> deque
> 输出步长为1，尺寸为k的滑动窗口在数列nums上每一步中的最大值。

* 用collections中的deque来创建maxlen为k的固定长度双向队列。
* 将nums[:K]先输进deque，得到起始点的max值
* 将nums[k:]一次遍历输入deque，每次获取max值即可。
# LeetCode
## 1 twoSum
> 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
	
* enumerate的应用，快速在列表内寻找符合条件的元素。

## 7 reverse
> 反转输出一个数

* 转字符串重排。
* 也可以逐位求余。

## 9 isPalindrome
> 判断给定数字是否为回文数

* 负数不可能是
* 只有一位一定是
* 变成字符串逐位对比即可。

## 014 longestCommonPrefix
> 寻找给定字符串列表的最长公共开头。

* 用zip(*strs)解包列表。
* 用set()去重，若len为1则为公共前缀。
* 若不为1则输出结果。

## 020 Valid Parentheses
> 确定字符串中是否全部括号都符合要求。

* 所谓符合要求，就是每一种类的左括号，其下一个同一种类的括号一定是他的右括号。
* 只要长度是奇数就一定不符合规则。

## 21 mergeTwoLists
> 把两个有序链表合并成为一个有序链表。

* 拼接即可，注意细节。

## 26 removeDuplicates
> 给定数组，删除重复元素。

* 合理运用set和list的变换，达到去重的功能。

## 27 removeElement
> 原地移除给定值。

* 带条件遍历列表，构造新列表。

## 35 searchInsert
> 在排序数组中找到目标值索引，如果没有目标值，则返回插入位置。

* 用索引值遍历列表，返回合适的索引值。

## 53 maxSubArray
> 找到最大连续子列，并返回其和

* 用双子列遍历列表，子列一保证当前子列为区域最大子列，子列二负责保存最大的子列一。

## 058 lengthOfLastWord
> 确定最后一个单词的长度。

* 用strip去除头尾空格。
* 用split分割。
* 用len计长度。

## 62 uniquePaths
> 算出从m*n矩阵的一头到另一头有多少种走法。

* 不存在斜向走法，不存在倒退，所以到一个x，y位置的总方法为走到x-1，y和x，y-1之和。
* 一直后推到第一排和第一列，第一排和第一列上的位置走法都只有一种。
* 可以类比杨辉三角来理解。

## 63 uniquePathsWithObstacles
> 同62，不过加入了障碍物。

* 整体规则同62，但是加入前提判断条件，在输入矩阵为1的地方赋值为0即可。

## 64 minPathSum
> 同62，求路径上和最小的值。

* 反向运算，取小值相加即可。

## 66 plusOne
> 给定代位置代表位数的数组，返回其+1后的数组。[9,9]--[1,0,0]

* 列表转化为int，对int进行+1操作，int转化为字符串，字符串分割转换为列表。

## 67 addBinary
> 给定两个二进制数，求和输出二进制。

* python内置了丰富的进制转换函数。
* 注意输出时要将'0b'去掉。

## 69 mySqrt
> 实现计算平方根整数

## 70 climbStairs
> 求爬梯子有多少种爬法。

* 逆向思维，爬到最后一个梯子需要爬到倒数第一个和倒数第二个梯子。

## 83 deleteDuplicates
> 有序链表去重

* 两个指针共同遍历，拼接即可，注意细节。

## 88 merge
> 给定两个数组，将其2合并进其1。

* 对要何合并的部分进行遍历，对数值进行对比，将较大的后移。

## 118 Pascal'sTriangle
> 给定层数n，生成n层杨辉三角

* 活用lambda和map功能。

## 119 Pascal'sTriangle II
> 给定层数n，生成第n层杨辉三角

* 同118

## 121 maxProfit
> 给定价格列表，寻求最大利润的一次交易

* 同53，使用双子列遍历，子列一保证区域最大利润值，子列二保证最大子列一。

## 122 maxProfit
> 给定价格列表，寻求多次交易的最大利润

* 遍历列表，对全部隔日差值为正进行求和

## 136 singleNumber
> 给定数组中出了一个数，其余数均出现两次，找到这个数

* 遍历每个元素
* 两次异或运算^为0
* 0^a=a

## 136 isHappy
> 判断是否是快乐数

* 重复逐位平方求和。
* 将结果构建字典，当运算结果已在字典中时，停止。
* 如果1在字典内（或停止时n=1），则为快乐数。

## 141 hasCycle
> 判断链表中是否有环

* 两个遍历，其中一个为一步，一个为两步。
* 当二者重逢时则链表有环。

## 160 getIntersectionNode
> 找到两个链表的相交部分

* 两个指针都遍历两个链表。
* 一个从a开始，一个从b开始。
* 最后二者相等的地方就是相交的部分。

## 167 twoSum
> 在给定数组中找到两个数字的位置，目标数字为这两个数字之和。

* 构造字典，其键和值分别等于列表的值和索引，即list[索引]=值————>{'值'：'索引'}

## 168 convertToTitle
> 转换成A~Z的26进制。

* 用chr(),ord()转换编码即可。

## 169 majorityElement
> 找到众数

* 由于题中众数过半，可构造计数器，相同+1，不同-1，最后一定是>0的数为众数。

## 171 titleToNumber
> 168反向实现。

* 168反向计算。

## 172 trailingZeroes
> 求阶乘末尾有多少个0.

* 0的个数= n/5 + n/(5^2)+.......

## 189 rotate
> 旋转数组（后n位移到前端）

* 数组切片，重新组合。

## 190 reverseBits
> 输出十进制整数的二进制反转的十进制整数。

* 用{：b}.format(n)输出不带0b的二进制字符串。
* 用字符串的切片方法[：：-1]进行反转。
* 用int(str,2)方法进行二进制转十进制输出。

## 191 hammingWeight
> 输出十进制数的二进制有多少位1.

* 循环除2求余相加即可。

## 198 rob
> 给定数组，不能相邻取值，找到最大和。

* 保存两次求和结果，取大值。

## 203 removeElements
> 删除链表中相应的值

* 链表头也要判断，所以生成一个额外的链表头，用next给出表头。

## ？204 countPrimes
> 寻找比n小的质数有多少

* ？

## 205 isIsomorphic
> 是否同构

* 将s,t用zip打包。
* 此时zip包内相当于s与t的每一位都进行了绑定。
* 对比set(zip)、set(s)、set(t)的长度，相等既是同构。

## 206 reverseList
> 反转链表

## 217 containsDuplicate
> 判断列表是否有重复元素

* 应用set的特性，对比长度即可。

## 219 containsNearbyDuplicate
> 判断列表中是否有间隔最大为k位的重复数字

* 同167，用值和索引分别构造字典的键和值，进行遍历条件判断。

## 231 isPowerOfTwo
> 确定给定的数是否为2的幂。

* 二进制下，相邻数的按位与可以将大数最后一位的1变0.
* 2的幂在二进制下只有最高位是1，其余皆为0.

## 234 isPalindrome
> 判断链表是否是回文串

* 用快慢指针的方式达到链表中点。
* 逐个对比。

## 237 deleteNode
> 删除给定的节点

* 给定的是节点，不是链表。

## 242 isAnagram
> 是否字母异位词

* 比较长短。
* 转换为列表，进行排序
* 全等既是字母异位词。

## 258 addDigits
> 反复将各个位上的数字相加，直到结果为一位数。

* 既是除9的余数。

## 263 isUgly
> 确定一个数是否只由2，3，5组成。

* 2,3,5皆为素数，彼此之间不相干。

## 268 missingNumber
> 列表从0到n，找到中间缺少的那个数

* 设缺位为x，则可以将原数列视为：从1到n+1的n位数组，其第1位到第x位皆减一。
* 故利用等差数列求和公式即可计算x。

## 283 moveZeros
> 将列表中的0移到末尾

* 带索引遍历列表，将全部非0项按索引重排。
* 而后将后端全部写为0。

## 290 wordPattern
> 给定字符串是否符合给定pattern的模式

* 同205，将pattern和str分割为列表。
* 之后用zip()将pattern和str的元素进行绑定。
* 用set进行去重后进行len对比即可确定模式是否相同。
* 对于长度不同的干扰项，需要加入pattern和str元素的原始len比较。

## 292 canWinNim
> 确定先手的情况下是否能够赢得Nim游戏。

* 因为每轮每人只能拿1~3颗石头，所以完全可控范围是每轮两个人加起来一共拿四颗石头。
* 所以只要先手拿起m颗石头，m=n%4即可保证胜利。
* 换而言之，只要石子数n除4有余数，先手即可保证胜利。（不失误）
* 反之，若能整除4，则后手必胜。（不失误）

## 303 sumRange
> 对列表给定区间求和。

* 因为要多次调用，所以将列表进行预处理。
* 预处理为当前每位变成从头到当前位置之和。
* 区间的和即后端位置上的值减去前端位置再前一个位置上的值。

## 342 isPowerOfFour
> 确定一个数是否是4的幂。

* 4的幂必大于等于0.
* 4的幂其二进制必只有最高位为1.
* 4的幂其二进制长度必为奇数。

## 345 reverseVowels
> 反转字符串中的元音字母。

* 将元音字母与其索引位置取出，原位补空格。
* 将元音字母按索引位置倒序填入字符串。

## 349 intersection
> 返回两个给定列表的交集（元素无重复）

* 用set的去重功能和交集（&）运算即可。

## 350 intersectionII
> 返回两个给定列表的交集（元素需重复）

* 遍历其中一个列表
* 对元素进行判断，存在则放进新列表，并在判断列表进行删除。

## 367 isPerfectSquare
> 确定一个数是否是个整数的平方数。

* 用牛顿法迭代求解。

## 371 getSum
> 不用+-做运算。

* 二进制相加，同位为1则为0，后位+1.
* 同位为0则为0。
* 同位相异则为1。
* <<表示二进制移位，后接数字表示位数。

## 374 guessNumber
> 提供了判断函数，用二分法来逼近结果。

* 按照二分法思路逼近即可。

## 383 canConstruct
> 确定第一个字符串是否是第二个字符串的子串（无序）

* 遍历即可。

## 389 findTheDifference
> 给定两个字符串，返回第二个多的字符。

* 遍历删除即可。

## 400 findNthDigit
> 找到数列中第n个字符是什么。

* 1-9每个数字有1个字符，10-99有两个字符，以此类推。

## 401readBinaryWatch
> 算出二进制手表可能表示的时间。

* 0~11，0~59双遍历。
* 保证这两个数的二进制形式上的1等于给定数值即可输出。

## 405 toHex
> 将给定数字转化成16进制形式的字符串。

* 16进制一位占4位，所以用15来进行与运算。
* 运算结束后进行4位的右移即可。

## 409 longestPalindrome
> 寻找字符串的最长回文串长度

* 运用collections模块下的Counter容器即可。
* 计数分奇偶数。
* 偶数直接计入长度。
* 计数可贡献计数-1的长度。
* 但一旦出现奇数，回文串中心可容纳一个字符，则至少长度+1

## 414 thridMax
> 找到列表中第三大的数

* 排序列表，带倒数3来遍历。
* 在非重复数上倒数，输出倒数1的数。

## 415 addStrings
> 将字符串形式的数字进行相加。

* 反向遍历两数字，chr(num)与num之间相差48.
* 每次相加之后判断是否进位即可。

## 434 countSegments
> 计算字符串内有多少单词。

* split后len即可。

## 438 findAnagrams
> 寻找字符串中所有异位词的起始索引位

* 用给定单词构造以值为键，以count为值的dict。
* 遍历。

## 441 arrangeCoins
> 给定数字能容纳多大的等差数列。

* 联立等差数列求和公式和一元二次方程求根公式即可。

## 443 compress
> 返回按要求压缩后的列表长度。

* 按要求压缩即可。

## 447 numberOfBoomerangs
> 寻找给定列表里全部“回旋镖”。 (i, j, k其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序））。

* 距离做键，次数为值，构造字典

## 448 findDisappearesdNumbers
> 找到列表中没有出现的数字（1到n）

* 索引方式遍历数组。
* 将值再作为索引，对相应位置的值进行绝对值取负。
* 则最后为正的索引+1即为缺失的数字。

## 453 minMoves
> 用最小的次数，使数组内全部数字相等，每次可以将其中len-1个数+1.

* n个数，每次n-1个加一，在相对参照系下，既是每次可以将一个数-1.
* 将sum(nums)看做一个山，则海平面就是len(nums)*min(nums)。
* 把山移平只需要进行他们之差次-1。

## 459 repeatedSubstringPattern
> 确定字符串是否由多个相同子串组成。

* 将字符串*2并掐头去尾。
* 此时如果字符串由子串重复组成，则第一遍的[1:]子串加上第二遍的[0]仍可以组成原字符串。

## 461 hammingDistance
> 计算两个数二进制有多少位不相同。

* ^运算结果中，不同位上变成1，其余为0.
* n&(n-1)的性质：把最小位的1变成0.
* 循环上步，每步计数，计得1的数量。

## 463 islandPerimeter
> 计算“岛”的边长。

* 每个1记四个边，每个相邻减两个边。

## 475 findRadius
> 找到使列表2中的数字展开后能够覆盖全部列表1中数字的最小半径。

* 双重遍历查找即可。

## 476 findComplement
> 二进制取反输出。

* 与全1异或等于取反。

## 482 licenseKeyFormatting
> 按照给定长度给字符串从后向前插入'-'。

* 用''.replace(old,new)来替换掉原字符串全部的'-'。
* 用''.upper()来全部大写。
* 遍历插入'-'即可。

## 485 findMaxConsecutiveOnes
> 寻找最大连续1的个数

* 将非1数字置为0。
* 将list转为str，对0进行分割。
* 取最大len即可。

## 492 constructRectangle
> 找到给定正整数的两个距离最近的正整除数。

* 用math模块下的sqrt定位到中心，以减少时间。

## 496 nextGreaterElement
> 输出子列a中每个数字在数列b中右侧下一个更大值的值，没有则填充-1。

* 因为为无重复数列，所以以数列b的值为键，以右侧第一个更大值之差为值构建字典，若没有则填充-1.
* 用子列a逐个查找字典构建结果数列即可。

## 500 findWords
> 找到全部能用键盘其中一行就能打出的单词。

* 用set相减来直接确定是否有多余字母。
* 用lower来全部小写。

## 504 convertToBase7
> 将给定数字以七进制字符串输出。

* 循环余7除7即可。

## 506findRelativeRanks
> 按大小给数组替换成名次。

* 应用lambda进行sort（）。

## 507 checkPerfectNumber
> 判断一个数是否与其全部正整数因子之和相等。

* 用sqrt减小区间后遍历即可。

## 520 detectCapitalUse
> 判断单词大小写是否正确。

* 字符串的islower()\isupper()方法可以直接判断字符串整体是否全部为大、小写。
* 之后用以上两个方法判断是否只有首字母大写。

## 521 findLUSlength
> 寻找两个字符串的最长子序列。

* 一个数列的最长子序列就是其本身。
* 如果两个字符串不相等，则最长子序列就是较长的那个。
* 相等则为-1

## 532 findPairs
> 找到数组中全部差值为k的数有多少对

* 构造当前数组的set，构造当前数组所有数字+k的set，用&求两个set的交集，返回len。
* 若k==0，则用collection模块中的Counter()函数，返回全部计数大于1的数字个数。

## 541 reverseStr
> 按照规则反转字符串。

* 按要求反转即可。

## 551 checkRecord
> 判断字符串有无三连L和多余一个A

* 按条件判断即可。

## 557 reverseWords
> 将字符串每个单词逐个反转输出

* 运用字符串的split（）对空格进行分割。
* 切片翻转后拼接输出。

## 561 arrayPairSum
> 将2n数列拆为n个2位子列，其子列中最小数之和最大

* 输出排序后的步长为2的取值之和即可。

## 566 matrixReshape
> 根据给定条件重塑矩阵

* 先判断数据量是否正确。
* 将原数组化为一行。
* 重组数组。

## 575 distributeCandies
> 两人均分多种糖果，其中一人最多能分多少种？

* 用len(set())获得糖果类型总数。
* 每种糖果数量-1之和为余量count，代表在不影响糖果多样性的前提下，另一个人可以拿到多少重复的糖果。
* 若count大于等于糖果总数的一半，则有多少种可以拿多少种。
* 若小于总数的一半，则count与总数一半的差值为不能拿的种类数量。

## 581 findUnsortedSubarray
> 在列表中找到最小未排序子列，返回len

* 将排序后和排序前的数列进行对比即可。

## 594 longestHarmoniousSubsequence
> 最值相差为1的子列的最长长度。

* 用Counter来将全部元素计数。
* 找出差值为1的数对中最多的一个。

## 598 maxCount
> 找到一系列操作后，矩阵中最大数的个数。

* 题中矩阵的每次操作皆从左上角开始。
* 所以只需要寻找到ops中操作的行、列的最小值即可。

## 599 findRestaurant
> 找出两列表中索引和最小的元素。

* 用位置做值元素做键构造字典。
* 找出同元素相加，找到最小索引和。
* 其余的共同元素排在后面。

## 605 canPlaceFlowers
> 找到最大个能与1不相邻的位置。

* 将列表前后填充方便运算。
* 遍历填充后的列表逐个判断即可。

## 628 maximumProduct
> 寻找列表里三个数之积的最大值。

* 重排列表后求积。
* 问题分解：
** 后三位符号相同：后三位求积
** 后三位符号不同：最后一位乘前端两位

## 633 judgeSquareSum
> 确定一个数是否为两个数的平方和。

* 用sqrt确定最大可能值。
* min=0和max值双向逼近中点，若平方和低于n则min++，若高于n则max--，相等return true。

## 643 findMaxAverage
> 寻找均值最大的k长子列的均值。

* 同53，双子列遍历，子列1确定区域最大，子列2确定最大子列1。

## 645 findErrorNums
> 有序数列中其中一个数被调换成了另一个数，找出这两个数。

* 列表和减去集合和等于重复值之和。
* 原本数列和（1到n）减去集合和为缺值。

## 657 judgeCircle
> 判断经过字符串中的UD和LR是否同时相等。

* 运用collections的Counter模块进行计数。
* 由于不一定存在全部四种字母，所以用try来进行。

## 661 imageSmoother
> 将矩阵中每个数与邻近8个数求平均。

* 用deepcopy会减少很多麻烦。

## 665 checkPossibility
> 确定是否最多用一次改变就能使数列单增。

* 要点在于用两对指针同时对比，1-3,2-4.若两对指针同时False，则直接False。
* 如果只是单个指针False，则计数最后对比<=1即可。

## 674 findLengthOfLCIS
> 找到最长单增子列的长度。

* 用两个指针记录单增子列的位置，对比即可。

## 680 validPalindrome
> 判断当前字符串或去掉一个字符的当前字符串是否为回文串。

* 按照普通方法首尾对比到第一个不同处。
* 将此时的子串首尾各去一位组成两个新的子串。
* 判断两个子串是否其中一个为回文串。

## 682 calPoints
> 根据规则算出总和。

* 遍历时逐个判断条件即可。

## 686 repeatedStringMatch
> 判断一个字符串能否折叠n次后容纳另一个字符串。可以返回n，不能返回-1.

* 只需要将字符串重复到目标的len的三倍以上，即可判断是否能够容纳目标。
* 同样，如果len已经为目标len的三倍以上，则可以直接判断，无需重复。

## 693 hasAlternatingBits
> 判断数字二进制是否全为01交替形式。

* 转为二进制字符串形式遍历判断即可。

## 697 findShortestSubArray
> 找到包含全部众数的最大子列

* 用Counter计数
* 两端缩进直到全为众数为止。

## 709 toLowerCase
> 将给定字符串中的大写字母转成小写

* 用字符串的lower()方法即可。

## 717 isOneBitCharacter
> 确定最后一位是不是1bit。

* 从头遍历，遇1跳两位，遇0跳一位。

## 720 longestWord
> 按照给定规则寻找单词。

* sorted(list(str()))按照字符串从小到大返回排序列表。
* 用set（）来过滤元素。
* 输出列表中最长的元素。

## 724 pivotIndex
> 寻找列表中靠左的一个索引，使索引左右之和相等。

* 先求整个数组之和。
* 再从左向右遍历。
* 遍历时对当前项求和，并在总和中减去。
* 当上面二者相等时即是最靠左的中心索引。

## 728 selfDividingNumbers
> 找到给定上下限内的全部自除数。

* 用range(下限，上限-1)来遍历。
* 转字符串遍历单个数字。

## 744 nextGreatestLetter
> 找到列表里距目标字母最近的更大的一个字母，若没有，则返回最小字母。

* 用set去重后list排序遍历即可。

## 746 minCostClimbingStairs
> 每步都能选择进一或进二，求遍历列表后的和的最小值。

* 从开头进行计算，将每一位替换成到达此处的最小值。
* 最后只需要对比最后两位的大小即可。

## 747 dominantIndex
> 确定列表中最大数是否至少是其他数的两倍，是的话返回索引。

* 带三个变量遍历数组，确定老大和老二以及老大的索引。
* 判断即可。

## 762 countPrimeSetBits
> 找到给定区间内有多少二进制中1之和为质数的数字。

* 由于不超过10^6，所以质数最大用到23，所以直接枚举即可。
* 直接使用str的count（'1'）来计算1的个数。

## 766 isToeplitzMatrix
> 判断是否为托普利茨矩阵

* 将问题分解为判断每个m[i][j]是否相等于m[i+1][j+1].

## 771 numJewelsInStones
> 找出列表J中有多少S中的字符。

* 遍历即可。

## 784 letterCasePermutation
> 输出所有大小写变化子集。

* 按照规则构建输出即可。

## 788 rotatedDigits
> 根据条件逐位判断数字。

* 遍历判断即可。

## 796 rotateString
> 判断A经过旋转是否能够变成B。

* 隐含条件：AB长度必须相等。
* 将旋转字符串看做一个首尾相接的环，只要B+=B即可保证这个环在字符串意义上的首尾相接。
* 所以只要判断A in B+B即可

## 804 uniqueMorseRepresentations
> 找出给定字符串列表共有几种摩尔斯编码形式。

* 按照ord(字母)-ord(a)的方法在翻译表中找到对应的摩尔斯码并翻译单词。
* 用set来去重，用len来统计数量。

## 806 numberOfLines
> 判断根据给定的字母宽度，100为一行，给定字符串能写多少行，最后一行占用多少。

* 使用widths[ord(i)-ord('a')]获得每一个字母宽度对应的索引值。
* 遍历相加，每100换行。
* 换行有两种情况：
	* 当刚好100时，当前宽度不保留，sum变为0.
	* 当宽度超过100时，保留当前宽度，sum变为当前字母宽度。

## 811 subdomainVisits
> 判断每个子域名访问次数。

* 分割统计即可。

## 812 largestTriangleArea
> 寻找给定点的集合中，能够组成的最大三角形的面积。

* 直接套用三角形三顶点面积公式。
* 用itertools中的combinations(points,3)直接遍历全部三组合输出。

## 819 mostCommonWord
> 找出频数最大的非禁词。

* 用正则表达式来将字符串中的非字母去掉。
* 用''.lower()来全部小写。
* 用''.split()来分离成列表。
* 遍历去除全部禁词
* 用collections.Counter().most_common(0)来找到最大频数的单词。

## 821 shortestToChar
> 判断字符串中每个字符离最近目标字符的距离。

* 两次循环，第一个确定全部目标的位置，第二个进行距离运算。

## 824 toGoatLatin
> 按照给定方案进行字符串改造。

* 遍历即可。

## 830 largeGroupPositions
> 确定大于2的连续字符的起始、终止位置。

* 带计数从头遍历即可。

## 832 flipAndInvertImage
> 按行翻转并取反二进制矩阵。

* 按要求遍历。

## 836 isRectangleOverlap
> 判断两个矩形是否有重叠

* 纸面推导即可。

## 840 numMagicSquaresInside
> 确定矩阵内有多少幻方。

* 只有1~9。
* 中心必为5。
* 偶在角，奇在变。

## 844 backspaceCompare
> 按照给定规则比较两字符串。

* 按照规则生成字符串即可。

## 849 maxDistToClosest
> 找到离其他1最大距离的索引。

* ?

## 852 peakIndexInMountainArray
> 二分查找山脉数组中的最大值

* 二分查找即可
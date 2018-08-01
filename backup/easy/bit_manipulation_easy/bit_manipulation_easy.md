## 190 reverseBits
> 输出十进制整数的二进制反转的十进制整数。

* 用{：b}.format(n)输出不带0b的二进制字符串。
* 用字符串的切片方法[：：-1]进行反转。
* 用int(str,2)方法进行二进制转十进制输出。

## 191 hammingWeight
> 输出十进制数的二进制有多少位1.

* 循环除2求余相加即可。

## 342 isPowerOfFour
> 确定一个数是否是4的幂。

* 4的幂必大于等于0.
* 4的幂其二进制必只有最高位为1.
* 4的幂其二进制长度必为奇数。

## 405 toHex
> 将给定数字转化成16进制形式的字符串。

* 16进制一位占4位，所以用15来进行与运算。
* 运算结束后进行4位的右移即可。

## 371 getSum
> 不用+-做运算。

* 二进制相加，同位为1则为0，后位+1.
* 同位为0则为0。
* 同位相异则为1。
* <<表示二进制移位，后接数字表示位数。

## 401readBinaryWatch
> 算出二进制手表可能表示的时间。

* 0~11，0~59双遍历。
* 保证这两个数的二进制形式上的1等于给定数值即可输出。

## 461 hammingDistance
> 计算两个数二进制有多少位不相同。

* ^运算结果中，不同位上变成1，其余为0.
* n&(n-1)的性质：把最小位的1变成0.
* 循环上步，每步计数，计得1的数量。

## 476 findComplement
> 二进制取反输出。

* 与全1异或等于取反。

## 762 countPrimeSetBits
> 找到给定区间内有多少二进制中1之和为质数的数字。

* 由于不超过10^6，所以质数最大用到23，所以直接枚举即可。
* 直接使用str的count（'1'）来计算1的个数。
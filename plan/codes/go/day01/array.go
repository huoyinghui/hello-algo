package main

import "fmt"

func checkIndex(nums []int, index int) {
	if index < 0 || index >= len(nums) {
		panic("Index out of bounds")
	}
}

/* 随机访问元素 */
func randomAccess(nums []int, index int) int {
	if index < 0 || index >= len(nums) {
		panic("Index out of bounds")
	}
	return nums[index]
}

/* 扩展数组长度 */

/* 在数组的索引 index 处插入元素 num */
func insert(nums []int, item int, index int) bool {
	checkIndex(nums, index)
	// 把索引 index 以及之后的所有元素向后移动一位
	for i := len(nums) - 1; i > index; i-- {
		nums[i] = nums[i-1]
	}
	// 将 item 赋给 index 处的元素
	nums[index] = item
	return true
}

/* 删除索引 index 处的元素 */
func remove(nums []int, index int) []int {
	checkIndex(nums, index)
	n := len(nums)
	for i := index; i < n-1; i++ {
		fmt.Printf("i:%d nums[i]:%d nums[i+1]:%d\n", i, nums[i], nums[i+1])
		nums[i] = nums[i+1]
	}
	// 删除最后一个元素
	nums = nums[:n-1]
	return nums
}

/* 遍历数组 */
func traverse(nums []int) (count int) {
	count = 0
	// 通过索引遍历数组
	for i := 0; i < len(nums); i++ {
		fmt.Printf("i:%d v:%d ", i, nums[i])
		count += nums[i]
	}
	fmt.Println()

	// 直接遍历数组元素
	for _, num := range nums {
		fmt.Printf("v:%d ", num)
	}
	fmt.Println()

	// 同时遍历数据索引和元素
	for i, num := range nums {
		fmt.Printf("i:%d v:%d ", i, num)
	}
	fmt.Println()
	return count
}

/* 在数组中查找指定元素 */

func main() {
	nums := []int{10, 20, 30, 40, 50}
	// traverse(nums)
	// fmt.Println(randomAccess(nums, 2))
	// fmt.Println(insert(nums, 100, 2))
	// fmt.Println(nums)
	fmt.Println(remove(nums, 1))
}

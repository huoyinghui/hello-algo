package leetcode

import (
	"math"
)

func countNumbers(cnt int) (buf []int) {

	m := math.Pow(10, float64(cnt))

	// traverse
	buf = make([]int, int(m)-1)
	for i := 1; i < int(m); i++ {
		buf[i-1] = i
	}
	return buf
}

package leetcode

import (
	"sort"
)

func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)

	i := 0
	j := 0

	for i < len(g) && j < len(s) {
		if g[i] <= s[j] {
			i += 1
		}
		// fmt.Println(i, j, g[i], s[j])
		j += 1
	}
	return i
}

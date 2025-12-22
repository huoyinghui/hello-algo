package leetcode

import (
	"testing"
)

func TestFindContentChildren(t *testing.T) {
	g := []int{1, 2, 3}
	s := []int{1, 1}
	res := findContentChildren(g, s)
	t.Logf("g = %v, s = %v, res = %d", g, s, res)
}

func TestFindContentChildren2(t *testing.T) {
	g := []int{1, 2}
	s := []int{1, 2, 3}
	res := findContentChildren(g, s)
	t.Logf("g = %v, s = %v, res = %d", g, s, res)
}

func TestFindContentChildren3(t *testing.T) {
	g := []int{1, 2, 3}
	s := []int{3}
	res := findContentChildren(g, s)
	t.Logf("g = %v, s = %v, res = %d", g, s, res)
}

func TestFindContentChildren4(t *testing.T) {
	// g = [10,9,8,7]
	g := []int{10, 9, 8, 7}
	s := []int{5, 6, 7, 8}
	res := findContentChildren(g, s)
	t.Logf("g = %v, s = %v, res = %d", g, s, res)
}

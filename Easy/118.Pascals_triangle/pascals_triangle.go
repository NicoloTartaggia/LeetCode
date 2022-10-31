func generate(numRows int) [][]int {
    res := make([][]int, numRows)
    for i := 0; i < numRows; i++ {
        if i == 0 {
            res[i] = append(res[i], []int{1}...)
        } else {
            for j := 0; j < i+1; j++ {
                if (j == 0 || j == i) {
                    res[i] = append(res[i], []int{1}...)
                } else {
                    res[i] = append(res[i], res [i-1][j-1] + res [i-1][j])
                } 
            }
        }
    }
    return res
}
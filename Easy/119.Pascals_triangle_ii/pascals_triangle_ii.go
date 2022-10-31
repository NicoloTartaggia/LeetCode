func getRow(rowIndex int) []int {
    res := make([][]int, rowIndex+1)
    for i := 0; i < rowIndex+1; i++ {
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
    return res[rowIndex] 
}
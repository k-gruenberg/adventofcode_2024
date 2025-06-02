main = do  
    file_content <- readFile "day4_input.txt"
    let lines_ = lines file_content
    let cols = [[line!!i | line <- lines_] | i <- [0..length (lines_!!0) - 1]]
    let diags = [[lines_!!i!!j | i <- [0..length lines_ - 1], j <- [0..length lines_ - 1], i + j == s] | s <- [0..2*(length lines_) - 1]] ++
                [[lines_!!i!!j | i <- [0..length lines_ - 1], j <- [0..length lines_ - 1], i - j == d] | d <- [-(length lines_) + 1..length lines_ - 1]]
    let h_words = [take 4 (drop i line) | line <- lines_, i <- [0..length line - 4]]
    let v_words = [take 4 (drop i col)  | col  <- cols,   i <- [0..length col  - 4]]
    let d_words = [take 4 (drop i diag) | diag <- diags,  i <- [0..length diag - 4]]
    print $ sum [length [word | word <- group, word `elem` ["XMAS", "SAMX"]] | group <- [h_words, v_words, d_words]]
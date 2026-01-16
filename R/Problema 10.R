primos <- c(2)
n <- 2000000
for (i in seq(3, n, by = 2)) {
  div_i <- c()
  for (j in 2:ceiling(sqrt(i))) {
    if (i %% j == 0) {
      div_i <- c(div_i, j)
      break
    }
  }
  
  if (length(div_i) == 0) {
    primos <- c(primos, i)
  }
}
print(primos)
sum(primos)




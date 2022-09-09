############## Estat 2

# 1 pop
'To devendo'



############## 2 pop

'Teste 1 - para media com var conhecidas'
# input
thmedia1i <- function(xb, yb, varx, vary, nx, ny){ 
  den <- varx/nx + vary/ny
  z <- (xb - yb) / sqrt(den)
  return(z) # z ~ N(0,1)
}

# amostra
thmedia1a <- function(x, y, varx, vary){ 
  nx <- length(x)
  ny <- length(y)
  xb <- mean(x)
  yb <- mean(y)
  
  den <- varx/nx + vary/ny
  z <- (xb - yb) / sqrt(den)
  return(z) # z ~ N(0,1)
}


'Teste 2 - para média com variancias desconhecidas e IGUAIS'
# input
thmedia2i <- function(xb, yb, varx, vary, nx, ny){ 
  Sp2 <- ((nx - 1) * varx + (ny - 1) * vary)/(nx + ny - 2)
  den <- sqrt(1/nx + 1/ny) * sqrt(Sp2)
  t  <- (xb - yb) / den
  return(t) # t ~ t(nx + ny - 2)
}

# amostra
thmedia2a <- function(x, y) {
  nx <- length(x)
  ny <- length(y)
  xb <- mean(x)
  yb <- mean(y)
  varx <- var(x)
  vary <- var(y)
  
  Sp2 <- ((nx - 1) * varx + (ny - 1) * vary)/(nx + ny - 2)
  den <- sqrt(1/nx + 1/ny) * sqrt(Sp2)
  t  <- (xb - yb) / den
  return(t) # t ~ t(nx + ny - 2)
}

'Teste 2 - para média com variancias desconhecidas e DIFERENTES'
# input
thmedia3i <- function(xb, yb, varx, vary, nx, ny){
  A <- varx/nx
  B <- vary/ny
  glnum <- (A + B)**2
  glden <- (A**2/(nx-1)) + (B**2/(ny-1))
  gl <- glnum/glden
  
  tden <- sqrt(A + B)
  t <- (xb - yb)/tden
  
  return(c(t, gl)) # t ~ t( gl )
}

# amostra
thmedia3a <- function(x, y){
  nx <- length(x)
  ny <- length(y)
  xb <- mean(x)
  yb <- mean(y)
  varx <- var(x)
  vary <- var(y)
  
  A <- varx/nx
  B <- vary/ny
  glnum <- (A + B)**2
  glden <- (A**2/(nx-1)) + (B**2/(ny-1))
  gl <- glnum/glden
  
  tden <- sqrt(A + B)
  t <- (xb - yb)/tden
  
  return(c(t, gl)) # t ~ t( gl )
}

'Teste 4 - para variância'
# input
thvar <- function(varx, vary){
  return(varx/vary)
}


# amostra
thvar <- function(x, y){
  nx <- length(x)
  ny <- length(y)
  print('F()')
  print(c(nx-1, ny-1))
  varx <- var(x)
  vary <- var(y)
  return(varx/vary)
}


'Faz seus teste ai mano '






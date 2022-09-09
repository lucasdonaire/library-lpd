library(plotly)
### PLOTLY

'grafico de função'

x <- seq(0,5, length.out = 101) # (a, b), e pode aumentar a qtd de pontos
random_y <- exp(x) # a função aplicada em x

# nao muda abaixo.

data <- data.frame(x, random_y)
fig <- plot_ly(data, x = ~x, y = ~random_y, type = 'scatter', mode = 'lines')
fig


'mais de uma funcao'

x <- seq(-100,100)
y1 <- dnorm(x, sd = 10)
y2 <- dnorm(x, sd = 20) 
data <- data.frame(x, y1, y2)
fig <- plot_ly(data, x = ~x, y = ~y1, type = 'scatter', mode = 'lines')
fig <- fig %>% add_trace(y = ~y2, name = 'trace 1', mode = 'lines')
fig


'histograma/histogramas'


fig <- plot_ly(alpha = 0.6)
fig <- fig %>% add_histogram(x = ~rnorm(500), xbins = list(size = 1000)) # x = dados. 
#size dos xbins = grossura das barras
fig <- fig %>% add_histogram(x = ~rnorm(500) + 1)
fig <- fig %>% layout(barmode = "overlay")

fig


'grafico de barras'

Animals <- c("giraffes", "orangutans", "monkeys")
SF_Zoo <- c(20, 14, 23)
LA_Zoo <- c(12, 18, 29)
data <- data.frame(Animals, SF_Zoo, LA_Zoo)

fig <- plot_ly(data, x = ~Animals, y = ~SF_Zoo, type = 'bar', name = 'SF Zoo')
fig <- fig %>% add_trace(y = ~LA_Zoo, name = 'LA Zoo')
fig <- fig %>% layout(yaxis = list(title = 'Count'), barmode = 'group')

fig



'dataframe para tabela'


fig <- plot_ly(
  type = 'table',
  columnwidth = c(80,160,160,80,100,80,80), # grossura colunas
  header = list(
    values = c( names(dftotal)),
    line = list(color = '#506784'),
    fill = list(color = '#119DFF'),
    height = 70 # grossura primeira linha
  ),
  cells = list(
    values = t(as.matrix(unname(dftotal))),
    line = list(color = '#506784'),
    fill = list(color = c('#25FEFD', 'white')),
    height = 40 # grossura demais linhas
  )
)

fig

'superficie 3d'

x <- -40:40 
y <- -40:40
z <- outer(x,y, function(x,y){x+y+x*y/10}) 
fig <- plot_ly(x = ~x, y = ~y, z = ~z, type = 'surface') ; fig


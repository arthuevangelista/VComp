# EDP

  A equação do calor pode ser utilizada para aplicação de filtros em imagens. Considera-se uma imagem como sendo uma função F(x,y). A função de calor será 

    Calor = Fxx + Fyy

   Onde Fxx é a segunda derivada de F(x,y) em relação a x; e
   Fyy é a segunda derivada de F(x,y) em relação a y.

  E a solução para esta equação pode ser encontrado numericamente à partir do método de Runge-Kutta ou Euler. Pelo método de Euler temos que:

    F(x,y) = F(x,y) + h * Calor

  Onde h é um espaçamento. Geralmente o valor de h será muito pequeno, por volta de 0.25, 0.01 e assim por diante. A escolha do valor de h é no chute. Seu valor determina a influência das derivadas. A função de calor nada mais é que o filtro da média. O efeito é semelhante ao filtro de blur (desfoque/borrar a imagem). Nos slides tem alguma parada sobre difusão? Não sei que porra é essa... Dar uma olhada no livro.

  Os algoritmos que calculam EDPs estão praticamente extintos uma vez que redes neurais foram aperfeiçoadas. O custo computacional e a demora para aquisição de resultados foram os principais fatores para sua extinção. Em compensação, estes algoritmos geralmente tem resultados mais acurados a cada iteração se comparado com convoluções e/ou redes neurais.

# CONVOLUÇÃO

  Assim como com vetores, a convolução funciona da mesma maneira com matrizes. A matriz de convolução é chamada de kernel da convolução onde o centro da matriz é o pixel atual do mapeamento. A forma da matriz (ou do kernel) determina a maneira que a imagem irá se comportar. Todas as operações/filtros vistos anteriormente podem ser substituídos por matrizes de convolução
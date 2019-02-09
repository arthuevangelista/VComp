# ==========================================================
# Importação das bibliotecas necessárias
# ==========================================================
import cv2
import mahotas
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('plant4.jpg')

linhas, colunas, C = img.shape

# ==========================================================
# Separa os canais de cor
# ==========================================================
B = img[:,:,0] # BLUE
G = img[:,:,1] # GREEN
R = img[:,:,2] # RED

copiaGG = np.zeros((linhas, colunas), dtype=int)

for i in range(linhas):
    for j in range(colunas):
        copiaGG[i,j] = np.uint8(np.absolute(0.441*np.float64(R[i,j]) - 0.811*np.float64(G[i,j]) + 0.385*np.float64(B[i,j]) + 18.787))

copiaG = np.uint8(cv2.normalize(copiaGG, None, 0, 255, cv2.NORM_MINMAX))

# ==========================================================
# Histograma
# ==========================================================
# Cria um objeto do tipo CLAHE
claheObj = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe = claheObj.apply(copiaG)

# ==========================================================
# Suavização
# ==========================================================
sigma = 7
suaveGauss = cv2.GaussianBlur(clahe, ( sigma, sigma), 0)

# ==========================================================
# Limiarização
# ==========================================================
# Limiarização utilizando o método de Otsu
T = mahotas.thresholding.otsu(suaveGauss)
otsu = suaveGauss.copy()
# Transforma regiões que sejam maiores que o threshold de otsu em branco
otsu[otsu > T] = 255
# Transforma regiões que sejam menores que o threshold de otsu em preto
otsu[otsu < 255] = 0

# ==========================================================
# Detecção de Bordas
# ==========================================================
canny = cv2.Canny(suaveGauss, 50, 150)

# ==========================================================
# Aplicação das Hough Lines
# ==========================================================
imgHough = img.copy()

rho = 1
theta = np.pi / 180
limiar = 100
minTam = 25
maxGap = 250

lines = cv2.HoughLinesP(canny, rho, theta, limiar, np.array([]),
                    minTam, maxGap)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(imgHough,(x1,y1),(x2,y2),(255,0,0),2)

# ==========================================================
# Fechamento
# ==========================================================
fech = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))
resultado = cv2.bitwise_and(img,img,mask = fech)

# ==========================================================
# PLOT
# ==========================================================

plt.title("Imagem original")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

plt.gray()
plt.title("Detecção de bordas.")
plt.imshow(canny)
plt.show()

plt.title("Segmentação utilizando Otsu.")
plt.imshow(cv2.cvtColor(cv2.bitwise_and(img,img,mask = otsu),cv2.COLOR_BGR2RGB))
plt.show()

plt.title("Segmentação utilizando Canny e fechamento.")
plt.imshow(cv2.cvtColor(resultado,cv2.COLOR_BGR2RGB))
plt.show()

plt.title("Hough lines")
plt.imshow(cv2.cvtColor(imgHough,cv2.COLOR_BGR2RGB))
plt.show()
# funcao3.py
import cv2
import os

def funcao3():
    # Cria a pasta para salvar os resultados, se não existir
    os.makedirs("resultados", exist_ok=True)
    
    # Carrega a imagem original
    img_path = "imagem_exame.jpg"
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Erro: não foi possível carregar a imagem {img_path}")
        return

    # 5. Redimensionamento e Interpolação
    # Redimensionar para 50% do tamanho original com interpolação bicúbica
    width_50 = int(img.shape[1] * 0.5)
    height_50 = int(img.shape[0] * 0.5)
    img_50 = cv2.resize(img, (width_50, height_50), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("resultados/redimensionada_50.jpg", img_50)
    
    # Redimensionar para 200% do tamanho original com interpolação linear
    width_200 = int(img.shape[1] * 2)
    height_200 = int(img.shape[0] * 2)
    img_200 = cv2.resize(img, (width_200, height_200), interpolation=cv2.INTER_LINEAR)
    cv2.imwrite("resultados/redimensionada_200.jpg", img_200)
    
    # 6. Transformações Geométricas
    # a) Rotacionar a imagem em 45° mantendo o tamanho original
    (h, w) = img.shape[:2]
    centro = (w // 2, h // 2)
    matriz_rotacao = cv2.getRotationMatrix2D(centro, 45, 1.0)
    img_rotacionada = cv2.warpAffine(img, matriz_rotacao, (w, h))
    cv2.imwrite("resultados/rotacionada_45.jpg", img_rotacionada)
    
    # b) Espelhar a imagem horizontalmente
    img_espelhada = cv2.flip(img, 1)
    cv2.imwrite("resultados/espelhada.jpg", img_espelhada)
    
    # c) Recortar um retângulo central de 300x300 pixels
    center_y, center_x = h // 2, w // 2
    half_crop = 150  # metade de 300
    start_x = max(center_x - half_crop, 0)
    start_y = max(center_y - half_crop, 0)
    end_x = start_x + 300
    end_y = start_y + 300

    # Ajusta os limites se ultrapassar o tamanho da imagem
    if end_x > w:
        end_x = w
        start_x = w - 300
    if end_y > h:
        end_y = h
        start_y = h - 300
        
    img_cortada = img[start_y:end_y, start_x:end_x]
    cv2.imwrite("resultados/retangulo_central.jpg", img_cortada)
    
    # 7. Binarização utilizando o método Otsu em uma imagem em escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite("resultados/binarizada_otsu.jpg", img_otsu)
    
    print("Funcao3: Redimensionamento, transformações geométricas e binarização concluídos.")

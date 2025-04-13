# funcao2.py
import cv2
import os
import numpy as np

def funcao2():
    # Cria a pasta para salvar os resultados, se não existir
    os.makedirs("resultados", exist_ok=True)
    
    # Carrega a imagem original
    img_path = "imagem_exame.jpg"
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Erro: não foi possível carregar a imagem {img_path}")
        return

    # 3. Modificação de Cores: Converter para o espaço de cores HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Aumentar a saturação (canal S) em 30%
    h, s, v = cv2.split(img_hsv)
    s = s.astype(np.float32) * 1.3  # aumenta 30%
    s[s > 255] = 255  # limitar o valor máximo
    s = s.astype(np.uint8)
    
    # Recombinar os canais e converter de volta para BGR
    img_hsv_mod = cv2.merge((h, s, v))
    img_saturacao = cv2.cvtColor(img_hsv_mod, cv2.COLOR_HSV2BGR)
    
    # Salvar a imagem com saturação aumentada
    cv2.imwrite("resultados/saturacao_aumentada.jpg", img_saturacao)
    
    # 4. Ajuste de Contraste e Brilho
    # Parâmetros: alpha = fator de contraste, beta = incremento do brilho
    alpha = 1.2  # pode ser ajustado conforme necessário
    beta = 50    # aumento de 50 unidades no brilho
    
    # Aplicar transformação linear: nova_imagem = alpha*imagem + beta
    img_ajustada = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    
    # Salvar a imagem com contraste e brilho ajustados
    cv2.imwrite("resultados/contraste_brilho.jpg", img_ajustada)
    
    print("Funcao2: Modificação de cores e ajustes de contraste/brilho concluídos.")

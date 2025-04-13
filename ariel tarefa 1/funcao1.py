# funcao1.py
import cv2
import os

def funcao1():
    # Cria a pasta para salvar os resultados, se não existir
    os.makedirs("resultados", exist_ok=True)
    
    # 1. Leitura e Exibição Inicial
    img_path = "imagem_exame.jpg"
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Erro: não foi possível carregar a imagem '{img_path}'. Verifique se o arquivo existe e o caminho está correto.")
        return
    
    # Exibe a imagem original (a janela será fechada quando uma tecla for pressionada)
    cv2.imshow("Imagem Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Salva a imagem original na pasta de resultados
    cv2.imwrite("resultados/original.jpg", img)
    
    # 2. Pré-processamento: Converter para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar equalização de histograma para realçar detalhes
    img_eq = cv2.equalizeHist(img_gray)
    
    # Salvar as imagens intermediárias
    cv2.imwrite("resultados/gray.jpg", img_gray)
    cv2.imwrite("resultados/equalizada.jpg", img_eq)
    
    print("Funcao1: Leitura e pré-processamento concluídos.")

# Chamada da função principal
if __name__ == "__main__":
    funcao1()
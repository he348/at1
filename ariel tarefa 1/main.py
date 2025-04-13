# main.py
import funcao1
import funcao2
import funcao3

def main():
    print("Iniciando o pipeline de processamento de imagens...")
    
    # Executa cada módulo de processamento
    funcao1.funcao1()
    funcao2.funcao2()
    funcao3.funcao3()
    
    print("Pipeline concluído. Verifique a pasta 'resultados' para as imagens geradas.")

if __name__ == "__main__":
    main()

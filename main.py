import tkinter as tk
from tkinter import messagebox
from validate_docbr import CPF
import os
from config import configuracoes
from PIL import Image, ImageTk

def validar_cpf():
    cpf = entry_cpf.get()
    cpf_validator = CPF()

    if cpf_validator.validate(cpf):
        caminho_pasta = configuracoes['caminho_pasta']

        try:
            arquivos = os.listdir(caminho_pasta)
            verificar = False

            for arquivo in arquivos:
                if cpf in arquivo:
                    verificar = True
                    caminho_arquivo = os.path.join(caminho_pasta, arquivo)

                    try:
                        os.remove(caminho_arquivo)
                        messagebox.showinfo("Aviso", f"Usuário {cpf} Derrubado")
                    except PermissionError:
                        messagebox.showerror("Erro", f"Permissão negada ao remover {caminho_arquivo}")

                    break

            if not verificar:
                messagebox.showinfo("Aviso", f"Usuário {cpf} não encontrado!")
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Diretório {caminho_pasta} não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")

    else:
        messagebox.showwarning("Aviso", f"O CPF {cpf} é inválido!")

janela = tk.Tk()

try:
    ico = Image.open('dist/icon.png')
    photo = ImageTk.PhotoImage(ico)
    janela.wm_iconphoto(False, photo)
except:
    print('Imagem nao encontrada')

janela.title("Validação e Remoção de Usuário")

label_cpf = tk.Label(janela, text="CPF:")
label_cpf.grid(row=0, column=0, padx=40, pady=40)

entry_cpf = tk.Entry(janela)
entry_cpf.grid(row=0, column=1, padx=40, pady=40)

botao_validar = tk.Button(janela, text="Validar CPF", command=validar_cpf)
botao_validar.grid(row=1, column=0, columnspan=2, pady=40)

janela.mainloop()

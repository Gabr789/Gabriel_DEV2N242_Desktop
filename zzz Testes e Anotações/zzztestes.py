import sys
print("\n", sys.executable)


# ---

# # 🎨 Atributos de Aparência por Widget

# ---

# ## 🔹 Comuns a quase todos (`Frame`, `Label`, `Button`, `Entry`)

# * **`bg` / `background`** → Cor de fundo.
# * **`fg` / `foreground`** → Cor do texto (não funciona em `Frame`).
# * **`font`** → Fonte (`("Arial", 12, "bold")`).
# * **`bd` / `borderwidth`** → Espessura da borda (px).
# * **`relief`** → Estilo da borda (`flat`, `raised`, `sunken`, `groove`, `ridge`, `solid`).
# * **`cursor`** → Cursor do mouse (`arrow`, `hand2`, `xterm`, etc.).
# * **`highlightthickness`** → Espessura da borda de foco.
# * **`highlightbackground`** → Cor da borda quando **sem foco**.
# * **`highlightcolor`** → Cor da borda quando **com foco**.
# * **`takefocus`** → Define se pode receber foco de teclado (`True`/`False`).

# ---

# ## 🔹 `Frame`

# É mais "contenção" do que widget visual, mas tem:

# * Todos os comuns.
# * Usado muito com `bg`, `relief`, `bd`, `cursor`.

# ---

# ## 🔹 `Label`

# Além dos comuns:

# * **`text`** → Texto exibido.
# * **`image`** → Imagem (`PhotoImage` ou `BitmapImage`).
# * **`compound`** → Combinação imagem + texto (`left`, `right`, `top`, `bottom`, `center`).
# * **`justify`** → Alinhamento de múltiplas linhas (`left`, `right`, `center`).
# * **`anchor`** → Posição do conteúdo dentro do widget (`n`, `s`, `e`, `w`, `ne`, `sw`, `center`, etc.).
# * **`padx`, `pady`** → Espaçamento interno do texto (px).
# * **`wraplength`** → Comprimento em pixels antes de quebrar a linha.

# ---

# ## 🔹 `Button` (e derivados: `Checkbutton`, `Radiobutton`)

# Além dos comuns e dos herdados de `Label`:

# * **`activebackground`** → Cor de fundo quando ativo/pressionado.
# * **`activeforeground`** → Cor do texto quando ativo.
# * **`disabledforeground`** → Cor do texto quando desabilitado.
# * **`anchor`** → Alinhamento do conteúdo dentro do botão.
# * **`compound`** → Texto + imagem juntos (como no `Label`).
# * **`padx`, `pady`** → Espaçamento interno.
# * **`width`, `height`** → Tamanho em caracteres (não pixels).
# * **`bitmap`** → Ícone simples em bitmap (além de `image`).

# *(Obs.: `Checkbutton` e `Radiobutton` têm os mesmos atributos visuais, mas com extras funcionais — `indicatoron`, `selectcolor`, `onvalue`, etc.)*

# ---

# ## 🔹 `Entry`

# Além dos comuns:

# * **`justify`** → Alinhamento do texto (`left`, `center`, `right`).
# * **`show`** → Máscara para caracteres (ex.: `"*"` para senha).
# * **`insertbackground`** → Cor do cursor de inserção.
# * **`insertwidth`** → Largura do cursor de inserção.
# * **`selectbackground`** → Cor de fundo do texto selecionado.
# * **`selectforeground`** → Cor do texto selecionado.
# * **`disabledbackground`** → Cor de fundo quando desabilitado.
# * **`disabledforeground`** → Cor do texto quando desabilitado.
# * **`readonlybackground`** → Cor de fundo em estado somente leitura.

# ---

# # 📌 Resumo em tabela

# | Widget     | Atributos principais de aparência                                                                                                                                      |
# | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **Frame**  | bg, bd, relief, cursor, highlight…                                                                                                                                     |
# | **Label**  | text, image, compound, fg, font, anchor, justify, padx/pady, wraplength                                                                                                |
# | **Button** | bg, fg, font, relief, activebackground, activeforeground, disabledforeground, image, compound, anchor, padx/pady, width/height                                         |
# | **Entry**  | bg, fg, font, bd, relief, justify, show, insertbackground, insertwidth, selectbackground, selectforeground, disabledbackground, disabledforeground, readonlybackground |

# ---

# 👉 Quer que eu prepare um **código exemplo** que mostre todos esses atributos em ação (um mini “catálogo visual” de estilos para Frame, Label, Button e Entry)?
























        # """Frame Enunciado"""

        # frame_enunciado = tk.Frame(
        #     self.janela,
        #     width=600,
        #     height=200,
        #     highlightbackground="black",
        #     highlightthickness=3
        # )
        # frame_enunciado.pack_propagate(False)
        # frame_enunciado.pack(pady=20)

        # enunciado = tk.Text(frame_enunciado, wrap="word", font=("Arial", 10))
        # enunciado.insert(
        #     "1.0",
        #     "\n Exercício 02\n"
        #     "\n   Crie um formulário de login usando Frame,"
        #     " com os campos Usuário e Senha e um botão Entrar.\n"
        #     "\n   Ao clicar em Entrar, mostre uma mensagem de sucesso"
        #     " se a senha for 1234 ou de erro, se for diferente."
        # )
        # enunciado.pack(fill="both")
        # enunciado.config(state="disabled")

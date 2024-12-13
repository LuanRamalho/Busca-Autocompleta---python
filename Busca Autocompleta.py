import tkinter as tk
from tkinter import ttk

# Lista de países
countries = [
    'África do Sul', 'Angola', 'Argélia', 'Benin', 'Botsuana', 'Burkina Faso', 
    'Burundi', 'Camarões', 'Cabo Verde', 'República Centro Africana', 'Chade', 
    'Comoros', 'República do Congo', 'República Democrática do Congo', 'Costa do Marfim', 
    'Djibuti', 'Egito', 'Eritreia', 'Eswatini', 'Etiópia', 'Gabão', 'Gâmbia', 
    'Gana', 'Guiné', 'Guiné-Bissau', 'Guiné Equatorial', 'Lesoto', 'Libéria', 'Líbia', 
    'Madagascar', 'Malauí', 'Mali', 'Mauritânia', 'Maurício', 'Mayotte', 'Marrocos', 
    'Moçambique', 'Namíbia', 'Níger', 'Nigéria', 'Quênia', 'Reunião', 'Ruanda', 
    'Saara do Oeste', 'Santa Helena', 'São Tomé e Príncipe', 'Senegal', 'Seychelles', 
    'Serra Leoa', 'Somália', 'Sudão', 'Sudão do Sul', 'Tanzânia', 'Togo', 'Tunísia', 
    'Uganda', 'Zâmbia', 'Zimbábue', 'Afeganistão', 'Arábia Saudita', 'Armênia', 
    'Azerbaijão', 'Bahrein', 'Bangladesh', 'Brunei', 'Butão', 'Camboja', 'Cazaquistão', 
    'Coréia do Norte', 'Coréia do Sul', 'China', 'Emirados Árabes Unidos', 'Filipinas', 
    'Hong Kong', 'Iemen', 'Índia', 'Indonésia', 'Irã', 'Iraque', 'Israel', 'Japão', 
    'Jordânia', 'Kuwait', 'Laos', 'Líbano', 'Macau', 'Malásia', 'Maldivas', 'Mianmar', 
    'Mongólia', 'Nepal', 'Omã', 'Palestina', 'Paquistão', 'Qatar', 'Quirguistão', 
    'Singapura', 'Síria', 'Sri Lanka', 'Tadjiquistão', 'Tailândia', 'Taiwan', 
    'Timor Leste', 'Turcomenistão', 'Turquia', 'Uzbequistão', 'Vietnã', 'Albânia', 
    'Alemanha', 'Andorra', 'Áustria', 'Belarus', 'Bélgica', 'Bósnia-Herzegovina', 
    'Bulgária', 'Chipre', 'Croácia', 'República Tcheca', 'Dinamarca', 'Escócia', 
    'Eslováquia', 'Eslovênia', 'Espanha', 'Estônia', 'Finlândia', 'França', 'Geórgia', 
    'Gibraltar', 'Grécia', 'Groenlândia', 'Holanda', 'Hungria', 'Inglaterra', 'Irlanda', 
    'Irlanda do Norte', 'Islândia', 'Itália', 'Kosovo', 'Letônia', 'Liechtenstein', 
    'Lituânia', 'Luxemburgo', 'Macedônia', 'Malta', 'Moldávia', 'Mônaco', 'Montenegro', 
    'Noruega', 'País de Gales', 'Polônia', 'Portugal', 'Reino Unido', 'Romênia', 'Rússia', 
    'San Marino', 'Sérvia', 'Suécia', 'Suiça', 'Ucrânia', 'Vaticano', 'Ilhas Aland', 
    'Ilhas Faroe', 'Canadá', 'Estados Unidos', 'México', 'Anguilla', 'Antígua e Barbuda', 
    'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Costa Rica', 'Cuba', 'Curaçao', 'Dominica', 
    'República Dominicana', 'El Salvador', 'Granada', 'Guadalupe', 'Guatemala', 'Haiti', 
    'Honduras', 'Jamaica', 'Martinica', 'Montserrat', 'Nicarágua', 'Panamá', 'Porto Rico', 
    'São Bartolomeu', 'São Cristóvão e Nevis', 'Santa Lucia', 'São Martinho', 
    'São Vicente e Granadinas', 'Trinidad e Tobago', 'Ilhas Bermudas', 'Ilhas Cayman', 
    'Ilhas Turks e Caicos', 'Ilhas Virgens Britânicas', 'Ilhas Virgens Americanas', 
    'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 
    'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 
    'Ilhas Falkland (Ilhas Malvinas)', 'Austrália', 'Fiji', 'Guam', 'Kiribati', 'Micronésia', 
    'Nauru', 'Niue', 'Nova Caledônia', 'Nova Zelândia', 'Palau', 'Papua Nova Guiné', 
    'Polinésia Francesa', 'Samoa', 'Samoa Americana', 'Tokelau', 'Tonga', 'Tuvalu', 
    'Vanuatu', 'Wallis e Futuna', 'Ilhas Christmas', 'Ilhas Cocos', 'Ilhas Cook', 
    'Ilhas Mariana do Norte', 'Ilhas Marshall', 'Ilhas Norfolk', 'Ilhas Salomão', 'Antártida'
]

class AutocompleteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Busca Autocompleta - Países")
        self.root.geometry("600x400")
        self.root.configure(bg="#03BBFF")
        
        self.input_var = tk.StringVar()
        
        # Entry field
        self.entry = ttk.Entry(self.root, textvariable=self.input_var, width=50, font=('Helvetica', 14))
        self.entry.pack(pady=10)
        
        # Listbox for autocomplete suggestions
        self.autocomplete_list = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE, font=('Helvetica', 12))
        self.autocomplete_list.pack(pady=5)
        
        # Label to display selected country
        self.selected_label = tk.Label(self.root, text="", font=('Helvetica', 12, "bold"), bg="#03BBFF", fg="#7604B7")
        self.selected_label.pack(pady=10)
        
        # Bindings
        self.entry.bind("<KeyRelease>", self.on_key_release)
        self.autocomplete_list.bind("<<ListboxSelect>>", self.on_select)
        self.entry.bind("<Return>", self.on_enter)
        self.root.bind("<FocusOut>", self.on_focus_out)
    
    def on_key_release(self, event):
        query = self.input_var.get().lower()
        if query:
            suggestions = [country for country in countries if query in country.lower()]
            self.autocomplete_list.delete(0, tk.END)
            for country in suggestions:
                self.autocomplete_list.insert(tk.END, country)
        else:
            self.autocomplete_list.delete(0, tk.END)
    
    def on_select(self, event):
        try:
            selected_item = self.autocomplete_list.get(self.autocomplete_list.curselection())
            self.selected_label.config(text=f"País Selecionado: {selected_item}")
        except IndexError:
            pass
    
    def on_enter(self, event):
        selected_item = self.autocomplete_list.get(self.autocomplete_list.curselection())
        if selected_item:
            self.input_var.set(selected_item)
            self.autocomplete_list.delete(0, tk.END)
            self.selected_label.config(text=f"País Selecionado: {selected_item}")
    
    def on_focus_out(self, event):
        root_x = self.autocomplete_list.winfo_rootx()
        root_y = self.autocomplete_list.winfo_rooty()
        end_x = root_x + self.autocomplete_list.winfo_width()
        end_y = root_y + self.autocomplete_list.winfo_height()
        
        if not (root_x <= event.x_root <= end_x and root_y <= event.y_root <= end_y):
            self.autocomplete_list.destroy()


# Criar a janela principal
root = tk.Tk()
app = AutocompleteApp(root)
root.mainloop()

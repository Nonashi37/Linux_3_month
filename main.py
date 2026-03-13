# import flet as ft 
# import datetime 

# def main(page: ft.Page):
#     page.title = 'Мое первое приложение На Флет!'
#     page.theme_mode = ft.ThemeMode.DARK

#     greeting_history = []

#     history_text = ft.Text(value="History of greeting:")

#     text_hello = ft.Text(value='Как дела')


#     def on_click_func(_):
#         name = name_input.value

#         if name:
#             now = datetime.datetime.now()
#             time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            
#             new_message = f"{time_string} - Hello, {name}!"
            
#             text_hello.value = f'Приветствую {name}'
#             text_hello.color = None


#             greeting_history.append(new_message)

#             name_input.value = None


#             history_text.value = "History of greetings: \n" + "\n".join(greeting_history)

#         else: 
#             text_hello.color = ft.Colors.YELLOW
#             text_hello.value = 'Введите Имя, Пж'

#         page.update()

#     name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
#     elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)

#     def edit_theme(_):
#         if page.theme_mode == ft.ThemeMode.DARK:
#             page.theme_mode = ft.ThemeMode.LIGHT
#         else:
#             page.theme_mode = ft.ThemeMode.DARK
#         page.update()
    

#     def delete_Button(_):
#         greeting_history.clear()
#         history_text.value = "History of greeting:" 
#         page.update() 

#     theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)

#     delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_Button)

#     main_objects = ft.Row([name_input, elevated_button, theme_button, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

#     page.add(text_hello, main_objects, history_text)

# ft.app(main)


# import flet as ft

# def main(page: ft.Page):
#     page.title = " Flett Clicker"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER # Центрируем все
#     text_field = ft.Text(value = "Click", size=20)

#     def button_clicked(e):
#         text_field.value = "Boom"
#         page.update()

#     on_click_btn = ft.ElevatedButton(text)

#     # here controllers vidgets
#     page.add(ft.Text("Hello, Senior!"))

#     # Запуск app
#     ft.app(target=main)



# import flet as ft 
# import datetime 
# import os 

# def main(page: ft.Page):
#     page.title = 'Мое первое приложение На Флет!'
#     page.theme_mode = ft.ThemeMode.DARK

#     greeting_history = []


#     if os.path.exists("history.txt"):
#         file = open("history.txt", "r", encoding="utf-8")
#         for line in file.readlines():
#             greeting_history.append(line.strip())
#         file.close()

#     history_text = ft.Text(value="History of greetings: \n" + "\n".join(greeting_history))

#     text_hello = ft.Text(value='Как дела')

#     def on_click_func(_):
#         name = name_input.value

#         if name:
#             now = datetime.datetime.now()
#             time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            
#             new_message = f"{time_string} - Hello, {name}!"
            
#             text_hello.value = f'Приветствую {name}'
#             text_hello.color = None

#             greeting_history.append(new_message)

        
#             file = open("history.txt", "a", encoding="utf-8") # "a" means append
#             file.write(new_message + "\n")
#             file.close()
        

#             name_input.value = None
#             history_text.value = "History of greetings: \n" + "\n".join(greeting_history)

#         else: 
#             text_hello.color = ft.Colors.YELLOW
#             text_hello.value = 'Введите Имя, Пж'

#         page.update()

#     name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
#     elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)

#     def edit_theme(_):
#         if page.theme_mode == ft.ThemeMode.DARK:
#             page.theme_mode = ft.ThemeMode.LIGHT
#         else:
#             page.theme_mode = ft.ThemeMode.DARK
#         page.update()
    
#     def delete_Button(_):
#         greeting_history.clear()
        
        
#         file = open("history.txt", "w", encoding="utf-8")
#         file.write("")
#         file.close()
    

#         history_text.value = "History of greeting:" 
#         page.update() 

#     theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
#     delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_Button)

#     main_objects = ft.Row([name_input, elevated_button, theme_button, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

#     page.add(text_hello, main_objects, history_text)

# ft.app(main)



# import flet as ft
# import asyncio

# async def main(page: ft.Page):
#     page.title = "Seniore Admine"
#     # This is where your FastAPI brain shines
#     status = ft.Text("System Idle", color="blue")

#     async def run_migration(e):
#         status.value = " Running DB migrations. . ."
#         status.color = 'orange'
#         page.update()

#         await asyncio.sleep(2) # simulationg heavy backend work

#         status.value = " success! Pruduction is safe. . . for now."
#         status.color = "green"
#         page.update()

#     page.add(
#         ft.Text("Senior Admin Panel", size=30, weight="bold"),
#         status,
#         ft.ElevatedButton("Deploy to Prod", on_click=run_migration)
#     )

# ft.app(target=main)




import flet as ft
import datetime
import os

def main(page: ft.Page):
    page.title = 'Flet Pro App'
    page.theme_mode = ft.ThemeMode.SYSTEM

    greeting_history = []

    # using 'with' - closese the file automatically
    if os.path.exists("history.txt"):
        with open("history.txt", "r", encoding="utf-8") as file:
            greeting_history = [line.strip() for line in file.readlines()]

    history_text = ft.Text(value="History of greetings: \n" + "\n".join(greeting_history) if greeting_history else "History is empty")
    text_hello = ft.Text(value='Ready to greet')

    def update_history_ui():
        """Helper to sync UI with the list state"""
        if not greeting_history:
            history_text.value = "History is empty"
        else:
            history_text.value = "History of greetings: \n" + "\n".join(greeting_history)
        page.update()

    def sync_to_file():
        """Overwrite the file with current history"""
        with open("history.txt", "w", encoding="utf-8") as file:
            # Join with new line and write
            file.write("\n".join(greeting_history) + ("\n" if greeting_history else ""))

    def on_send_click(_):
        name = name_input.value
        if name:
            now = datetime.datetime.now()
            time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            new_message = f"{time_string} - Hello, {name}"

            text_hello.value = f" |Приветствую теюя {name}! "
            text_hello.color = None

            greeting_history.append(new_message)

            # Append mode for efficiency when adding
            with open("history.txt", "a", encoding="utf-8") as file:
                file.write(new_message + "\n")

                name_input.value = ""
                update_history_ui()
        else:
            text_hello.color = ft.Colors.YELLOW
            text_hello.value = "Введите Имя"
            page.update()

    def delete_last_item(_):
        if greeting_history:
            greeting_history.pop( ) # remove the last element
            sync_to_file()
            update_history_ui()
        else:
            history_text.value = "History is empty"
            page.update()

    def clear_all_history(_):
        greeting_history.clear()
        sync_to_file
        update_history_ui()

    def toggle_theme(_):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode. DARK else ft.ThemeMode.DARK
        page.update()

    # UI Components
    name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_send_click)
    send_btn = ft.ElevatedButton('Send', icon=ft.Icons.SEND, on_click=on_send_click)
    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)
    
    # new buttons
    delete_last_btn = ft.IconButton(icon=ft.Icons.UNDO, on_click=delete_last_item, tooltip="Delete Last")
    clear_all_btn = ft.IconButton(icon=ft.Icons.DELETE_SWEEP, on_click=clear_all_history, tooltip="Clear All", icon_color=ft.Colors.RED_400)

    controls_row = ft.Row(
        [name_input, send_btn, theme_btn, delete_last_btn, clear_all_btn], 
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    page.add(text_hello, controls_row, history_text)

ft.app(target=main)
# import flet as ft 



# def main(page: ft.Page):
#     page.title = 'Мое первое приложение На Флет!'
#     page.theme_mode = ft.ThemeMode.DARK

#     greeting_history = []

#     history_text = ft.Text(value="History of greeting:")

#     text_hello = ft.Text(value='Как дела')


#     def on_click_func(_):
#         # print(name_input.value)
#         name = name_input.value

#         if name:
#             # text_hello.value = 'Hello ' + name_input.value 
#             text_hello.value = f'Приветствую {name}'
#             text_hello.color = None

#             greeting_history.append(name)

#             name_input.value = None

#             history_text.value = "History of greetinggs: \n" + "\n".join(greeting_history)

#         else: 
#             text_hello.color = ft.Colors.YELLOW
#             text_hello.value = 'Введите Имя, Пж'


#         page.update()

#     name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
#     elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)

#     # text_button = ft.TextButton(text='send', icon=ft.Icons.SEND, icon_color=ft.Colors.GREEN)
#     # icon_button = ft.IconButton(icon=ft.Icons.SEND, icon_color=ft.Colors.RED)

#     def edit_theme(_):
#         if page.theme_mode == ft.ThemeMode.DARK:
#             page.theme_mode = ft.ThemeMode.LIGHT
#         else:
#             page.theme_mode = ft.ThemeMode.DARK
#         page.update()
    
#     def delete_Button(_):
#         if history_text:
#             history_text.clear()


#     theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)

#     delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_Button)

#     main_objects = ft.Row([name_input, elevated_button, theme_button, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

#     page.add(text_hello, main_objects, history_text)



# # ft.app(main)
# ft.app(main, view=ft.AppView.WEB_BROWSER)\





# import flet

# class Colors:
#     BACKGROUNG = '#e2e4e5'
#     ICON = '#6c7072'

# def main(page:flet.Page):
#     page.window.width = 520
#     page.window.height = 690
#     page.padding = 0
#     page.bgcolor = 'black'
#     page.vertical_alignment = 'center'
#     page.horizontal_alignment = 'center'
#     menu_button = flet.IconButton(
#         flet.Icons.MENU_ROUNDED,
#         icon_color=Colors.ICON,icon_size=26
#     )

#     page.add(
#         flet.Container(
#             content=flet.Stack([
#                 flet.Container(
#                     flet.Row([
#                         menu_button
#                     ],alignment=flet.MainAxisAlignment.END),
#                     padding=flet.padding.all(15)
#                 )
#             ]),
#             width=280,
#             height=590,
#             bgcolor=Colors.BACKGROUNG,
#             border_radius=44
#         )
#     )

# flet.app(main)

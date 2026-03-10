import flet as ft 
import datetime 

def main(page: ft.Page):
    page.title = 'Мое первое приложение На Флет!'
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []

    history_text = ft.Text(value="History of greeting:")

    text_hello = ft.Text(value='Как дела')


    def on_click_func(_):
        name = name_input.value

        if name:
            now = datetime.datetime.now()
            time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            
            new_message = f"{time_string} - Hello, {name}!"
            
            text_hello.value = f'Приветствую {name}'
            text_hello.color = None


            greeting_history.append(new_message)

            name_input.value = None


            history_text.value = "History of greetings: \n" + "\n".join(greeting_history)

        else: 
            text_hello.color = ft.Colors.YELLOW
            text_hello.value = 'Введите Имя, Пж'

        page.update()

    name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)

    def edit_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()
    

    def delete_Button(_):
        greeting_history.clear()
        history_text.value = "History of greeting:" 
        page.update() 

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)

    delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_Button)

    main_objects = ft.Row([name_input, elevated_button, theme_button, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(text_hello, main_objects, history_text)

ft.app(main)





# import flet

# class Colors:
#     BACKGROUNG = '#e2e4e5'
#     ICON = '#6c7072'
#     CONTAINER_BACKGROUND = '#FFFFFF'
#     FOREGROUND = '#0f0f0f'

# class SidebarButton(flet.Container):
#     def __init__(self, label, icon_src):
#         super().__init__()
#         self.content = flet.Container(
#                         flet.Row([
#                             flet.Image(src=icon_src, width=20),
#                             flet.Text(label, font_family="Poppins-Bold", size=14, color=Colors.FOREGROUND)
#                         ]), padding=flet.padding.only(bottom=18)
#                     )

# class Sidebar (flet.Container):
#     def __init__(self):
#         super().__init__()
#         self.content = flet.Column([
#             flet.Container(
#                 flet.Column([
#                     flet.Image(src='https://scontent.ffru4-1.fna.fbcdn.net/v/t39.30808-6/470684072_1184700096353655_4639370321925427747_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=101&ccb=1-7&_nc_sid=13d280&_nc_ohc=1zjrhPWc8NcQ7kNvwF6ldYi&_nc_oc=Adn9srelkxRUssvXVjLAUaApwcyTYWdd2PWEx5Iy_KbzQvtzpS1glrj5EAXnBLpK5Yo&_nc_zt=23&_nc_ht=scontent.ffru4-1.fna&_nc_gid=EG3gAZY1feV_8yoXncv3_g&_nc_ss=8&oh=00_AfxlY-zrV_9ZczbZHOgojY2Ou_NUGkaVi_5vQQcktRnJmw&oe=69B5C3F9', width=70,border_radius=360),
#                     flet.Text(
#                         'Regulus Black',
#                         color=Colors.FOREGROUND, size = 14,
#                         weight='w700', font_family="Poppins-Bold"
#                     ),
#                     flet.Text(
#                         'UX/UI  Designer',
#                         color=Colors.FOREGROUND, size=14,
#                         weight='w500', font_family='Poppins-Bold'
#                     )
#                 ],spacing=5),
#                 padding=flet.padding.only(top=50, left=30, right=15)
#             ),
#             flet.Divider(color=Colors.BACKGROUNG),
#             flet.Container(
#                 flet.Column([
#                     SidebarButton("Home", "https://i.pinimg.com/1200x/2a/6c/fe/2a6cfe0aecf1ba14803f0431ea84a56d.jpg"),
#                     SidebarButton("Topics", "https://i.pinimg.com/736x/10/b1/11/10b11197339ee49f22b3866024dee986.jpg"),
#                     SidebarButton("Messages", "https://i.pinimg.com/736x/be/0a/8d/be0a8d51920adaab2b14638ad4d03518.jpg"),
#                     SidebarButton("Notifications", "https://i.pinimg.com/1200x/f2/46/6a/f2466a5c19a5da65e9440ec182401949.jpg"),
#                     SidebarButton("Bookmarks", "https://i.pinimg.com/474x/f5/ef/cc/f5efccaf1b5f55952669d2135182d4bb.jpg"),
#                     SidebarButton("Profile", "https://i.pinimg.com/1200x/23/cd/56/23cd561f2557c23c099ef25063879ef9.jpg")
#                 ]),
#                 padding=flet.padding.only(left=30, right=15)
#             )
#         ])
#         self.width = 230
#         self.height = 590
#         self.top,self.left = 0,-280
#         self.animate_position = flet.Animation(150, flet.AnimationCurve.EASE_OUT)
#         self.bgcolor = Colors.CONTAINER_BACKGROUND


# def main(page:flet.Page):
#     def open_sidebar(event):
#         sidebar_control.left = 0 if sidebar_control.left != 0 else - 280
#         menu_button.icon = flet.Icons.CHEVRON_LEFT if sidebar_control.left == 0 else flet.Icons.MENU_ROUNDED

#         sidebar_control.update()
#         menu_button.update()
#     page.window.width = 520
#     page.window.height = 690
#     page.padding = 0
#     page.bgcolor = 'black'
#     page.vertical_alignment = 'center'
#     page.horizontal_alignment = 'center'
#     page.fonts = {
#         "Poppins": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf",
#         "Poppins-Bold": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Bold.ttf"
#     }
#     sidebar_control = Sidebar()
#     menu_button = flet.IconButton(
#         flet.Icons.MENU_ROUNDED,
#         icon_color=Colors.ICON,icon_size=26,
#         on_click=open_sidebar
#     )

#     page.add(
#         flet.Container(
#             content=flet.Stack([
#                 flet.Container(
#                     flet.Row([
#                         menu_button
#                     ],alignment=flet.MainAxisAlignment.END),
#                     padding=flet.padding.all(15)
#                 ),
#                 sidebar_control
#             ]),
#             width=280,
#             height=590,
#             bgcolor=Colors.BACKGROUNG,
#             border_radius=44
#         )
#     )

# flet.app(main)

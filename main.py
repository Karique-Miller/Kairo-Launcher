import platform,tkinter
from tkinter import *
from tkinter import ttk,filedialog,messagebox
import os,subprocess,json,sys,ctypes
HAVE_PIL=True
try:
    from PIL import Image,ImageTk
except Exception:
    HAVE_PIL=False
if platform.system()=="Windows":
    myappid='mycompany.myproduct.subproduct.version';ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
SAVE_FILE="games.json";all_game_buttons=[]
TILE_WIDTH=253;TILE_HEIGHT=120
def save_games_to_file(games_list):
    try:
        with open(SAVE_FILE,'w') as f:json.dump(games_list,f,indent=4)
    except IOError as e:print(f"Error saving games file: {e}")
def load_games_from_file():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE,'r') as f:return json.load(f)
        except (IOError,json.JSONDecodeError) as e:print(f"Error loading games file: {e}")
    return []
def reset_save():
    if os.path.exists(SAVE_FILE):os.remove(SAVE_FILE)
    python=sys.executable;os.execl(python,python,*sys.argv)
def main_program():
    window=Tk();window.geometry("500x500");window.title("Kairo Launcher");window.resizable(width=False,height=False)
    try:icon=PhotoImage(file='Icons/Launcher Icon.png');window.iconphoto(True,icon)
    except TclError:print("Icon file not found, continuing without icon.")
    window.config(background="#800000");style=ttk.Style()
    try:
        adder=PhotoImage(file='Icons/adder.png');TWOXKO=PhotoImage(file='Icons/2XKO.png');Valorant=PhotoImage(file='Icons/Valorant.png')
        Skate=PhotoImage(file='Icons/skate.png');Rivals=PhotoImage(file='Icons/Rivals.png');Randomizer=PhotoImage(file='Icons/Randomizer.png')
    except TclError as e:
        print(f"Error loading images: {e}");adder=PhotoImage();TWOXKO=PhotoImage();Valorant=PhotoImage();Skate=PhotoImage();Rivals=PhotoImage();Randomizer=PhotoImage()
    raw_saved=load_games_from_file();saved_games=[]
    for entry in raw_saved:
        if not isinstance(entry,dict):continue
        normalized_entry={"name":entry.get("name","").strip(),"path":entry.get("path",None),"image":entry.get("image",entry.get("img",None)),"is_static":bool(entry.get("is_static",entry.get("static",False))),"removed":bool(entry.get("removed",False))}
        saved_games.append(normalized_entry)
    def find_saved_entry(game_info=None,name=None,path=None):
        if game_info:
            path=game_info.get("path");name=game_info.get("display_name") or game_info.get("name")
        if path:
            for e in saved_games:
                if e.get("path") and os.path.normcase(e.get("path"))==os.path.normcase(path):return e
        if name:
            lower=name.lower()
            for e in saved_games:
                if e.get("name","").lower()==lower:return e
        return None
    def update_or_add_saved_entry(entry):
        existing=None
        if entry.get("path"):
            for e in saved_games:
                if e.get("path") and os.path.normcase(e.get("path"))==os.path.normcase(entry["path"]):existing=e;break
        if not existing and entry.get("name"):
            for e in saved_games:
                if e.get("name","").lower()==entry["name"].lower():existing=e;break
        if existing:existing.update(entry)
        else:saved_games.append(entry)
        save_games_to_file(saved_games)
    def remove_saved_entry_by_path_or_name(game_info):
        entry=find_saved_entry(game_info=game_info)
        if not entry:
            if game_info.get("is_static"):
                new_entry={"name":game_info.get("display_name") or game_info.get("name"),"path":None,"image":None,"is_static":True,"removed":True}
                update_or_add_saved_entry(new_entry)
            return
        if game_info.get("is_static"):
            entry["removed"]=True;update_or_add_saved_entry(entry)
        else:
            try:saved_games.remove(entry);save_games_to_file(saved_games)
            except ValueError:pass
    def reset_game_list():
        search_entry.delete(0,END);search_entry.insert(0,"Search for games...");sort_game_buttons()
        for game_info in all_game_buttons:
            container=game_info['container']
            if container.master is top_frame:continue
            container.pack(pady=25)
        second_frame.update_idletasks();canvas.configure(scrollregion=canvas.bbox("all"));sort_game_buttons()
    def sort_game_buttons():
        sorted_list=sorted([g for g in all_game_buttons if g['container'].master is second_frame],key=lambda x:x['name'])
        for game_info in sorted_list:
            container=game_info['container'];container.pack_forget();container.pack(pady=25)
        second_frame.update_idletasks();canvas.configure(scrollregion=canvas.bbox("all"))
    main_frame=Frame(window);main_frame.pack(fill='both',expand=True)
    canvas=Canvas(main_frame,bg="#800000",borderwidth=0,highlightthickness=0);canvas.pack(side=LEFT,fill='both',expand=True)
    scrollbar=Scrollbar(main_frame,orient=VERTICAL,command=canvas.yview);scrollbar.pack(side=RIGHT,fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set);canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
    second_frame=Frame(canvas,bg="#800000");canvas.create_window((0,0),window=second_frame,anchor="n")
    top_frame=Frame(second_frame,height=70,bg="#800000");top_frame.pack(fill='x');top_frame.pack_propagate(False)
    window_id=canvas.create_window((0,0),window=second_frame,anchor="n")
    def on_canvas_configure(event):canvas.itemconfig(window_id,width=event.width);canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>",on_canvas_configure)
    def _on_mouse_wheel(event):canvas.yview_scroll(-1*int((event.delta/120)),"units")
    canvas.bind_all("<MouseWheel>",_on_mouse_wheel)
    def open_2XKO():
        try:os.startfile(r"C:\Users\Public\Desktop\2XKO.lnk")
        except Exception as e:print(e)
    def open_Randomizer():
        try:os.startfile(r"C:\Users\Apex Gaming Pcs\PycharmProjects\Random Game Generator\Kairo Randomizer\Kairo Randomizer.exe")
        except Exception as e:print(e)
    def open_VALORANT():
        try:os.startfile(r"C:\Users\Public\Desktop\VALORANT.lnk")
        except Exception as e:print(e)
    def open_skate():
        try:os.startfile(r"C:\Users\Apex Gaming Pcs\Desktop\skate..url")
        except Exception as e:print(e)
    def open_rivals():
        try:os.startfile(r"C:\Users\Apex Gaming Pcs\Desktop\Marvel Rivals.url")
        except Exception as e:print(e)
    def launch_game(path):
        try:subprocess.Popen(path,shell=True)
        except Exception as e:print(f"Error launching {path}: {e}")
    def delete_game(game_info):
        display_name=game_info.get('display_name',game_info.get('name','')).strip()
        if not messagebox.askyesno("Delete",f"Delete '{display_name}'?"):return
        container=game_info['container']
        try:container.destroy()
        except Exception:pass
        try:all_game_buttons.remove(game_info)
        except ValueError:pass
        remove_saved_entry_by_path_or_name(game_info)
        second_frame.update_idletasks();canvas.configure(scrollregion=canvas.bbox("all"))
    def show_dots(game_info):
        container=game_info['container']
        if 'dots' not in game_info or game_info['dots'] is None:
            dots_btn=Button(container,text="|",font=("Arial",12,"bold"),bg="Grey",fg="black",bd=0,relief="flat",cursor="hand2",highlightthickness=0,padx=3,pady=4,command=lambda gi=game_info:open_dots_menu(gi))
            dots_btn.bind("<Enter>",lambda e:dots_btn.config(bg="Grey"));dots_btn.bind("<Leave>",lambda e:dots_btn.config(bg="Grey"))
            game_info['dots']=dots_btn
        else:dots_btn=game_info['dots']
        dots_btn.place(relx=1.0,x=-6,y=6,anchor=NE);dots_btn.lift()
    def hide_dots_if_outside(event,game_info):
        container=game_info['container'];dots_btn=game_info.get('dots');widget_under_pointer=window.winfo_containing(event.x_root,event.y_root)
        if widget_under_pointer is None:
            if dots_btn:dots_btn.place_forget()
            return
        if (widget_under_pointer is container) or (dots_btn is not None and (widget_under_pointer is dots_btn or widget_under_pointer.master is dots_btn)):return
        parent=widget_under_pointer
        while parent:
            if parent is container:return
            parent=parent.master
        if dots_btn:dots_btn.place_forget()
    def open_dots_menu(game_info):
        dots_btn=game_info.get('dots')
        if dots_btn is None:return
        menu=Menu(window,tearoff=0);menu.add_command(label="Add Image",command=lambda gi=game_info:add_image_to_button(gi));menu.add_command(label="Delete",command=lambda gi=game_info:delete_game(gi))
        x=dots_btn.winfo_rootx();y=dots_btn.winfo_rooty()+dots_btn.winfo_height()
        try:menu.tk_popup(x,y)
        finally:menu.grab_release()
    def pil_load_and_fit_image(path,target_w=TILE_WIDTH,target_h=TILE_HEIGHT,bg_color=(243,208,208,255)):
        if not HAVE_PIL:raise ImportError("Pillow is required for proper image resizing. Install with: pip install pillow")
        img=Image.open(path).convert("RGBA");img.thumbnail((target_w,target_h),Image.LANCZOS)
        background=Image.new("RGBA",(target_w,target_h),bg_color);paste_x=(target_w-img.width)//2;paste_y=(target_h-img.height)//2;background.paste(img,(paste_x,paste_y),img);return ImageTk.PhotoImage(background)
    def add_image_to_button(game_info):
        file_path=filedialog.askopenfilename(title="Select PNG image",filetypes=[("PNG images","*.png"),("All files","*.*")])
        if not file_path:return
        if not HAVE_PIL:
            if not messagebox.askyesno("Pillow not found","Pillow (PIL) is not installed. Without Pillow the image won't be resized to fit the tile.\n\nInstall Pillow with: pip install pillow\n\nContinue and attempt to load anyway?"):return
        container=game_info['container'];button_widget=None
        for child in container.winfo_children():
            if isinstance(child,Button):button_widget=child;break
        if not button_widget:messagebox.showerror("Error","Could not find the button widget to set the image on.");return
        tk_img=None
        try:
            if HAVE_PIL:tk_img=pil_load_and_fit_image(file_path,TILE_WIDTH,TILE_HEIGHT)
            else:tk_img=PhotoImage(file=file_path)
        except Exception as e:messagebox.showerror("Invalid Image",f"Could not load/resize image:\n{e}");return
        button_widget.config(image=tk_img,text="");game_info['tk_image']=tk_img;game_info['image_path']=file_path
        entry=find_saved_entry(game_info=game_info)
        new_entry={"name":game_info.get("display_name") or game_info.get("name"),"path":game_info.get("path"),"image":file_path,"is_static":bool(game_info.get("is_static",False)),"removed":False}
        if entry:entry.update({"image": file_path, "removed": False, "is_static": new_entry["is_static"]})
        else:update_or_add_saved_entry(new_entry)
    def create_game_button_widget(name,path):
        display_name=name;lower_name=display_name.lower();button_container=Frame(second_frame,width=TILE_WIDTH,height=TILE_HEIGHT,bg="#800000");button_container.pack_propagate(False);button_container.pack(pady=25)
        new_button=Button(button_container,text=display_name,bg="#F3D0D0",font=("Arial",30,"bold"),relief="flat",cursor="hand2",borderwidth=10,highlightthickness=10,command=lambda p=path:launch_game(p) if p else None);new_button.pack(fill=tkinter.BOTH,expand=True)
        game_info={'name':lower_name,'display_name':display_name,'container':button_container,'path':path,'dots':None,'tk_image':None,'image_path':None,'is_static':False}
        entry=find_saved_entry(name=display_name,path=path)
        if entry and entry.get("image"):
            try:
                if HAVE_PIL:img=pil_load_and_fit_image(entry["image"],TILE_WIDTH,TILE_HEIGHT)
                else:img=PhotoImage(file=entry["image"])
                new_button.config(image=img,text="");game_info['tk_image']=img;game_info['image_path']=entry["image"]
            except Exception:pass
        all_game_buttons.append(game_info)
        button_container.bind("<Enter>",lambda e,gi=game_info:show_dots(gi));button_container.bind("<Leave>",lambda e,gi=game_info:hide_dots_if_outside(e,gi))
        new_button.bind("<Enter>",lambda e,gi=game_info:show_dots(gi));new_button.bind("<Leave>",lambda e,gi=game_info:hide_dots_if_outside(e,gi))
        second_frame.update_idletasks();canvas.configure(scrollregion=canvas.bbox("all"))
    def add_game():
        file_path=filedialog.askopenfilename(title="Game Shortcut",filetypes=[("Executable or Shortcut","*.exe *.lnk *.bat"),("All files","*.*")])
        if not file_path:return
        game_name=os.path.splitext(os.path.basename(file_path))[0];create_game_button_widget(game_name,file_path);sort_game_buttons()
        new_entry={"name":game_name,"path":file_path,"image":None,"is_static":False,"removed":False};update_or_add_saved_entry(new_entry)
    def filter_games(event=None):
        search_term=search_entry.get().lower()
        if not search_term or search_term=="search for games...":
            for game_info in all_game_buttons:
                container=game_info['container']
                if container.master is top_frame:continue
                container.pack(pady=25)
        else:
            for game_info in all_game_buttons:
                container=game_info['container']
                if container.master is top_frame:continue
                name=game_info['name']
                if search_term in name:container.pack(pady=25)
                else:container.pack_forget()
        second_frame.update_idletasks();canvas.configure(scrollregion=canvas.bbox("all"))
    def on_search_focus_in(event):
        if search_entry.get()=="Search for games...":search_entry.delete('0','end')
    def on_window_click(event):
        widget=window.winfo_containing(event.x_root,event.y_root)
        if widget is not search_entry:reset_game_list();window.focus_set()
    window.bind("<Button-1>",on_window_click)
    search_entry=Entry(top_frame,font=("Arial",12),width=20);search_entry.place(relx=0.5,rely=0.5,anchor=CENTER);search_entry.insert(0,"Search for games...");search_entry.bind("<FocusIn>",on_search_focus_in);search_entry.bind("<KeyRelease>",filter_games)
    def create_static_image_button(image_photo,command_func,name):
        display_name=name;lower_name=display_name.lower();button_container=Frame(second_frame,width=TILE_WIDTH,height=TILE_HEIGHT,bg="#800000");button_container.pack_propagate(False);button_container.pack(pady=25)
        new_button=Button(button_container,image=image_photo,command=command_func,bg='#000000',activebackground='black',borderwidth=0,highlightthickness=0,cursor="hand2");new_button.pack(fill=tkinter.BOTH,expand=True)
        game_info={'name':lower_name,'display_name':display_name,'container':button_container,'path':None,'dots':None,'tk_image':None,'image_path':None,'is_static':True}
        entry=find_saved_entry(name=display_name)
        if entry and entry.get("removed"):button_container.destroy();return
        if entry and entry.get("image"):
            try:
                if HAVE_PIL:img=pil_load_and_fit_image(entry["image"],TILE_WIDTH,TILE_HEIGHT)
                else:img=PhotoImage(file=entry["image"])
                new_button.config(image=img);game_info['tk_image']=img;game_info['image_path']=entry["image"]
            except Exception:pass
        else:
            if image_photo and str(image_photo).startswith('pyimage'):game_info['tk_image']=image_photo
        all_game_buttons.append(game_info)
        button_container.bind("<Enter>",lambda e,gi=game_info:show_dots(gi));button_container.bind("<Leave>",lambda e,gi=game_info:hide_dots_if_outside(e,gi))
        new_button.bind("<Enter>",lambda e,gi=game_info:show_dots(gi));new_button.bind("<Leave>",lambda e,gi=game_info:hide_dots_if_outside(e,gi))
    button_adder=Button(top_frame,image=adder,bg='#800000',activebackground='#800000',width=50,height=50,borderwidth=0,highlightthickness=0,command=add_game,cursor="hand2");button_adder.place(x=50,rely=0.5,anchor=W)
    button_clear=Button(top_frame,bg='black',activebackground='black',width=6,height=2,command=reset_save,text="RESET",fg='#F3D0D0',font=("Arial",10,"bold"),cursor="hand2");button_clear.place(relx=0.92,rely=0.5,anchor=E)
    def is_removed_static(name):e=find_saved_entry(name=name);return bool(e and e.get("removed"))
    if not is_removed_static("2XKO"):create_static_image_button(TWOXKO,open_2XKO,"2XKO")
    if not is_removed_static("Kairo Randomizer"):create_static_image_button(Randomizer,open_Randomizer,"Kairo Randomizer")
    if not is_removed_static("Marvel Rivals"):create_static_image_button(Rivals,open_rivals,"Marvel Rivals")
    if not is_removed_static("Skate"):create_static_image_button(Skate,open_skate,"Skate")
    if not is_removed_static("Valorant"):create_static_image_button(Valorant,open_VALORANT,"Valorant")
    for game in saved_games:
        if game.get("is_static") and game.get("removed"):continue
        if game.get("is_static"):
            for gi in all_game_buttons:
                if gi['name']==game.get("name","").lower():
                    if game.get("image") and not gi.get("tk_image"):
                        try:
                            if HAVE_PIL:img=pil_load_and_fit_image(game["image"],TILE_WIDTH,TILE_HEIGHT)
                            else:img=PhotoImage(file=game["image"])
                            for child in gi['container'].winfo_children():
                                if isinstance(child,Button):child.config(image=img,text="");gi['tk_image']=img;gi['image_path']=game["image"];break
                        except Exception:pass
                    break
            continue
        create_game_button_widget(game.get("name",""),game.get("path",None))
        if game.get("image"):
            for gi in reversed(all_game_buttons):
                if gi.get("path") and game.get("path") and os.path.normcase(gi.get("path"))==os.path.normcase(game.get("path")):
                    try:
                        if HAVE_PIL:img=pil_load_and_fit_image(game["image"],TILE_WIDTH,TILE_HEIGHT)
                        else:img=PhotoImage(file=game["image"])
                        for child in gi['container'].winfo_children():
                            if isinstance(child,Button):child.config(image=img,text="");gi['tk_image']=img;gi['image_path']=game["image"];break
                    except Exception:pass
                    break
        sort_game_buttons()
    window.mainloop()
if __name__=="__main__":main_program()
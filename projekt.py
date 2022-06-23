import pygame
import random

pygame.init()

panel=200
screen_width=800
screen_height=600

screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Lizard Wizard')


current_fighter=1
current_fighter2=1
current_fighter3=1
current_fighter4=1
cooldown=0
wait_time=450




font=pygame.font.SysFont('Times New Roman',30)
green = (100, 255, 100)
red=(255,0,0)

background_img=pygame.image.load('forest.jpg')
panel_img=pygame.image.load('panel.png')
attack_img=pygame.image.load('attack.jpg')
fire_img=pygame.image.load('fire.jpg')
heal_img=pygame.image.load('heal.jpg')
yes_img=pygame.image.load('yes.jpg')
no_img=pygame.image.load('no.jpg')
hp_potion_img=pygame.image.load('hp_potion.png')
mp_potion_img=pygame.image.load('mp_potion.png')
story_1=pygame.image.load('story1.png')
story_2=pygame.image.load('story2.png')
story_3=pygame.image.load('story3.png')
rules=pygame.image.load('rules.png')
slide_1=pygame.image.load('slide1.png')
slide_2=pygame.image.load('slide2.png')
slide_3=pygame.image.load('slide3.png')
title=pygame.image.load('title.png')
game_over=pygame.image.load('game_over.png')
win=pygame.image.load('win.png')

fire_sound=pygame.mixer.Sound("FireIgnite.wav")
hit_sound=pygame.mixer.Sound("hit.wav")
win_sound=pygame.mixer.Sound("win.wav")
loss_sound=pygame.mixer.Sound("loss.wav")
heal_sound=pygame.mixer.Sound("heal.wav")
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

def draw_text(text,font,text_color,x,y):
    img=font.render(text,True,text_color)
    screen.blit(img,(x,y))
    
def draw_background():
    screen.blit(background_img,(0,0))
    

def draw_panel():
    screen.blit(panel_img,(0,400))
    draw_text(f'Flint HP:{lizard.hp} MP:{lizard.mp}', font, green, 50,425)
    draw_text(f'{lizard.hp_potions}', font, green, 155,535)
    draw_text(f'{lizard.mp_potions}', font, green, 300,535)
   
def draw_story1():
    screen.blit(title,(0,0))    

def draw_story2():
    screen.blit(story_1,(0,0))

def draw_story3():
    screen.blit(story_2,(0,0))

def draw_story4():
    screen.blit(story_3,(0,0))

def draw_rules():
    screen.blit(rules,(0,0))

def draw_slide1():
    screen.blit(slide_1,(0,0))

def draw_slide2():
    screen.blit(slide_2,(0,0))

def draw_slide3():
    screen.blit(slide_3,(0,0))


def draw_game_over():
    screen.blit(game_over,(0,0))

def draw_win():
    screen.blit(win,(0,0))


    

class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    

class fighter():
    def __init__(self,name,x,y,scale,max_hp,max_mp,start_hp_potions,start_mp_potions):
        self.start_hp_potions=start_hp_potions
        self.start_mp_potions=start_mp_potions
        self.hp_potions=start_hp_potions
        self.mp_potions=start_mp_potions
        self.scale=scale
        self.name=name
        self.max_hp=max_hp
        self.hp=max_hp
        self.max_mp=max_mp
        self.mp=max_mp
        self.alive=True
        self.animation_list=[]
        self.frame_index=0
        self.action=0 
        self.update_time=pygame.time.get_ticks()
        temp_list=[]
        
        for i in range(1,5):
            img=pygame.image.load(f'{self.name}/idle/{i}.png')
            img=pygame.transform.scale(img,(img.get_width()*self.scale,img.get_height()*self.scale))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list=[]
        for i in range(1,5):
            img=pygame.image.load(f'{self.name}/attack/{i}.png')
            img=pygame.transform.scale(img,(img.get_width()*self.scale,img.get_height()*self.scale))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list=[]
        for i in range(1,5):
            img=pygame.image.load(f'{self.name}/fire/{i}.png')
            img=pygame.transform.scale(img,(img.get_width()*self.scale,img.get_height()*self.scale))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list=[]
        for i in range(1,5):
            img=pygame.image.load(f'{self.name}/heal/{i}.png')
            img=pygame.transform.scale(img,(img.get_width()*self.scale,img.get_height()*self.scale))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list=[]
        for i in range(1,5):
            img=pygame.image.load(f'{self.name}/hit/{i}.png')
            img=pygame.transform.scale(img,(img.get_width()*self.scale,img.get_height()*self.scale))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image=self.animation_list[self.action][self.frame_index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    def idle(self):
        self.action=0
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()

    def attack(self, target):
        fighter_number=1
        if self.name=='lizard':
            damage=random.randint(10,20)
        if self.name=='wolf':
            damage=random.randint(5,20)
        if self.name=='Magic Tree':
            damage=random.randint(15,30)
        if self.name=='Cursed Wolf':
            damage=random.randint(15,30)
        if self.name=='Evil Mage':
            damage=random.randint(20,40)
            
        target.hp-=damage
        self.action=1
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        target.action=4
        target.frame_index=0
        target.update_time=pygame.time.get_ticks()
        pygame.mixer.Sound.play(hit_sound)
    
        
        if target.hp<1:
            target.hp=0
            target.alive=False
            if target.name=='wolf':
                self.hp_potions+=1
             
            if target.name=='Magic Tree':
                self.mp_potions+=1
             
            if target.name=='Cursed Wolf':
                self.hp_potions+=1
                self.mp_potions+=1
               

    def heal(self):
        pygame.mixer.Sound.play(heal_sound)
        self.mp-=2
        self.hp+=50
        self.action=3
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        if self.hp>self.max_hp:
                self.hp=self.max_hp

    def use_hp(self):
        pygame.mixer.Sound.play(heal_sound)
        self.hp_potions-=1
        self.hp+=100
        self.action=3
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        if self.hp>self.max_hp:
            self.hp=self.max_hp

    def use_mp(self):
        pygame.mixer.Sound.play(heal_sound)
        self.mp_potions-=1
        self.mp+=10
        self.action=3
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        if self.mp>self.max_mp:
            self.mp=self.max_mp      
                
    def fire(self, target):
        damage=30
        target.hp-=damage
        self.mp-=2
        self.action=2
        self.frame_index=0
        self.update_time=pygame.time.get_ticks()
        target.action=2
        target.frame_index=0
        target.update_time=pygame.time.get_ticks()
        pygame.mixer.Sound.play(fire_sound)
        
        if target.hp<1:
            target.hp=0
            target.alive=False
            if target.name=='wolf':
                self.hp_potions+=1
                
            if target.name=='Magic Tree':
                self.mp_potions+=1
                
            if target.name=='Cursed Wolf':
                self.hp_potions+=1
                self.mp_potions+=1
               
            
            
            
    def update(self):
        animation_cooldown=175
        self.image=self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks()-self.update_time>animation_cooldown:
            self.update_time=pygame.time.get_ticks()
            self.frame_index+=1
        if self.frame_index>=len(self.animation_list[self.action]):
            self.idle()

    def reset(self):
        self.alive=True
        self.mp=self.max_mp
        self.hp=self.max_hp
        self.frame_index=0
        self.action=0
        self.hp_potions=self.start_hp_potions
        self.mp_potions=self.start_mp_potions
        self.update_time=pygame.time.get_ticks()
        
    
    def draw(self):
        screen.blit(self.image,self.rect)


    

    def draw(self):
        screen.blit(self.image,self.rect)

lizard=fighter('lizard',175,270,5,200,10,1,1)
wolf=fighter('wolf',600,240,6,60,0,0,0)
tree=fighter('Magic Tree',600,240,6,100,0,0,0)
cursed=fighter('Cursed Wolf',600,240,6,100,0,0,0)
mage=fighter('Evil Mage',600,240,6,200,0,0,0)
attack_button=Button(50,460,attack_img)
fire_button=Button(50,500,fire_img)
heal_button=Button(200,500,heal_img)
hp_potion_button=Button(55,540,hp_potion_img)
mp_potion_button=Button(205,540,mp_potion_img)
yes_button=Button(270,400,yes_img)
no_button=Button(420,400,no_img)
fighter_number=1
run=True
story=0
time=0
while run:
    if story<6500:
        if story<=500:
            draw_story1()
            story+=1
        if story<=4000 and story>500:
            draw_story2()
            story+=1
        if story<=4500 and story>4000:
            draw_story3() 
            story+=1
        if story>4500 and story<=5000:
            draw_story4()
            story+=1
        if story>5000 and story<=6500:
            draw_rules()
            story+=1
    else:
        
        
        
        if lizard.alive==True:
            
            
            if fighter_number==1:
                draw_background()
                draw_panel()
                attack_button.draw()    
                fire_button.draw()
                heal_button.draw()
                hp_potion_button.draw()
                mp_potion_button.draw()
                lizard.update()
                lizard.draw()
                wolf.update()
                wolf.draw()
                draw_text(f'Wolf HP:{wolf.hp}', font, red, 550,425)
                if current_fighter%2==1:
                    position=pygame.mouse.get_pos()
                    if attack_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and attack_button.clicked==False:
                            attack_button.clicked=True
                            lizard.attack(wolf)
                            current_fighter+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            attack_button.clicked=False
                    elif fire_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and fire_button.clicked==False and lizard.mp>1:
                            fire_button.clicked=True
                            lizard.fire(wolf)
                            current_fighter+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            fire_button.clicked=False
                    elif heal_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and heal_button.clicked==False and lizard.mp>1 and lizard.hp<lizard.max_hp:
                            heal_button.clicked=True
                            lizard.heal()
                            current_fighter+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            heal_button.clicked=False
                    elif hp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and hp_potion_button.clicked==False and lizard.hp_potions>0 and lizard.hp<lizard.max_hp:
                            hp_potion_button.clicked=True
                            lizard.use_hp()
                            current_fighter+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            hp_potion_button.clicked=False
                    elif mp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and mp_potion_button.clicked==False and lizard.mp_potions>0 and lizard.mp<lizard.max_mp:
                            mp_potion_button.clicked=True
                            lizard.use_mp()
                            current_fighter+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            mp_potion_button.clicked=False
                        
                if current_fighter%2==0 and wolf.alive==True:
                    cooldown+=1
                    if cooldown>=wait_time:
                        wolf.attack(lizard)
                        current_fighter+=1
                        cooldown=0
                if wolf.alive==False and fighter_number==1:
                    if time<1000:
                        if time<=300:
                            time+=1
                        if time>300 and time<=1000:
                            
                            draw_slide1()
                            time+=1
                    else:
                        fighter_number=2
                        time=0
                    
                    
            
            if fighter_number==2:
                draw_background()
                draw_panel()
                attack_button.draw()
                fire_button.draw()
                heal_button.draw()
                hp_potion_button.draw()
                mp_potion_button.draw()
                lizard.update()
                lizard.draw()
                tree.update()
                tree.draw()
                draw_text(f'Magic Tree HP:{tree.hp}', font, red, 500,425)
                
                if current_fighter2%2==1:
                    position=pygame.mouse.get_pos()
                    if attack_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and attack_button.clicked==False:
                            attack_button.clicked=True
                            lizard.attack(tree)
                            current_fighter2+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            attack_button.clicked=False
                    elif fire_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and fire_button.clicked==False and lizard.mp>1:
                            fire_button.clicked=True
                            lizard.fire(tree)
                            current_fighter2+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            fire_button.clicked=False
                    elif heal_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and heal_button.clicked==False and lizard.mp>1 and lizard.hp<lizard.max_hp:
                            heal_button.clicked=True
                            lizard.heal()
                            current_fighter2+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            heal_button.clicked=False
                    elif hp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and hp_potion_button.clicked==False and lizard.hp_potions>0 and lizard.hp<lizard.max_hp:
                            hp_potion_button.clicked=True
                            lizard.use_hp()
                            current_fighter2+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            hp_potion_button.clicked=False
                    elif mp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and mp_potion_button.clicked==False and lizard.mp_potions>0 and lizard.mp<lizard.max_mp:
                            mp_potion_button.clicked=True
                            lizard.use_mp()
                            current_fighter2+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            mp_potion_button.clicked=False
                            
                if current_fighter2%2==0 and tree.alive==True:
                    cooldown+=1
                    if cooldown>=wait_time:
                        tree.attack(lizard)
                        current_fighter2+=1
                        cooldown=0
                if tree.alive==False and fighter_number==2:
                    if time<900:
                        if time<=200:
                            time+=1
                        if time>200 and time<=900:
                            draw_slide2()
                            time+=1
                    else:
                        fighter_number=3
                        time=0

            if fighter_number==3:
                draw_background()
                draw_panel()
                attack_button.draw()
                fire_button.draw()
                heal_button.draw()
                hp_potion_button.draw()
                mp_potion_button.draw()
                lizard.update()
                lizard.draw()
                cursed.update()
                cursed.draw()
                draw_text(f'Cursed Wolf HP:{cursed.hp}', font, red, 500,425)
                                
                if current_fighter3%2==1:
                    position=pygame.mouse.get_pos()
                    if attack_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and attack_button.clicked==False:
                            attack_button.clicked=True
                            lizard.attack(cursed)
                            current_fighter3+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            attack_button.clicked=False
                    elif fire_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and fire_button.clicked==False and lizard.mp>1:
                            fire_button.clicked=True
                            lizard.fire(cursed)
                            current_fighter3+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            fire_button.clicked=False
                    elif heal_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and heal_button.clicked==False and lizard.mp>1 and lizard.hp<lizard.max_hp:
                            heal_button.clicked=True
                            lizard.heal()
                            current_fighter3+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            heal_button.clicked=False
                    elif hp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and hp_potion_button.clicked==False and lizard.hp_potions>0 and lizard.hp<lizard.max_hp:
                            hp_potion_button.clicked=True
                            lizard.use_hp()
                            current_fighter3+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            hp_potion_button.clicked=False
                    elif mp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and mp_potion_button.clicked==False and lizard.mp_potions>0 and lizard.mp<lizard.max_mp:
                            mp_potion_button.clicked=True
                            lizard.use_mp()
                            current_fighter3+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            mp_potion_button.clicked=False
                                            
                if current_fighter3%2==0 and cursed.alive==True:
                    cooldown+=1
                    if cooldown>=wait_time:
                        cursed.attack(lizard)
                        current_fighter3+=1
                        cooldown=0
                if cursed.alive==False and fighter_number==3:
                    if time<900:
                        if time<=200:
                            time+=1
                        if time>200 and time<=900:
                            draw_slide3()
                            time+=1
                    else:
                        fighter_number=4
                        time=0

            if fighter_number==4:
                draw_background()
                draw_panel()
                attack_button.draw()
                fire_button.draw()
                heal_button.draw()
                hp_potion_button.draw()
                mp_potion_button.draw()
                lizard.update()
                lizard.draw()
                mage.update()
                mage.draw()
                draw_text(f'Evil Mage HP:{mage.hp}', font, red, 500,425)
                                
                if current_fighter4%2==1:
                    position=pygame.mouse.get_pos()
                    if attack_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and attack_button.clicked==False:
                            attack_button.clicked=True
                            lizard.attack(mage)
                            current_fighter4+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            attack_button.clicked=False
                    elif fire_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and fire_button.clicked==False and lizard.mp>1:
                            fire_button.clicked=True
                            lizard.fire(mage)
                            current_fighter4+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            fire_button.clicked=False
                    elif heal_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and heal_button.clicked==False and lizard.mp>1 and lizard.hp<lizard.max_hp:
                            heal_button.clicked=True
                            lizard.heal()
                            current_fighter4+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            heal_button.clicked=False
                    elif hp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and hp_potion_button.clicked==False and lizard.hp_potions>0 and lizard.hp<lizard.max_hp:
                            hp_potion_button.clicked=True
                            lizard.use_hp()
                            current_fighter4+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            hp_potion_button.clicked=False
                    elif mp_potion_button.rect.collidepoint(position):
                        if pygame.mouse.get_pressed()[0]==1 and mp_potion_button.clicked==False and lizard.mp_potions>0 and lizard.mp<lizard.max_mp:
                            mp_potion_button.clicked=True
                            lizard.use_mp()
                            current_fighter4+=1
                        if pygame.mouse.get_pressed()[0]==0:
                            mp_potion_button.clicked=False
                                            
                if current_fighter4%2==0 and mage.alive==True:
                    cooldown+=1
                    if cooldown>=wait_time:
                        mage.attack(lizard)
                        current_fighter4+=1
                        cooldown=0
                if mage.alive==False:
                    if time<200:
                        pygame.mixer.Sound.play(win_sound)
                        time+=1
                    else:
                        pygame.mixer.music.stop()
                        draw_win()
                        yes_button.draw()
                        no_button.draw()
                        position=pygame.mouse.get_pos()
                        if yes_button.rect.collidepoint(position):
                            if pygame.mouse.get_pressed()[0]==1 and yes_button.clicked==False:
                                yes_button.clicked=True
                                lizard.reset()
                                wolf.reset()
                                tree.reset()
                                cursed.reset()
                                mage.reset()
                                current_fighter=1
                                current_fighter2=1
                                current_fighter3=1
                                current_fighter4=1
                                cooldown=0
                                fighter_number=1
                                time=0
                                pygame.mixer.music.play(-1)
                            if pygame.mouse.get_pressed()[0]==0:
                                yes_button.clicked=False
                        elif no_button.rect.collidepoint(position):
                            if pygame.mouse.get_pressed()[0]==1 and no_button.clicked==False:
                                run=False
                      
                        
                            
        if lizard.alive==False:
            if time<400:
                pygame.mixer.Sound.play(loss_sound)
                time+=1
            else:
                pygame.mixer.music.stop()
                draw_game_over()
                yes_button.draw()
                no_button.draw()
                if fighter_number==4:
                    pygame.mixer.Sound.play(loss_sound)
                position=pygame.mouse.get_pos()
                if yes_button.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and yes_button.clicked==False:
                        yes_button.clicked=True
                        lizard.reset()
                        wolf.reset()
                        tree.reset()
                        cursed.reset()
                        mage.reset()
                        current_fighter=1
                        current_fighter2=1
                        current_fighter3=1
                        current_fighter4=1
                        cooldown=0
                        fighter_number=1
                        time=0
                        pygame.mixer.music.play(-1)
                    if pygame.mouse.get_pressed()[0]==0:
                        yes_button.clicked=False
                elif no_button.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and no_button.clicked==False:
                        run=False
                
            
       
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()


# coding: utf-8

# In[1]:


import pygame


# In[2]:


from pygame.locals import *


# In[3]:


pygame.init()
width, height = 800, 480
keys = [False, False, False, False]
playerpos=[100,100]
screen=pygame.display.set_mode((width, height))


# In[4]:


player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")


# In[5]:


while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    screen.blit(player, playerpos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_o:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5


# In[7]:


clock = pygame.time.Clock()


# In[10]:


crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
    clock.tick(60)
    pygame.quit()
quit()


# In[1]:


s='abcdd'


# In[5]:


s.split()


# In[14]:


print(s[i] for i in (0,len(s)))


# In[28]:


for i in range(0,3):
    print(i)


# In[16]:


dict1=dict()


# In[18]:


dict1.keys()


# In[20]:


dict1['a']=1


# In[24]:


for k,v in dict1.items():
    print((k,v))


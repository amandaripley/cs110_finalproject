import random
import tkinter as tk
import pygame

class remote(object):
    def __init__(self,laptop):
        self.laptop = laptop
    def click(self):
        self.laptop.on()
    def close(self):
        self.laptop.title1.destroy()
        self.laptop.title2.destroy()
        self.laptop.button.destroy()
        self.laptop.entry.destroy()

class laptop(tk.Tk):
    def __init__(self, key):
        
        self.game = dict()
        self.game['scar'] = {'display':'s _ _ r', 'definition':'a mark \
left on the skin or within body tissue where a wound, burn, or sore has \
not healed completely and fibrous connective tissue has developed.'}
        self.key = key
        self.puzzle_finish = False
        tk.Tk.__init__(self)
        '''
	self.game['escape'] = {'display':'_ s _ _ _ e', 'definition':'break \
	free from confinement or control'}

	self.game['convenience'] = {'display':'c _ n _ _ _ _ e _ _ _', \
	'definition':'the state of being able to proceed with \
	omething with little effort or difficulty'}
	'''

    
    def on(self):
        self.entry = tk.Entry(self)
        self.title1 = tk.Label(text = self.game['scar']['definition'])
        self.title2 = tk.Label(text = self.game['scar']['display'])
        self.button = tk.Button(self, text="I want to answer!", command=self.answer)
        self.title1.pack()
        self.title2.pack()
        self.entry.pack()
        self.button.pack()

    def answer(self):
        result = self.entry.get()
        if (result != 'scar'):
            print('Wrong answer')
        else:
            print('Image got')
            self.image.image_got()
            self.title1.destroy()
            self.title2.destroy()
            self.entry.destroy()
            self.button.destroy()
        return 'You solved it'

class image(object):
    def __init__(self)：
        self.complete = False
        self.sum = 0

    def image_got(self):
        self.sum += 1

    def finish(self):
        return self.sum >= 3

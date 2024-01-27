import random
import time

class Baby:
    def __init__(self, name, age, ascii):
        self.name = name
        self.age = age
        self.ascii = ascii
        self.cry = True

    def cry(self):
        self.cry = True
        print(f'{self.name} is crying')


babies_ascii = [
   r"""
   ,,,    
 _/. .\_  
(.\_o_/.) 
(.`,.`'.')
 ('.`,'`,)
  ('.`,'`)
   `--'"` """,
   r"""
   _,_    
 _/- -\_  
(.\_-_/.) 
(.`,.'.'.)
 ('.`,'',)
  ('.','`)
   `--'"` """,
   r"""
   >*<
 _/. .\_
(.\_c_/.)
(.,'.,'',)
 (',.'`.,)
  (.'.'.')
   `--'"'""",
   r"""
   _?_    
 _/a a\_  
(.\_~_/') 
(.'.,'.`.)
 ('.,'.`.)
  ('.','')
   `--'"' """,
   r"""
   _(_    
 _/' '\_  
(.\_^_/.) 
('.,'.`'.)
 ('.,'.',)
  ('.`.,')
   `--'"' """,
   r"""
   _@_    
 _/, ,\_  
(,\_e_/') 
(.`'.,'.')
 ('.','.`)
  (.'.,'.)
   `--'"` """
]


babies = {str(i+1): Baby(f"baby-{i+1}", random.randrange(0, 12), babies_ascii[i]) for i in range(0, len(babies_ascii))}


welcome_screen = r"""
  .-\"\"\"-.
 /      o\
|    o   0).-.
|       .-;(_/     .-.
 \     /  /)).---._|  `\   ,
  '.  '  /((       `'-./ _/|
    \  .'  )        .-.;`  /
     '.             |  `\-'
       '._        -'    /
          ``""--`------`

          cry-baby v0.1
    """

if __name__ == '__main__':
    print(welcome_screen)

    for baby in babies:
        print(babies[baby].ascii)
        print(f'{babies[baby].name}\n')

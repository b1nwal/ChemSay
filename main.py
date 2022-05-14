import re
from tkinter import *
import os
e = []
class pt:
  hydrogen = {'name': 'Hydrogen', 'symbol': 'H', 'mass': '1.00794', 'number': 1}
  helium = {'name': 'Helium', 'symbol': 'He', 'mass': '4.002602', 'number': 2}
  lithium = {'name': 'Lithium', 'symbol': 'Li', 'mass': '6.941', 'number': 3}
  beryllium = {'name': 'Beryllium', 'symbol': 'Be', 'mass': '9.012182', 'number': 4}
  boron =  {'name': 'Boron', 'symbol': 'B', 'mass': '10.811', 'number': 5}
  carbon = {'name': 'Carbon', 'symbol': 'C', 'mass': '12.0107', 'number': 6}
  nitrogen = {'name': 'Nitrogen', 'symbol': 'N', 'mass': '14.0067', 'number': 7}
  oxygen = {'name': 'Oxygen', 'symbol': 'O', 'mass': '15.9994', 'number': 8}
  fluorine = {'name': 'Fluorine', 'symbol': 'F', 'mass': '18.9984032', 'number': 9}
  neon = {'name': 'Neon', 'symbol': 'Ne', 'mass': '20.1797', 'number': 10}
  sodium = {'name': 'Sodium', 'symbol': 'Na', 'mass': '22.98976928', 'number': 11}
  magnesium = {'name': 'Magnesium', 'symbol': 'Mg', 'mass': '24.3050', 'number': 12}
  aluminum = {'name': 'Aluminum', 'symbol': 'Al', 'mass': '26.9815386', 'number': 13}
  silicon = {'name': 'Silicon', 'symbol': 'Si', 'mass': '28.0855', 'number': 14}
  phosphorus = {'name': 'Phosphorus', 'symbol': 'P', 'mass': '30.973762', 'number': 15}
  sulfur = {'name': 'Sulfur', 'symbol': 'S', 'mass': '32.065', 'number': 16}
  chlorine = {'name': 'Chlorine', 'symbol': 'Cl', 'mass': '35.453', 'number': 17}
  argon = {'name': 'Argon', 'symbol': 'Ar', 'mass': '39.948', 'number': 18}
  potassium = {'name': 'Potassium', 'symbol': 'K', 'mass': '39.0983', 'number': 19}
  calcium = {'name': 'Calcium', 'symbol': 'Ca', 'mass': '40.078', 'number': 20}
  scandium = {'name': 'Scandium', 'symbol': 'Sc', 'mass': '44.955912', 'number': 21}
  titanium = {'name': 'Titanium', 'symbol': 'Ti', 'mass': '47.867', 'number': 22}
  vanadium = {'name': 'Vanadium', 'symbol': 'V', 'mass': '50.9415', 'number': 23}
  chromium = {'name': 'Chromium', 'symbol': 'Cr', 'mass': '51.9961', 'number': 24}
  manganese = {'name': 'Manganese', 'symbol': 'Mn', 'mass': '54.938045', 'number': 25}
  iron = {'name': 'Iron', 'symbol': 'Fe', 'mass': '55.845', 'number': 26}
  cobalt = {'name': 'Cobalt', 'symbol': 'Co', 'mass': '58.933195', 'number': 27}
  nickel = {'name': 'Nickel', 'symbol': 'Ni', 'mass': '58.6934', 'number': 28}
  copper = {'name': 'Copper', 'symbol': 'Cu', 'mass': '63.546', 'number': 29}
  zinc = {'name': 'Zinc', 'symbol': 'Zn', 'mass': '65.38', 'number': 30}
  gallium = {'name': 'Gallium', 'symbol': 'Ga', 'mass': '69.723', 'number': 31}
  germanium = {'name': 'Germanium', 'symbol': 'Ge', 'mass': '72.64', 'number': 32}
  arsenic = {'name': 'Arsenic', 'symbol': 'As', 'mass': '74.92160', 'number': 33}
  selenium = {'name': 'Selenium', 'symbol': 'Se', 'mass': '78.96', 'number': 34}
  bromine = {'name': 'Bromine', 'symbol': 'Br', 'mass': '79.904', 'number': 35}
  krypton = {'name': 'Krypton', 'symbol': 'Kr', 'mass': '83.798', 'number': 36}
  rubidium = {'name': 'Rubidium', 'symbol': 'Rb', 'mass': '85.4678', 'number': 37}
  strontium = {'name': 'Strontium', 'symbol': 'Sr', 'mass': '87.62', 'number': 38}
  yttrium = {'name': 'Yttrium', 'symbol': 'Y', 'mass': '88.90585', 'number': 39}
  zirconium = {'name': 'Zirconium', 'symbol': 'Zr', 'mass': '91.224', 'number': 40}
  niobium = {'name': 'Niobium', 'symbol': 'Nb', 'mass': '92.90638', 'number': 41}
  molybdenum = {'name': 'Molybdenum', 'symbol': 'Mo', 'mass': '95.96', 'number': 42}
  technetium = {'name': 'Technetium', 'symbol': 'Tc', 'mass': '98', 'number': 43}
  ruthenium = {'name': 'Ruthenium', 'symbol': 'Ru', 'mass': '101.07', 'number': 44}
  rhodium = {'name': 'Rhodium', 'symbol': 'Rh', 'mass': '102.90550', 'number': 45}
  palladium = {'name': 'Palladium', 'symbol': 'Pd', 'mass': '106.42', 'number': 46}
  silver = {'name': 'Silver', 'symbol': 'Ag', 'mass': '107.8682', 'number': 47}
  cadmium = {'name': 'Cadmium', 'symbol': 'Cd', 'mass': '112.411', 'number': 48}
  indium = {'name': 'Indium', 'symbol': 'In', 'mass': '114.818', 'number': 49}
  tin = {'name': 'Tin', 'symbol': 'Sn', 'mass': '118.710', 'number': 50}
  antimony = {'name': 'Antimony', 'symbol': 'Sb', 'mass': '121.760', 'number': 51}
  tellurium = {'name': 'Tellurium', 'symbol': 'Te', 'mass': '127.60', 'number': 52}
  iodine = {'name': 'Iodine', 'symbol': 'I', 'mass': '126.90447', 'number': 53}
  xenon = {'name': 'Xenon', 'symbol': 'Xe', 'mass': '131.293', 'number': 54}
  cesium = {'name': 'Cesium', 'symbol': 'Cs', 'mass': '132.9054519', 'number': 55}
  barium = {'name': 'Barium', 'symbol': 'Ba', 'mass': '137.327', 'number': 56}
  lanthanum = {'name': 'Lanthanum', 'symbol': 'La', 'mass': '138.90547', 'number': 57}
  cerium = {'name': 'Cerium', 'symbol': 'Ce', 'mass': '140.116', 'number': 58}
  praseodymium = {'name': 'Praseodymium', 'symbol': 'Pr', 'mass': '140.90765', 'number': 59}
  neodymium = {'name': 'Neodymium', 'symbol': 'Nd', 'mass': '144.242', 'number': 60}
  promethium = {'name': 'Promethium', 'symbol': 'Pm', 'mass': '145', 'number': 61}
  samarium = {'name': 'Samarium', 'symbol': 'Sm', 'mass': '150.36', 'number': 62}
  europium = {'name': 'Europium', 'symbol': 'Eu', 'mass': '151.964', 'number': 63}
  gadolinium = {'name': 'Gadolinium', 'symbol': 'Gd', 'mass': '157.25', 'number': 64}
  terbium = {'name': 'Terbium', 'symbol': 'Tb', 'mass': '158.92535', 'number': 65}
  dysprosium = {'name': 'Dysprosium', 'symbol': 'Dy', 'mass': '162.500', 'number': 66}
  holmium = {'name': 'Holmium', 'symbol': 'Ho', 'mass': '164.93032', 'number': 67}
  erbium = {'name': 'Erbium', 'symbol': 'Er', 'mass': '167.259', 'number': 68}
  thulium = {'name': 'Thulium', 'symbol': 'Tm', 'mass': '168.93421', 'number': 69}
  ytterbium = {'name': 'Ytterbium', 'symbol': 'Yb', 'mass': '173.054', 'number': 70}
  lutetium = {'name': 'Lutetium', 'symbol': 'Lu', 'mass': '174.9668', 'number': 71}
  hafnium = {'name': 'Hafnium', 'symbol': 'Hf', 'mass': '178.49', 'number': 72}
  tantalum = {'name': 'Tantalum', 'symbol': 'Ta', 'mass': '180.94788', 'number': 73}
  tungsten = {'name': 'Tungsten', 'symbol': 'W', 'mass': '183.84', 'number': 74}
  rhenium = {'name': 'Rhenium', 'symbol': 'Re', 'mass': '186.207', 'number': 75}
  osmium = {'name': 'Osmium', 'symbol': 'Os', 'mass': '190.23', 'number': 76}
  iridium = {'name': 'Iridium', 'symbol': 'Ir', 'mass': '192.217', 'number': 77}
  platinum = {'name': 'Platinum', 'symbol': 'Pt', 'mass': '195.084', 'number': 78}
  gold = {'name': 'Gold', 'symbol': 'Au', 'mass': '196.966569', 'number': 79}
  mercury = {'name': 'Mercury', 'symbol': 'Hg', 'mass': '200.59', 'number': 80}
  thallium = {'name': 'Thallium', 'symbol': 'Tl', 'mass': '204.3833', 'number': 81}
  lead = {'name': 'Lead', 'symbol': 'Pb', 'mass': '207.2', 'number': 82}
  bismuth = {'name': 'Bismuth', 'symbol': 'Bi', 'mass': '208.98040', 'number': 83}
  polonium = {'name': 'Polonium', 'symbol': 'Po', 'mass': '209', 'number': 84}
  astatine = {'name': 'Astatine', 'symbol': 'At', 'mass': '210', 'number': 85}
  radon = {'name': 'Radon', 'symbol': 'Rn', 'mass': '222', 'number': 86}
  francium = {'name': 'Francium', 'symbol': 'Fr', 'mass': '223', 'number': 87}
  radium = {'name': 'Radium', 'symbol': 'Ra', 'mass': '226', 'number': 88}
  actinium = {'name': 'Actinium', 'symbol': 'Ac', 'mass': '227', 'number': 89}
  thorium = {'name': 'Thorium', 'symbol': 'Th', 'mass': '232.03806', 'number': 90}
  protactinium = {'name': 'Protactinium', 'symbol': 'Pa', 'mass': '231.03588', 'number': 91}
  uranium = {'name': 'Uranium', 'symbol': 'U', 'mass': '238.02891', 'number': 92}
  neptunium = {'name': 'Neptunium', 'symbol': 'Np', 'mass': '237', 'number': 93}
  plutonium = {'name': 'Plutonium', 'symbol': 'Pu', 'mass': '244', 'number': 94}
  americium = {'name': 'Americium', 'symbol': 'Am', 'mass': '243', 'number': 95}
  curium = {'name': 'Curium', 'symbol': 'Cm', 'mass': '247', 'number': 96}
  berkelium = {'name': 'Berkelium', 'symbol': 'Bk', 'mass': '247', 'number': 97}
  californium = {'name': 'Californium', 'symbol': 'Cf', 'mass': '251', 'number': 98}
  einsteinium = {'name': 'Einsteinium', 'symbol': 'Es', 'mass': '252', 'number': 99}
  fermium = {'name': 'Fermium', 'symbol': 'Fm', 'mass': '257', 'number': 100}
  mendelevium = {'name': 'Mendelevium', 'symbol': 'Md', 'mass': '258', 'number': 101}
  nobelium = {'name': 'Nobelium', 'symbol': 'No', 'mass': '259', 'number': 102}
  lawrencium = {'name': 'Lawrencium', 'symbol': 'Lr', 'mass': '262', 'number': 103}
  rutherfordium = {'name': 'Rutherfordium', 'symbol': 'Rf', 'mass': '267', 'number': 104}
  dubnium = {'name': 'Dubnium', 'symbol': 'Db', 'mass': '268', 'number': 105}
  seaborgium = {'name': 'Seaborgium', 'symbol': 'Sg', 'mass': '271', 'number': 106}
  bohrium = {'name': 'Bohrium', 'symbol': 'Bh', 'mass': '272', 'number': 107}
  hassium = {'name': 'Hassium', 'symbol': 'Hs', 'mass': '270', 'number': 108}
  meitnerium = {'name': 'Meitnerium', 'symbol': 'Mt', 'mass': '276', 'number': 109}
  darmstadtium = {'name': 'Darmstadtium', 'symbol': 'Ds', 'mass': '281', 'number': 110}
  roentgenium = {'name': 'Roentgenium', 'symbol': 'Rg', 'mass': '280', 'number': 111}
  copernicium = {'name': 'Copernicium', 'symbol': 'Cn', 'mass': '285', 'number': 112}
  nihonium = {'name': 'Nihonium', 'symbol': 'Nh', 'mass': '284', 'number': 113}
  flerovium = {'name': 'Flerovium', 'symbol': 'Fl', 'mass': '289', 'number': 114}
  moscovium = {'name': 'Moscovium', 'symbol': 'Mc', 'mass': '288', 'number': 115}
  livermorium = {'name': 'Livermorium', 'symbol': 'Lv', 'mass': '293', 'number': 116}
  tennessine = {'name': 'Tennessine', 'symbol': 'Ts', 'mass': '294', 'number': 117}
  oganesson = {'name': 'Oganesson', 'symbol': 'Og', 'mass': '294', 'number': 118}
  sym = {'h': hydrogen, 'he': helium, 'li': lithium, 'be': beryllium, 'b': boron, 'c': carbon, 'n': nitrogen, 'o': oxygen, 'f': fluorine, 'ne': neon, 'na': sodium, 'mg': magnesium, 'al': aluminum, 'si': silicon, 'p': phosphorus, 's': sulfur, 'cl': chlorine, 'ar': argon, 'k': potassium, 'ca': calcium, 'sc': scandium, 'ti': titanium, 'v': vanadium, 'cr': chromium, 'mn': manganese, 'fe': iron, 'co': cobalt, 'ni': nickel, 'cu': copper, 'zn': zinc, 'ga': gallium, 'ge': germanium, 'as': arsenic, 'se': selenium, 'br': bromine, 'kr': krypton, 'rb': rubidium, 'sr': strontium, 'y': yttrium, 'zr': zirconium, 'nb': niobium, 'mo': molybdenum, 'tc': technetium, 'ru': ruthenium, 'rh': rhodium, 'pd': palladium, 'ag': silver, 'cd': cadmium, 'in': indium, 'sn': tin, 'sb': antimony, 'te': tellurium, 'i': iodine, 'xe': xenon, 'cs': cesium, 'ba': barium, 'la': lanthanum, 'ce': cerium, 'pr': praseodymium, 'nd': neodymium, 'pm': promethium, 'sm': samarium, 'eu': europium, 'gd': gadolinium, 'tb': terbium, 'dy': dysprosium, 'ho': holmium, 'er': erbium, 'tm': thulium, 'yb': ytterbium, 'lu': lutetium, 'hf': hafnium, 'ta': tantalum, 'w': tungsten, 're': rhenium, 'os': osmium, 'ir': iridium, 'pt': platinum, 'au': gold, 'hg': mercury, 'tl': thallium, 'pb': lead, 'bi': bismuth, 'po': polonium, 'at': astatine, 'rn': radon, 'fr': francium, 'ra': radium, 'ac': actinium, 'th': thorium, 'pa': protactinium, 'u': uranium, 'np': neptunium, 'pu': plutonium, 'am': americium, 'cm': curium, 'bk': berkelium, 'cf': californium, 'es': einsteinium, 'fm': fermium, 'md': mendelevium, 'no': nobelium, 'lr': lawrencium, 'rf': rutherfordium, 'db': dubnium, 'sg': seaborgium, 'bh': bohrium, 'hs': hassium, 'mt': meitnerium, 'ds': darmstadtium, 'rg': roentgenium, 'cn': copernicium, 'nh': nihonium, 'fl': flerovium, 'mc': moscovium, 'lv': livermorium, 'ts': tennessine, 'og': oganesson, 'a':'a','d':'d','e':'e','g':'g','j':'j','l':'l','m':'m','q':'q','r':'r','t':'t','x':'x','z':'z',' ':' '}
def chem_say(word):
    ss = []
    l = []
    fin = []
    d = {i:[] for i in range(len(word))}
    for i in pt.sym:
      g = [i.start() for i in re.finditer(i, word)]
      for x in g:
        d[x].append(i)
    for i in d[0]:
      l.append([i])
    for i in range(len(word)):
      n = []
      for i in l:
        c = sum(map(len,i))
        if c >= len(word):
          n.append(i)
          continue
        for x in d[c]:
          n.append(i + [x])
      l = n
    for i in l:
      s = 0
      for x in i:
        if type(pt.sym[x]) == type({}):
          s += 1
        else:
          s += 2
      ss.append(s)
    try:
        g = l[ss.index(min(ss))]
    except ValueError:
        xn = cv.create_rectangle(0,0,0,0,width=0)
        on = cv.create_rectangle(0,0,0,0,width=0)
        nu = cv.create_rectangle(0,0,0,0,width=0)
        sy = cv.create_text(540,200,fill="#CBF7ED",font="Times 40",text="No results.")
        na = cv.create_rectangle(0,0,0,0,width=0)
        ma = cv.create_rectangle(0,0,0,0,width=0)
        elem = element(xn,on,nu,sy,na,ma)
        e.append(elem)
        return []
    for i in g:
      fin.append(pt.sym[i])
    return fin
win = Tk()
win.geometry('1080x720')
cv = Canvas(win,width=1080,height=720,bg="#161925",highlightthickness=0)
cv.pack()
cv.create_text(540,500,fill="#CBF7ED",font="Times 15",text="*All Masses Are Rounded")
logoimg = PhotoImage(file="assets/logo.gif")
cv.create_image(980,670,image=logoimg)
class element():
    def __init__(self,xn,on,nu,sy,na,ma):
        self.xn = xn
        self.on = on
        self.nu = nu
        self.sy = sy
        self.na = na
        self.ma = ma
def draw_element(x,y,e):
    if type(e) == type(''):
        xn = cv.create_rectangle(0,0,0,0,width=0)
        on = cv.create_rectangle(0,0,0,0,width=0)
        nu = cv.create_rectangle(0,0,0,0,width=0)
        sy = cv.create_text(x+50,y+50,fill="#CBF7ED",font="Times 40",text=e)
        na = cv.create_rectangle(0,0,0,0,width=0)
        ma = cv.create_rectangle(0,0,0,0,width=0)
        elem = element(xn,on,nu,sy,na,ma)
        return elem
    number  = e['number']
    symbol  = e['symbol']
    name    = e['name']
    mass    = float(e['mass'])
    xn = cv.create_rectangle(x+6, y+6, x+106, y+106,outline="#23395B",width=8)
    on = cv.create_rectangle(x, y, x+100, y+100,outline="#406E8E",width=8)
    nu = cv.create_text(x+20,y+20,fill="#CBF7ED",font="15",text=number)
    sy = cv.create_text(x+50,y+50,fill="#CBF7ED",font="Times 40",text=symbol)
    na = cv.create_text(x+50,y+80,fill="#CBF7ED",font="Times 10",text=name)
    ma = cv.create_text(x+80,y+20,fill="#CBF7ED",font="15",text=round(mass))
    elem = element(xn,on,nu,sy,na,ma)
    return elem
def get_input(f):
    for i in e:
        cv.delete(i.xn)
        cv.delete(i.on)
        cv.delete(i.nu)
        cv.delete(i.sy)
        cv.delete(i.na)
        cv.delete(i.ma)
    l = chem_say(wbox.get().lower())
    wbox.delete(0,END)
    tl = 0
    for i in l:
        if i == ' ':
            tl += 60
        else:
            tl += 100
    x,y=440 - tl/2,100
    for i in l:
        if i == ' ':
            x+=60
        else:
            x+=100
        e.append(draw_element(x,y,i))
wbox = Entry(win,bg="#23395B",bd=0,font="Consolas 40",fg="#8EA8C3",insertbackground="#8EA8C3")
cv.create_window(540,400,window=wbox,height=120,width=690)
cv.create_rectangle(190,335,890,465,outline="#23395B",width=10)
cv.create_rectangle(180,325,900,475,outline="#406E8E",width=10)
wbox.bind('<Return>',get_input)
win.title('ChemSay')
win.iconbitmap('assets/icon.ico')
win.mainloop()

#!/usr/bin/python
# -*- coding: utf-8 -*-
#Turkish
tr = {
    'midnight':'geceyarısı',
    'evening':'AKŞAM',
    'morning':'SABAH',
    'andromeda':'Andromeda Gökadası',
    'orion':'Avcı Bulutsusu',
    'sevensisters':'Yedi Kızkardeşler',
    'waning':'Küçülen Ay',
    'moonrise_times':'Ay\'ın doğuş zamanları',
    'waxing':'Büyüyen Ay',
    'moonset_times':'Ay\'ın batış zamanları',
    'newmoon':'Yeni ay',
    'firstquarter':'İlk dördün',
    'fullmoon':'Dolunay',
    'lastquarter':'Son dördün',
    'rising':'doğuyor',
    'mercury':'Merkür',
    'venus':'Venüs',
    'mars':'Mars',
    'jupiter':'Jüpiter',
    'saturn':'Satürn',
    'uranus':'Uranüs',
    'neptune':'Neptün',
    'antares':'Antares',
    'transit':'meridyende',
    'transit_abbrev':'mrd.',
    'arcturus':'Arcturus',
    'pollux':'Pollux',
    'deneb':'Deneb',
    'setting':'batıyor',
    'set_abbrev':'bt.',
}
#English
en = {
    'midnight':'midnight',
    'evening':'EVENING',
    'morning':'MORNING',
    'andromeda':'Andromeda Galaxy',
    'orion':'Orion Nebula',
    'sevensisters':'Seven Sisters',
    'waning':'Waning',
    'moonrise_times':'Moonrise',
    'waxing':'Waxing',
    'moonset_times':'Moonset',
    'newmoon':'New Moon',
    'firstquarter':'First Quarter',
    'fullmoon':'Full Moon',
    'lastquarter':'Last Quarter',
    'rising':'Rising',
    'mercury':'Mercury',
    'venus':'Venus',
    'mars':'Mars',
    'jupiter':'Jupiter',
    'saturn':'Saturn',
    'uranus':'Uranus',
    'neptune':'Neptune',
    'antares':'Antares',
    'transit':'Transit',
    'transit_abbrev':'Trns.',
    'arcturus':'Arcturus',
    'pollux':'Pollux',
    'deneb':'Deneb',
    'setting':'setting',
    'set_abbrev':'st.',
}
#Chinese
ch = {

}
#German
de = {

}
#Experimentally automatically detect
experiment = False
if(experiment):
    import os
    if(os.environ['LANGUAGE']=='tr_TR'):
        t=tr
    elif(os.environ['LANGUAGE']=='en_US'):
        t=en
    # elif(os.environ['LANGUAGE']=='de_DE'):
    #     t=de
    # elif(os.environ['LANGUAGE']=='?'):
    #     t=ch
    else:
        t=en
else: # otherwise manually set
    t=en

#!/usr/bin/python
# -*- coding: utf-8 -*-
#English
en = {
    'midnight':'Midnight',
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
    'rises':'Rises',
    'mercury':'Mercury',
    'venus':'Venus',
    'mars':'Mars',
    'jupiter':'Jupiter',
    'saturn':'Saturn',
    'uranus':'Uranus',
    'neptune':'Neptune',
    'antares':'Antares',
    'transits':'Transits',
    'transits_abbrev':'Trns.',
    'arcturus':'Arcturus',
    'pollux':'Pollux',
    'deneb':'Deneb',
    'sets':'Sets',
    'sets_abbrev':'Sts.',
    'ring_nebula':'Ring Nebula',
    'owl_nebula':'Owl Nebula',
    'crab_nebula':'Crab Nebula',
}
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
    'rises':'doğuyor',
    'mercury':'Merkür',
    'venus':'Venüs',
    'mars':'Mars',
    'jupiter':'Jüpiter',
    'saturn':'Satürn',
    'uranus':'Uranüs',
    'neptune':'Neptün',
    'antares':'Antares',
    'transits':'meridyende',
    'transits_abbrev':'mrd.',
    'arcturus':'Arcturus',
    'pollux':'Pollux',
    'deneb':'Deneb',
    'sets':'batıyor',
    'sets_abbrev':'bt.',
    'ring_nebula':en['ring_nebula'],
    'owl_nebula':en['owl_nebula'],
    'crab_nebula':en['crab_nebula'],
}
#Chinese
ch = {
  'midnight':'半夜',
  'evening':'晚上',
  'morning':'早晨',
  'andromeda':'仙女座星系',
  'orion':'猎户座',
  'sevensisters':'七姐 (昴)',
  'waning':'亏',
  'moonrise_times':'月出时间',
  'waxing':'打蜡',
  'moonset_times':'月落时间',
  'newmoon':'新月',
  'firstquarter':'第一季',
  'fullmoon':'满月',
  'lastquarter':'上个季度',
  'rises':'上升',
  'mercury':'水星',
  'venus':'金星',
  'mars':'火星',
  'jupiter':'木星',
  'saturn':'土星',
  'uranus':'天王星',
  'neptune':'海王星',
  'antares':'安塔尔',
  'transits':'中天',
  'transits_abbrev':'中天',
  'arcturus':'大角',
  'pollux':'北河三',
  'deneb':'天津四',
  'sets':'套',
  'sets_abbrev':'套',
  'ring_nebula':en['ring_nebula'],
  'owl_nebula':en['owl_nebula'],
  'crab_nebula':en['crab_nebula'],
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

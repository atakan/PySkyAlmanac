#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#English
en = {
    'lang':'English',
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
    'found':'found',
}
#Turkish
tr = {
    'lang':'Türk',
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
    'found':'bulundu',
}
#Chinese
zh = {
  'lang':'中國',
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
  'found':'人找到了',
}
#German
de = {
    'lang':'Deutsch',
    'midnight':'Mitternacht',
    'evening':'ABEND',
    'morning':'MORGEN',
    'andromeda':'Andromedagalaxie',
    'orion':'Orionnebel',
    'sevensisters':en['sevensisters'],
    'waning':'Abnehmender',
    'moonrise_times':'Mondaufgang',
    'waxing':'Zunehmender',
    'moonset_times':'Monduntergang',
    'newmoon':'Neumond',
    'firstquarter':'Erstes Quartal',
    'fullmoon':'Vollmond',
    'lastquarter':'Letzten Quartal',
    'rises':'Anstieg',
    'mercury':'Merkur',
    'venus':'Venus',
    'mars':'Mars',
    'jupiter':'Jupiter',
    'saturn':'Saturn',
    'uranus':'Uranus',
    'neptune':'Neptun',
    'antares':'Antares',
    'transits':'Transite',
    'transits_abbrev':'Trns.',
    'arcturus':'Arctur',
    'pollux':'Pollux',
    'deneb':'Deneb',
    'sets':'Sätze',
    'sets_abbrev':'Stz.',
    'ring_nebula':'Ringnebel',
    'owl_nebula':'Eulennebel',
    'crab_nebula':'Crabnebel',
    'found':'vorgefundener',
}
# You can set lang=de,ch,en,tr as the language. This uses the hardcoded astronomical values above.
# If you set lang='de','zh','en', 'tr' or any other string of a language, then this assumes you are wanting to try to automatically translate all of the strings. This is just using google translate (via goslate), so it possibly going to be poorly translated, but better than nothing!
lang = None
# lang = de
# lang = 'no'
experiment_detect = False
experiment_translate = False
def_lang = en
encode_these = [zh] # TODO: a list of translated languages that need to be dealt with. either deal with it here, or via latex.
if(isinstance(lang,dict)):
    if(lang in encode_these):
        # for item in lang.keys():
        #     lang[item]=lang[item].encode('utf-8')
        #     print(lang[item])
        t=def_lang # TODO: for now, until have solution
    t=lang
elif(isinstance(lang,basestring) and experiment_translate):
    try:
        print('trying automatic translation...')
        import goslate
        gs = goslate.Goslate()
        c = {}
        for key in en.keys():
            c[key] = gs.translate(en[key],t).encode('utf-8')
            #print(c[key])
        t = c
        print(lang+'...✓')
    except:
        print('Install goslate with `pip install goslate` for automatic translation.')
        t=def_lang
elif(experiment_detect and lang==None):
    #print('trying to autodetect language...')
    import os
    if(os.environ['LANGUAGE']=='tr_TR'):
        t=tr
    elif(os.environ['LANGUAGE']=='en_US'):
        t=en
    elif(os.environ['LANGUAGE']=='de_DE'):
        t=de
    # elif(os.environ['LANGUAGE']=='?'): #chinese?
    #     t=zh
    #print(t['lang']+' '+t['found']+'!')
    else:
        t=def_lang
else:
    t=def_lang
    #print('default language ('+t['lang']+') used.')

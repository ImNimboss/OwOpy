'''
Introducing you to the OwOpy module!\n
This module suits your OwOify needs perfectly, and it\'s customizable as well!\n
It can be used for BOTH normal python (synchronous code) and asynchronous code (the async/await syntax and with the asyncio module).\n
If you do not know the difference between sync and async, it is recommended to use the normal owoify() (synced function) as it is the most basic and is used for most programs and applications.\n
It has 2 functions (sync and async) -\n
sync - owoify()\n
async - aio_owoify()\n
The module\'s github link - https://github.com/Nimboss2411/OwOpy
'''

#Modules
import random

#Global variable initialisation
owo_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
owo_emotes = ['^w^', '>w< ', 'UwU ', '(・`ω\\´・)', 
    '(´・ω・\\`)', 'OwO', '◔w◔ ', '( ͡o ω ͡o )', '(O꒳O)', 
    '( °ω° )', '( ͡o ꒳ ͡o )', 'ღ(O꒳Oღ)', 
    '*𝓷𝓾𝔃𝔃𝓵𝓮𝓼 𝔂𝓸𝓾𝓻 𝓬𝓱𝓮𝓼𝓽*', '‿︵*𝓇𝒶𝓌𝓇*‿︵ ʘwʘ', 
    '✼ ҉♡ (。O⁄ ⁄ω⁄ ⁄ O。) ҉♡ ✼', '✧･ﾟ: *✧･ﾟ:*(OwO)*:･ﾟ✧*:･ﾟ✧', 
    'ᎧᏇᎧ', '♡w♡', 'ÒwÓ', '≧◡≦', '✧(˘•ω•˘)ง', '~(˶‾᷄ꈊ‾᷅˵)~', 
    'ᕙ(⇀w↼‶)ᕗ', '༼ ༎ຶ w ༎ຶ༽', '( ͡° w ͡°)', '(•w•)', '♤w♤', '♧w♧', 
    '(๑و•̀ω•́)و', '(˶‾᷄ ⁻̫ ‾᷅˵)', '꒰๑´•.̫ • `๑꒱', '・ω・', '>ω^', 
    '{・ω-*}', 'ˁ(⦿@ᴥ⦿*)ˀ', 'ʕ✿๑•́ ᴥ •̀๑✿ʔ', '(•̯͡.•̯͡)', '꒰◍ᐡᐤᐡ◍꒱', 
    '༼ (´・ω・`) ༽', '♥(⇀ᆽ↼ﾐ)∫', '✿(≗ﻌ≗^)', '( ͒ ඉ .̫ ඉ ͒)', 
    '( ^◡^)', '^•ﻌ•^', '{ @❛ꈊ❛@ }', '^•ﻌ•^ฅ', '(✿^U^)/', 
    '(≗ﻌ≗^)']

#Normal owoify function (synchronous)
def owoify(owo_string: str, level: int = 2):
    '''
    OwOifies (and UwUifies) your text!\n
    Usage - owopy.owoify('string', level) #level defaults to 2\n
    How levels work -\n
    There are three levels - 1, 2 and 3.\n
    The higher the level the more OwOified your text will be, try it out!
    '''

    if not isinstance(owo_string, str):
        raise ValueError('n...nani?! the sentence awgument must be a stwing!')
        return

    if not isinstance(level, int):
        raise ValueError('b...baka?! the level awgument must be a non-decimal numbew!')
        return

    if not level in [1, 2, 3]:
        raise ValueError('o...owo?! the level awgument must be between 1 and thwee (1 and 3 incwuded!)')
        return
    
    owo_string = owo_string.replace('r', 'w')
    owo_string = owo_string.replace('R', 'W')
    owo_string = owo_string.replace('l', 'w')
    owo_string = owo_string.replace('L', 'W')
    owo_string = owo_string.replace('b', 'bw')
    owo_string = owo_string.replace('B', 'BW')
    
    if level == 3:
        owo_string = owo_string.replace('o', 'owo')
        owo_string = owo_string.replace('O', 'OwO')
        owo_string = owo_string.replace('!', f'! {random.choice(owo_emotes)}{random.choice(owo_emotes)}')
        owo_string = owo_string.replace('?', f'? {random.choice(owo_emotes)}{random.choice(owo_emotes)}')
        owo_string = owo_string.replace('.', f'{random.choice(owo_emotes)}{random.choice(owo_emotes)}')
    if level == 2:
        owo_string = owo_string.replace('!', f'! {random.choice(owo_emotes)}')
        owo_string = owo_string.replace('?', f'? {random.choice(owo_emotes)}')
        owo_string = owo_string.replace('.', f'{random.choice(owo_emotes)}')

    for vowel in owo_vowels:
        if f'n{vowel}' in owo_string:
            owo_string = owo_string.replace(f'n{vowel}', f'ny{vowel}')
        elif f'N{vowel}' in owo_string:
            owo_string = owo_string.replace(f'N{vowel}', f'NY{vowel}')
        
    for vowel in owo_vowels:
        if f'b{vowel}' in owo_string:
            owo_string = owo_string.replace(f'b{vowel}', f'bw{vowel}')
        elif f'B{vowel}' in owo_string:
            owo_string = owo_string.replace(f'B{vowel}', f'BW{vowel}')
    
    if level == 2:
        owo_string = f'{random.choice(owo_emotes)} {owo_string} {random.choice(owo_emotes)}'
    elif level == 3:
        owo_string = f'{random.choice(owo_emotes)} {random.choice(owo_emotes)} {owo_string} {random.choice(owo_emotes)} {random.choice(owo_emotes)}'
    
    return owo_string

#Async owoify function (asynchronous)
async def aio_owoify(owo_string: str, level: int = 2):
    '''
    OwOifies (and UwUifies) your text!\n
    Usage - owopy.aio_owoify('string', level). MAKE SURE this is used asynchronously otherwise you will get Runtime Warnings and possibly Syntax Errors. The level param defaults to 2\n
    How levels work -\n
    There are three levels - 1, 2 and 3.\n
    The higher the level the more OwOified your text will be, try it out!
    '''

    async def aio_replace(main_str, first_str, second_str):
        return main_str.replace(first_str, second_str)

    if not isinstance(owo_string, str):
        raise ValueError('n...nani?! the sentence awgument must be a stwing!')
        return

    if not isinstance(level, int):
        raise ValueError('b...baka?! the level awgument must be a non-decimal numbew!')
        return

    if not level in [1, 2, 3]:
        raise ValueError('o...owo?! the level awgument must be between 1 and thwee (1 and 3 incwuded!)')
        return
    
    owo_string = await aio_replace(owo_string, 'r', 'w')
    owo_string = await aio_replace(owo_string, 'R', 'W')
    owo_string = await aio_replace(owo_string, 'l', 'w')
    owo_string = await aio_replace(owo_string, 'L', 'W')
    owo_string = await aio_replace(owo_string, 'b', 'bw')
    owo_string = await aio_replace(owo_string, 'B', 'BW')
    if level == 3:
        owo_string = await aio_replace(owo_string, 'o', 'owo')
        owo_string = await aio_replace(owo_string, 'O', 'OwO')
        owo_string = await aio_replace(owo_string, '!', f'! {random.choice(owo_emotes)}{random.choice(owo_emotes)}')
        owo_string = await aio_replace(owo_string, '?', f'? {random.choice(owo_emotes)}{random.choice(owo_emotes)}')
        owo_string = await aio_replace(owo_string, '.', f'{random.choice(owo_emotes)}{random.choice(owo_emotes)}')
    if level == 2:
        owo_string = await aio_replace(owo_string, '!', f'! {random.choice(owo_emotes)}')
        owo_string = await aio_replace(owo_string, '?', f'? {random.choice(owo_emotes)}')
        owo_string = await aio_replace(owo_string, '.', f'{random.choice(owo_emotes)}')

    for vowel in owo_vowels:
        if f'n{vowel}' in owo_string:
            owo_string = await aio_replace(owo_string, f'n{vowel}', f'ny{vowel}')
        elif f'N{vowel}' in owo_string:
            owo_string = await aio_replace(owo_string, f'N{vowel}', f'NY{vowel}')
        
    for vowel in owo_vowels:
        if f'b{vowel}' in owo_string:
            owo_string = await aio_replace(owo_string, f'b{vowel}', f'bw{vowel}')
        elif f'B{vowel}' in owo_string:
            owo_string = await aio_replace(owo_string, f'B{vowel}', f'BW{vowel}')
    
    if level == 2:
        owo_string = f'{random.choice(owo_emotes)} {owo_string} {random.choice(owo_emotes)}'
    elif level == 3:
        owo_string = f'{random.choice(owo_emotes)} {random.choice(owo_emotes)} {owo_string} {random.choice(owo_emotes)} {random.choice(owo_emotes)}'
    
    return owo_string
